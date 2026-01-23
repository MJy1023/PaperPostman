"""
README Generator Module

Generates the main README.md file with Latest News,
Weekly Summary, and Daily Recommendation sections.
"""

import random
from datetime import datetime
from typing import List, Dict, Optional


def generate_readme(
    latest_papers: List[Dict],
    daily_recommendations: List[Dict],
    weekly_summary: str,
    last_updated: str = None,
    template: Optional[str] = None
) -> str:
    """
    Generate the complete README content.

    Args:
        latest_papers: Papers for Latest News section
        daily_recommendations: Papers for Daily Recommendation section
        weekly_summary: Weekly summary text (may be empty)
        last_updated: Last updated timestamp (defaults to now)
        template: Optional README template

    Returns:
        Complete README content as string
    """
    if last_updated is None:
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    readme_parts = []

    # Header
    readme_parts.append("# PaperPostman\n")
    readme_parts.append("> Automatically curated research papers from arXiv and papers.cool\n")
    readme_parts.append(f"\n**Last Updated:** {last_updated}\n")
    readme_parts.append("---\n")

    # Latest News Section
    readme_parts.append(_generate_latest_news_section(latest_papers))

    # Daily Recommendation Section
    readme_parts.append(_generate_daily_recommendation_section(daily_recommendations))

    # Weekly Summary Section (only if summary exists)
    if weekly_summary and weekly_summary.strip():
        readme_parts.append(_generate_weekly_summary_section(weekly_summary))

    # Footer
    readme_parts.append("\n---\n")
    readme_parts.append("\n*This repository is automatically maintained by PaperPostman.*\n")
    readme_parts.append("*Archived READMEs can be found in the [archive/](archive/) directory.*\n")

    return "".join(readme_parts)


def _generate_latest_news_section(papers: List[Dict]) -> str:
    """
    Generate the Latest News section.

    Args:
        papers: List of paper dictionaries

    Returns:
        Markdown string for Latest News section
    """
    section = "\n## Latest News\n\n"

    if not papers:
        section += "*No new papers matching your keywords found today.*\n\n"
        return section

    section += f"*{len(papers)} papers found matching your keywords.*\n\n"

    for i, paper in enumerate(papers, 1):
        section += f"### {i}. {paper['title']}\n\n"

        # Authors
        authors = paper.get('authors', [])
        if authors:
            author_list = ', '.join(authors[:5])
            if len(authors) > 5:
                author_list += ' et al.'
            section += f"**Authors:** {author_list}\n\n"

        # Affiliations
        affiliations = paper.get('affiliations', [])
        if affiliations:
            aff_list = ', '.join(affiliations[:3])
            if len(affiliations) > 3:
                aff_list += ' et al.'
            section += f"**Affiliations:** {aff_list}\n\n"

        # Published date
        published_date = paper.get('published_date')
        if published_date:
            section += f"**Published:** {published_date.strftime('%Y-%m-%d')}\n\n"

        # Conference or Categories
        conference = paper.get('conference')
        if conference:
            section += f"**Conference:** {conference}\n\n"
            # Also display conference_year if available
            conference_year = paper.get('conference_year')
            if conference_year:
                section += f"**Year:** {conference_year}\n\n"
            # Also display track if available
            track = paper.get('track')
            if track:
                section += f"**Track:** {track}\n\n"
        else:
            categories = paper.get('categories', [])
            if categories:
                section += f"**Categories:** {', '.join(categories)}\n\n"

        # Link
        link = paper.get('link', '')
        if link:
            section += f"**[Read Paper]({link})**\n\n"

        # Abstract (display full abstract, no truncation)
        summary = paper.get('summary', '')
        if summary:
            section += f"{summary}\n\n"

        section += "---\n\n"

    return section


def _generate_daily_recommendation_section(papers: List[Dict]) -> str:
    """
    Generate the Daily Recommendation section.

    Args:
        papers: List of recommended paper dictionaries

    Returns:
        Markdown string for Daily Recommendation section
    """
    section = "\n## Daily Recommendation\n\n"

    if not papers:
        section += "*No daily recommendation available.*\n\n"
        return section

    for paper in papers:
        section += f"### 🌟 {paper['title']}\n\n"

        # Authors
        authors = paper.get('authors', [])
        if authors:
            author_list = ', '.join(authors[:3])
            if len(authors) > 3:
                author_list += ' et al.'
            section += f"**Authors:** {author_list}\n\n"

        # Conference
        conference = paper.get('conference')
        if conference:
            section += f"**Conference:** {conference}\n\n"

        # Link
        link = paper.get('link', '')
        if link:
            section += f"**[Read Paper]({link})**\n\n"

        # Abstract (display full abstract, no truncation)
        summary = paper.get('summary', '')
        if summary:
            section += f"{summary}\n\n"

    section += "---\n\n"

    return section


def _generate_weekly_summary_section(summary: str) -> str:
    """
    Generate the Weekly Summary section.

    Args:
        summary: Weekly summary text

    Returns:
        Markdown string for Weekly Summary section
    """
    section = "\n## Weekly Summary\n\n"

    # Add timestamp
    today = datetime.now().strftime("%Y-%m-%d")
    section += f"*Week ending {today}*\n\n"
    section += "---\n\n"
    section += summary
    section += "\n\n---\n\n"

    return section


def select_random_recommendations(
    papers: List[Dict],
    count: int = 1,
    source: str = "conferences"
) -> List[Dict]:
    """
    Randomly select papers for daily recommendation.

    Args:
        papers: List of all papers
        count: Number of papers to select
        source: "conferences", "arxiv", or "both"

    Returns:
        List of selected papers
    """
    # Filter by source
    if source == "conferences":
        filtered = [p for p in papers if p.get('conference')]
    elif source == "arxiv":
        filtered = [p for p in papers if not p.get('conference')]
    else:
        filtered = papers

    # Handle edge cases
    if not filtered:
        return []

    # Randomly select papers
    count = min(count, len(filtered))
    selected = random.sample(filtered, count)

    return selected


def format_authors(authors: List[str], max_display: int = 5) -> str:
    """
    Format author list for display.

    Args:
        authors: List of author names
        max_display: Maximum number of authors to display

    Returns:
        Formatted author string
    """
    if not authors:
        return "Unknown"

    if len(authors) <= max_display:
        return ', '.join(authors)
    else:
        return ', '.join(authors[:max_display]) + ' et al.'


def format_date(date: datetime) -> str:
    """
    Format date for display.

    Args:
        date: datetime object

    Returns:
        Formatted date string
    """
    if date is None:
        return "N/A"
    return date.strftime("%Y-%m-%d")


def create_initial_readme() -> str:
    """
    Create an initial README when no data is available yet.

    Returns:
        Initial README content
    """
    readme = """# PaperPostman

> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** Setup in progress

---

## Latest News

*Welcome to PaperPostman! This repository will be automatically updated with the latest research papers.*

---

## Daily Recommendation

*Daily recommendations will appear here after the first update.*

---

## Weekly Summary

*Weekly summaries will appear here on Fridays.*

---

---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
"""
    return readme


if __name__ == "__main__":
    # Test the generator
    sample_papers = [
        {
            "id": "2301.001",
            "title": "Attention Is All You Need",
            "authors": ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar"],
            "affiliations": ["Google Brain"],
            "summary": "This paper introduces the Transformer architecture, which relies entirely on attention mechanisms and eliminates recurrence and convolution.",
            "link": "https://arxiv.org/abs/1706.03762",
            "categories": ["cs.CL"],
            "source": "arxiv"
        }
    ]

    print("Testing README generator...")
    readme = generate_readme(
        latest_papers=sample_papers,
        daily_recommendations=sample_papers[:1],
        weekly_summary=""
    )
    print("README generated successfully!")
