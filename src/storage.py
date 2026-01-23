"""
Storage Module

Handles saving and loading papers, archiving README files,
and managing persistent data.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


def save_papers(
    papers: List[Dict],
    filepath: str
) -> bool:
    """
    Save papers to a JSON file.

    Args:
        papers: List of paper dictionaries
        filepath: Path to save the file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(papers, f, ensure_ascii=False, indent=2, default=_json_serializer)

        return True
    except Exception as e:
        print(f"Error saving papers to {filepath}: {e}")
        return False


def load_papers(filepath: str) -> List[Dict]:
    """
    Load papers from a JSON file.

    Args:
        filepath: Path to the JSON file

    Returns:
        List of paper dictionaries (empty list if file doesn't exist or error)
    """
    try:
        if not os.path.exists(filepath):
            return []

        with open(filepath, 'r', encoding='utf-8') as f:
            papers = json.load(f)

        return papers if isinstance(papers, list) else []
    except Exception as e:
        print(f"Error loading papers from {filepath}: {e}")
        return []


def append_papers(
    papers: List[Dict],
    filepath: str
) -> bool:
    """
    Append new papers to an existing JSON file, avoiding duplicates.

    Args:
        papers: List of new paper dictionaries
        filepath: Path to the JSON file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Load existing papers
        existing = load_papers(filepath)

        # Track seen IDs to avoid duplicates
        seen_ids = {p.get('id') for p in existing if p.get('id')}
        seen_titles = {p.get('title') for p in existing if p.get('title')}

        # Add only new papers
        for paper in papers:
            paper_id = paper.get('id')
            paper_title = paper.get('title')

            # Skip if duplicate by ID or title
            if (paper_id and paper_id in seen_ids) or \
               (paper_title and paper_title in seen_titles):
                continue

            existing.append(paper)
            if paper_id:
                seen_ids.add(paper_id)
            if paper_title:
                seen_titles.add(paper_title)

        # Save updated list
        return save_papers(existing, filepath)

    except Exception as e:
        print(f"Error appending papers to {filepath}: {e}")
        return False


def archive_readme(
    readme_path: str,
    archive_dir: str,
    date: Optional[datetime] = None
) -> bool:
    """
    Archive a README file to a date-named subdirectory.

    Args:
        readme_path: Path to the current README file
        archive_dir: Directory to store archives
        date: Date for the archive (defaults to today)

    Returns:
        True if successful, False otherwise
    """
    if not os.path.exists(readme_path):
        return True  # Nothing to archive

    try:
        if date is None:
            date = datetime.now()

        # Create archive path: archive/YYYY-MM-DD/README.md
        date_str = date.strftime("%Y-%m-%d")
        archive_path = os.path.join(archive_dir, date_str, "README.md")

        # Create archive directory
        os.makedirs(os.path.dirname(archive_path), exist_ok=True)

        # Copy README to archive
        with open(readme_path, 'r', encoding='utf-8') as src:
            content = src.read()

        with open(archive_path, 'w', encoding='utf-8') as dst:
            dst.write(content)

        print(f"Archived README to {archive_path}")
        return True

    except Exception as e:
        print(f"Error archiving README: {e}")
        return False


def save_weekly_papers(
    papers: List[Dict],
    weekly_dir: str,
    date: Optional[datetime] = None
) -> bool:
    """
    Save papers for weekly summarization.

    Args:
        papers: List of paper dictionaries
        weekly_dir: Directory to store weekly data
        date: Date for the week (defaults to today)

    Returns:
        True if successful, False otherwise
    """
    try:
        if date is None:
            date = datetime.now()

        # Get week number and year
        week_number = date.isocalendar()[1]
        year = date.year

        # Create filename: weekly/YYYY/week_XX.json
        week_dir = os.path.join(weekly_dir, str(year))
        filename = f"week_{week_number:02d}.json"
        filepath = os.path.join(week_dir, filename)

        # Append papers to the weekly file
        return append_papers(papers, filepath)

    except Exception as e:
        print(f"Error saving weekly papers: {e}")
        return False


def load_weekly_papers(
    weekly_dir: str,
    date: Optional[datetime] = None
) -> List[Dict]:
    """
    Load papers for the current week.

    Args:
        weekly_dir: Directory storing weekly data
        date: Date to get the week for (defaults to today)

    Returns:
        List of paper dictionaries
    """
    try:
        if date is None:
            date = datetime.now()

        # Get week number and year
        week_number = date.isocalendar()[1]
        year = date.year

        # Load from file
        week_dir = os.path.join(weekly_dir, str(year))
        filename = f"week_{week_number:02d}.json"
        filepath = os.path.join(week_dir, filename)

        return load_papers(filepath)

    except Exception as e:
        print(f"Error loading weekly papers: {e}")
        return []


def clear_old_weekly_data(
    weekly_dir: str,
    max_weeks_to_keep: int = 4
) -> bool:
    """
    Clear old weekly data files.

    Args:
        weekly_dir: Directory storing weekly data
        max_weeks_to_keep: Number of weeks to keep

    Returns:
        True if successful, False otherwise
    """
    try:
        current_week = datetime.now().isocalendar()[1]
        current_year = datetime.now().year

        for year_dir in Path(weekly_dir).iterdir():
            if year_dir.is_dir():
                year = int(year_dir.name)
                for week_file in year_dir.glob("week_*.json"):
                    week_number = int(week_file.stem.split("_")[1])

                    # Calculate weeks difference
                    weeks_ago = 0
                    if year == current_year:
                        weeks_ago = current_week - week_number
                    elif year < current_year:
                        # Approximate (52 weeks per year)
                        weeks_ago = (current_year - year) * 52 + current_week - week_number

                    if weeks_ago > max_weeks_to_keep:
                        week_file.unlink()
                        print(f"Deleted old weekly data: {week_file}")

        return True

    except Exception as e:
        print(f"Error clearing old weekly data: {e}")
        return False


def save_config(
    config: Dict,
    filepath: str
) -> bool:
    """
    Save configuration to a YAML-like or JSON file.

    Args:
        config: Configuration dictionary
        filepath: Path to save the file

    Returns:
        True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Use YAML if available, otherwise JSON
        try:
            import yaml
            with open(filepath, 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
        except ImportError:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)

        return True
    except Exception as e:
        print(f"Error saving config to {filepath}: {e}")
        return False


def load_config(filepath: str) -> Dict:
    """
    Load configuration from a YAML or JSON file.

    Args:
        filepath: Path to the configuration file

    Returns:
        Configuration dictionary (empty dict if file doesn't exist)
    """
    try:
        if not os.path.exists(filepath):
            return {}

        with open(filepath, 'r') as f:
            content = f.read()

        # Try YAML first, then JSON
        try:
            import yaml
            return yaml.safe_load(content) or {}
        except ImportError:
            return json.loads(content) or {}

    except Exception as e:
        print(f"Error loading config from {filepath}: {e}")
        return {}


def _json_serializer(obj):
    """
    Custom JSON serializer for datetime objects.
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not JSON serializable")


def get_archive_dates(archive_dir: str) -> List[str]:
    """
    Get list of available archive dates.

    Args:
        archive_dir: Directory containing archives

    Returns:
        List of date strings in YYYY-MM-DD format
    """
    try:
        if not os.path.exists(archive_dir):
            return []

        dates = []
        for entry in os.listdir(archive_dir):
            if os.path.isdir(os.path.join(archive_dir, entry)):
                dates.append(entry)

        return sorted(dates, reverse=True)

    except Exception as e:
        print(f"Error getting archive dates: {e}")
        return []


if __name__ == "__main__":
    # Test storage functions
    print("Storage module loaded.")
    print("Functions available: save_papers, load_papers, append_papers,")
    print("                    archive_readme, save_weekly_papers, load_weekly_papers")
