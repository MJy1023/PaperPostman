"""
Paper Filter Module

Filters papers by keywords and other criteria.
"""

from typing import List, Dict
import re


def filter_by_keywords(
    papers: List[Dict],
    keywords: List[str],
    match_type: str = "any"
) -> List[Dict]:
    """
    Filter papers by keywords in title and abstract.

    Args:
        papers: List of paper dictionaries
        keywords: List of keywords to filter by
        match_type: "any" - match any keyword, "all" - match all keywords

    Returns:
        Filtered list of papers
    """
    if not keywords:
        return papers

    # Prepare keywords (lowercase, strip)
    keywords = [kw.strip().lower() for kw in keywords if kw.strip()]

    filtered = []

    for paper in papers:
        # Combine title and abstract for matching
        text = (paper.get('title', '') + ' ' + paper.get('summary', '')).lower()

        # Remove special characters for better matching
        text_clean = re.sub(r'[^\w\s]', ' ', text)

        if match_type == "any":
            if any(kw in text_clean for kw in keywords):
                filtered.append(paper)
        elif match_type == "all":
            if all(kw in text_clean for kw in keywords):
                filtered.append(paper)

    return filtered


def filter_by_categories(
    papers: List[Dict],
    categories: List[str]
) -> List[Dict]:
    """
    Filter papers by arXiv categories.

    Args:
        papers: List of paper dictionaries
        categories: List of category codes (e.g., ["cs.AI", "cs.LG"])

    Returns:
        Filtered list of papers
    """
    if not categories:
        return papers

    categories_set = set(cat.lower() for cat in categories)

    filtered = []
    for paper in papers:
        paper_categories = paper.get('categories', [])
        if any(cat.lower() in categories_set for cat in paper_categories):
            filtered.append(paper)

    return filtered


def filter_by_conference(
    papers: List[Dict],
    conferences: List[str]
) -> List[Dict]:
    """
    Filter papers by conference name.

    Args:
        papers: List of paper dictionaries
        conferences: List of conference names

    Returns:
        Filtered list of papers
    """
    if not conferences:
        return papers

    conferences_set = set(conf.lower() for conf in conferences)

    filtered = []
    for paper in papers:
        conference = paper.get('conference', '')
        if conference and conference.lower() in conferences_set:
            filtered.append(paper)

    return filtered


def filter_by_date(
    papers: List[Dict],
    min_date=None,
    max_date=None
) -> List[Dict]:
    """
    Filter papers by publication date.

    Args:
        papers: List of paper dictionaries
        min_date: Minimum date (inclusive)
        max_date: Maximum date (inclusive)

    Returns:
        Filtered list of papers
    """
    if min_date is None and max_date is None:
        return papers

    filtered = []
    for paper in papers:
        published_date = paper.get('published_date')
        if not published_date:
            continue

        include = True
        if min_date and published_date < min_date:
            include = False
        if max_date and published_date > max_date:
            include = False

        if include:
            filtered.append(paper)

    return filtered


def sort_papers(
    papers: List[Dict],
    sort_by: str = "date",
    reverse: bool = True
) -> List[Dict]:
    """
    Sort papers by specified criteria.

    Args:
        papers: List of paper dictionaries
        sort_by: "date", "title", "authors"
        reverse: Sort in descending order (for dates)

    Returns:
        Sorted list of papers
    """
    if sort_by == "date":
        # Use epoch (1970-01-01) as default for None dates
        from datetime import datetime
        epoch = datetime(1970, 1, 1)
        return sorted(
            papers,
            key=lambda p: p.get('published_date') or epoch,
            reverse=reverse
        )
    elif sort_by == "title":
        return sorted(
            papers,
            key=lambda p: p.get('title', '').lower(),
            reverse=reverse
        )
    elif sort_by == "authors":
        return sorted(
            papers,
            key=lambda p: ', '.join(p.get('authors', [])).lower(),
            reverse=reverse
        )
    else:
        return papers


def deduplicate_papers(papers: List[Dict]) -> List[Dict]:
    """
    Remove duplicate papers based on arXiv ID or title.

    Args:
        papers: List of paper dictionaries

    Returns:
        Deduplicated list of papers
    """
    seen = set()
    deduplicated = []

    for paper in papers:
        # Use arXiv ID if available, otherwise use title
        key = paper.get('id')
        if not key:
            # Create normalized title as fallback
            title = paper.get('title', '').lower().strip()
            key = title

        if key and key not in seen:
            seen.add(key)
            deduplicated.append(paper)

    return deduplicated


def limit_papers(papers: List[Dict], limit: int) -> List[Dict]:
    """
    Limit the number of papers returned.

    Args:
        papers: List of paper dictionaries
        limit: Maximum number of papers to return

    Returns:
        Limited list of papers
    """
    return papers[:limit]


def get_keyword_match_score(
    paper: Dict,
    keywords: List[str]
) -> int:
    """
    Calculate a score for how well a paper matches the keywords.

    Args:
        paper: Paper dictionary
        keywords: List of keywords

    Returns:
        Score (higher = better match)
    """
    if not keywords:
        return 0

    keywords = [kw.strip().lower() for kw in keywords if kw.strip()]
    text = (paper.get('title', '') + ' ' + paper.get('summary', '')).lower()
    text_clean = re.sub(r'[^\w\s]', ' ', text)

    score = 0
    for kw in keywords:
        # Count occurrences in title (weighted more)
        title = paper.get('title', '').lower()
        score += title.count(kw) * 3
        # Count occurrences in abstract
        score += text_clean.count(kw)

    return score


def rank_by_keyword_match(papers: List[Dict], keywords: List[str]) -> List[Dict]:
    """
    Rank papers by keyword match score.

    Args:
        papers: List of paper dictionaries
        keywords: List of keywords

    Returns:
        Ranked list of papers (highest match first)
    """
    scored = [(paper, get_keyword_match_score(paper, keywords)) for paper in papers]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [paper for paper, score in scored]


if __name__ == "__main__":
    # Test the filter
    sample_papers = [
        {
            "id": "2301.001",
            "title": "Attention Is All You Need",
            "summary": "This paper introduces the Transformer architecture for attention.",
            "authors": ["Author A", "Author B"],
            "categories": ["cs.AI"],
            "published_date": None
        },
        {
            "id": "2301.002",
            "title": "A Survey of Machine Learning",
            "summary": "This paper surveys recent advances in ML.",
            "authors": ["Author C"],
            "categories": ["cs.LG"],
            "published_date": None
        }
    ]

    keywords = ["transformer", "attention"]
    filtered = filter_by_keywords(sample_papers, keywords)
    print(f"Filtered papers: {len(filtered)}")
    for paper in filtered:
        print(f"  - {paper['title']}")
