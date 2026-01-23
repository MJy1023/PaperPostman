#!/usr/bin/env python3
"""
PaperPostman - Main Entry Point

Automatically fetches papers from arXiv and papers.cool,
filters by keywords, and updates the README.

Latest News section: Uses arXiv papers only (daily updates)
Daily Recommendation section: Uses papers.cool conference papers
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add src directory to path for imports
src_dir = Path(__file__).parent
sys.path.insert(0, str(src_dir))

import yaml
from arxiv_fetcher import fetch_papers
from paperscool_fetcher import fetch_multiple_venues
from paper_filter import (
    filter_by_keywords,
    sort_papers,
    deduplicate_papers,
    limit_papers
)
from readme_generator import (
    generate_readme,
    select_random_recommendations,
    create_initial_readme
)
from llm_summarizer import summarize_weekly_papers, is_summary_day
from storage import (
    save_papers,
    load_papers,
    archive_readme,
    save_weekly_papers,
    load_weekly_papers,
    load_config,
    append_papers
)


def load_config_file(config_path: str = None) -> dict:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to config file (defaults to src/config.yaml)

    Returns:
        Configuration dictionary
    """
    if config_path is None:
        config_path = os.path.join(src_dir, "config.yaml")

    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        return {}

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f) or {}

    # Replace environment variables in string values
    config = _resolve_env_vars(config)

    return config


def _resolve_env_vars(config: dict) -> dict:
    """
    Recursively replace ${VAR} environment variable references in config values.

    Args:
        config: Configuration dictionary

    Returns:
        Config with resolved environment variables
    """
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(item) for item in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.environ.get(env_var, config)
    else:
        return config


def get_project_paths(config: dict) -> dict:
    """
    Get all project path configurations.

    Args:
        config: Configuration dictionary

    Returns:
        Dictionary of project paths
    """
    project_root = Path(__file__).parent.parent

    paths = {
        'project_root': project_root,
        'readme': project_root / "README.md",
        'archive': project_root / config.get('archive_dir', 'archive'),
        'data': project_root / config.get('data_dir', 'data'),
        'papers_json': project_root / "data" / "papers.json"
    }

    return paths


def main():
    """Main execution function."""
    print("=== PaperPostman Starting ===")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print()

    # Load configuration
    config = load_config_file()
    if not config:
        print("Error: Could not load configuration.")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"  Keywords: {', '.join(config.get('keywords', [])[:5])}...")
    print(f"  arXiv categories: {', '.join(config.get('arxiv_categories', []))}")
    print(f"  Conferences: {', '.join(config.get('conferences', []))}")
    print()

    # Get project paths
    paths = get_project_paths(config)
    paths['data'].mkdir(parents=True, exist_ok=True)
    paths['archive'].mkdir(parents=True, exist_ok=True)

    # Step 1: Fetch arXiv papers (for Latest News)
    print("Step 1: Fetching arXiv papers...")
    arxiv_papers = fetch_papers(
        categories=config.get('arxiv_categories', []),
        max_results=100,
        api_base=config.get('arxiv_api_base', 'https://export.arxiv.org/api/query')
    )
    print(f"  Found {len(arxiv_papers)} papers from arXiv")

    # Step 2: Fetch conference papers from papers.cool (for Daily Recommendation)
    print("\nStep 2: Fetching conference papers from papers.cool...")
    conferences = config.get('conferences', [])

    # Flatten conference papers into a single list
    conference_papers = []
    for conference in conferences:
        print(f"  Fetching {conference}...")
        from paperscool_fetcher import fetch_venue_papers
        # Don't pass year parameter - let it extract from page title automatically
        papers = fetch_venue_papers(
            conference=conference,
            year=None,  # Extract year from page title
            base_url=config.get('paperscool_base_url', 'https://papers.cool/venue')
        )
        conference_papers.extend(papers)
        print(f"    {len(papers)} papers from {conference}")

    print(f"\n  Total: {len(conference_papers)} papers from conferences")

    # Step 3: Filter arXiv papers for Latest News
    print("\nStep 3: Filtering arXiv papers for Latest News...")
    keywords = config.get('keywords', [])

    # Filter arXiv papers (for Latest News)
    arxiv_filtered = filter_by_keywords(arxiv_papers, keywords)
    arxiv_filtered = deduplicate_papers(arxiv_filtered)
    arxiv_filtered = sort_papers(arxiv_filtered, sort_by="date", reverse=True)
    papers_per_day = config.get('papers_per_day', 20)
    latest_papers = limit_papers(arxiv_filtered, papers_per_day)

    print(f"  {len(arxiv_filtered)} arXiv papers match keywords")
    print(f"  Displaying top {len(latest_papers)} papers for Latest News")

    # Step 4: Filter conference papers for Daily Recommendation
    print("\nStep 4: Filtering conference papers for Daily Recommendation...")
    conference_filtered = filter_by_keywords(conference_papers, keywords)
    conference_filtered = deduplicate_papers(conference_filtered)

    print(f"  {len(conference_filtered)} conference papers match keywords")

    # Step 5: Save all papers (both sources)
    print("\nStep 5: Saving all papers to storage...")
    all_papers = arxiv_papers + conference_papers
    save_papers(all_papers, str(paths['papers_json']))
    print("  Papers saved to data/papers.json")

    # Step 6: Generate daily recommendation (from conference papers only)
    print("\nStep 6: Generating daily recommendation...")
    daily_rec_count = config.get('daily_recommendation_count', 1)

    daily_recommendations = select_random_recommendations(
        conference_filtered,  # Use only conference papers
        count=daily_rec_count,
        source="conferences"
    )

    if daily_recommendations:
        print(f"  Selected {len(daily_recommendations)} paper(s) for recommendation")
        for paper in daily_recommendations:
            print(f"    - {paper.get('title', 'N/A')[:50]}...")
    else:
        print("  No recommendations generated (no matching conference papers)")

    # Step 7: Generate weekly summary (if today is summary day)
    weekly_summary = ""
    summary_day = config.get('weekly_summary_day', 'Friday')

    if is_summary_day(summary_day):
        print(f"\nStep 7: Generating weekly summary (today is {summary_day})...")

        # Load weekly papers (only arXiv papers for weekly summary)
        weekly_papers = load_weekly_papers(str(paths['data'] / 'weekly'))
        print(f"  {len(weekly_papers)} arXiv papers accumulated this week")

        if weekly_papers:
            llm_api_base = config.get('llm_api_base', '')
            llm_api_key = config.get('llm_api_key', '')
            llm_model = config.get('llm_model', 'deepseek-chat')
            llm_temperature = config.get('llm_temperature', 0.7)
            llm_max_tokens = config.get('llm_max_tokens', 2000)

            if llm_api_base and llm_api_key and llm_api_key != '${DEEPSEEK_API_KEY}':
                print("  Calling LLM API...")
                try:
                    weekly_summary = summarize_weekly_papers(
                        papers=weekly_papers,
                        api_base=llm_api_base,
                        api_key=llm_api_key,
                        model=llm_model,
                        temperature=llm_temperature,
                        max_tokens=llm_max_tokens
                    )
                    print("  Weekly summary generated")
                except Exception as e:
                    print(f"  Error generating weekly summary: {e}")
                    weekly_summary = f"*Error generating summary: {str(e)}*"
            else:
                print("  LLM API not configured, skipping summary")
                weekly_summary = f"*Summary generation skipped - LLM API not configured.*"
        else:
            print("  No papers to summarize this week")
            weekly_summary = "*No papers to summarize this week.*"
    else:
        print(f"\nStep 7: Skipping weekly summary (today is not {summary_day})")

    # Step 8: Save arXiv papers for weekly summary
    print("\nStep 8: Saving arXiv papers for weekly summary...")
    save_weekly_papers(arxiv_filtered, str(paths['data'] / 'weekly'))

    # Step 9: Archive previous README
    print("\nStep 9: Archiving previous README...")
    if paths['readme'].exists():
        archive_readme(str(paths['readme']), str(paths['archive']))
        print("  Previous README archived")
    else:
        print("  No existing README to archive")

    # Step 10: Generate and write new README
    print("\nStep 10: Generating new README...")
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    readme_content = generate_readme(
        latest_papers=latest_papers,
        daily_recommendations=daily_recommendations,
        weekly_summary=weekly_summary,
        last_updated=last_updated
    )

    with open(paths['readme'], 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"  README generated and saved to {paths['readme']}")

    print("\n=== PaperPostman Complete ===")
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")


def run_init():
    """Run initialization - create initial README."""
    print("Initializing PaperPostman...")
    paths = get_project_paths(load_config_file())

    # Create directories
    paths['data'].mkdir(parents=True, exist_ok=True)
    paths['archive'].mkdir(parents=True, exist_ok=True)

    # Create initial README
    initial_readme = create_initial_readme()
    with open(paths['readme'], 'w', encoding='utf-8') as f:
        f.write(initial_readme)

    print(f"Initial README created at {paths['readme']}")
    print("Project initialized successfully!")


if __name__ == "__main__":
    # Command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--init":
            run_init()
        elif sys.argv[1] == "--help":
            print("PaperPostman - Automated paper fetcher and README updater")
            print("\nUsage:")
            print("  python main.py          # Run daily update")
            print("  python main.py --init   # Initialize project (create initial README)")
            print("  python main.py --help   # Show this help")
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Use --help for usage information")
            sys.exit(1)
    else:
        main()
