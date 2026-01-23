"""
arXiv Paper Fetcher

Fetches papers from arXiv using the Atom feed API.
API Documentation: https://info.arxiv.org/help/api/index.html
"""

import feedparser
import urllib.parse
from datetime import datetime
from typing import List, Dict, Optional
import time


def fetch_papers(
    categories: List[str],
    max_results: int = 100,
    days_back: int = 1,
    api_base: str = "https://export.arxiv.org/api/query"
) -> List[Dict]:
    """
    Fetch latest papers from arXiv by categories.

    Args:
        categories: List of arXiv categories (e.g., ["cs.AI", "cs.CL"])
        max_results: Maximum number of results to fetch
        days_back: Number of days to look back for papers
        api_base: arXiv API base URL

    Returns:
        List of paper dictionaries with keys:
        - id: arXiv ID
        - title: Paper title
        - authors: List of author names
        - affiliations: List of author affiliations (may be empty)
        - summary: Paper abstract
        - link: URL to paper
        - published_date: Publication date
        - categories: List of arXiv categories
    """
    papers = []

    for category in categories:
        # Construct query for category and recent papers
        query = f"cat:{category}"

        # Calculate date range if specified
        if days_back > 0:
            today = datetime.utcnow()
            # arXiv uses YYYYMMDD format
            date_from = today.strftime("%Y%m%d")
            query += f" AND submittedDate:[{date_from}0000 TO {date_from}2359]"
            
            # DEBUG: Use yesterday's date for testing (临时调试指定昨天)
            # from datetime import timedelta
            # yesterday = today - timedelta(days=1)
            # date_from_debug = yesterday.strftime("%Y%m%d")
            # query += f" AND submittedDate:[{date_from_debug}0000 TO {date_from_debug}2359]"
            # DEBUG: Use yesterday's date for testing (临时调试指定昨天)

        # Encode query for URL
        encoded_query = urllib.parse.quote(query)

        # Build API URL
        url = f"{api_base}?search_query={encoded_query}&start=0&max_results={max_results}"

        try:
            # Fetch and parse the feed
            feed = feedparser.parse(url)

            if feed.bozo:
                print(f"Warning: Parse error for category {category}: {feed.bozo_exception}")

            # Extract papers from feed entries
            for entry in feed.entries:
                paper = _parse_arxiv_entry(entry, category)
                if paper:
                    papers.append(paper)

            # Small delay between requests to be polite
            time.sleep(0.5)

        except Exception as e:
            print(f"Error fetching papers for category {category}: {e}")

    return papers


def fetch_papers_by_id(
    arxiv_ids: List[str],
    api_base: str = "https://export.arxiv.org/api/query"
) -> List[Dict]:
    """
    Fetch specific papers by arXiv ID.

    Args:
        arxiv_ids: List of arXiv IDs (e.g., ["2301.07041", "cs.AI/2301.07041"])
        api_base: arXiv API base URL

    Returns:
        List of paper dictionaries
    """
    if not arxiv_ids:
        return []

    # Build ID list query
    id_list = " OR ".join(arxiv_ids)
    encoded_query = urllib.parse.quote(f"id:{id_list}")
    url = f"{api_base}?search_query={encoded_query}"

    try:
        feed = feedparser.parse(url)
        papers = []
        for entry in feed.entries:
            paper = _parse_arxiv_entry(entry)
            if paper:
                papers.append(paper)
        return papers
    except Exception as e:
        print(f"Error fetching papers by ID: {e}")
        return []


def _parse_arxiv_entry(entry, category: Optional[str] = None) -> Optional[Dict]:
    """
    Parse an arXiv feed entry into a paper dictionary.

    Args:
        entry: feedparser entry object
        category: Category that was used to fetch this paper

    Returns:
        Paper dictionary or None if parsing fails
    """
    try:
        # Extract arXiv ID from ID URL
        # Format: http://arxiv.org/abs/2301.07041v1
        arxiv_url = entry.id
        arxiv_id = arxiv_url.split("/")[-1].split("v")[0]

        # Extract authors
        authors = []
        affiliations = []
        if hasattr(entry, 'authors'):
            for author in entry.authors:
                authors.append(author.name)
                # Affiliations are not always available in arXiv API
                if hasattr(author, 'affiliation'):
                    affiliations.append(author.affiliation)

        # Extract categories
        categories = []
        if hasattr(entry, 'tags'):
            for tag in entry.tags:
                if hasattr(tag, 'term'):
                    categories.append(tag.term)

        # Parse published date
        published_date = None
        if hasattr(entry, 'published_parsed'):
            published_date = datetime(*entry.published_parsed[:6])
        elif hasattr(entry, 'updated_parsed'):
            published_date = datetime(*entry.updated_parsed[:6])

        return {
            "id": arxiv_id,
            "title": entry.title.strip(),
            "authors": authors,
            "affiliations": affiliations,
            "summary": entry.summary.strip(),
            "link": arxiv_url,
            "published_date": published_date,
            "categories": categories,
            "source": "arxiv"
        }
    except Exception as e:
        print(f"Error parsing arXiv entry: {e}")
        return None


def get_arxiv_categories() -> Dict[str, str]:
    """
    Return a dictionary of common arXiv categories and their descriptions.

    Returns:
        Dictionary mapping category codes to descriptions
    """
    return {
        "cs.AI": "Artificial Intelligence",
        "cs.CL": "Computation and Language",
        "cs.CV": "Computer Vision",
        "cs.LG": "Machine Learning",
        "cs.CR": "Cryptography and Security",
        "stat.ML": "Statistics - Machine Learning",
        "cs.NE": "Neural and Evolutionary Computing",
        "cs.IR": "Information Retrieval",
        "cs.MM": "Multimedia",
        "cs.RO": "Robotics",
    }


if __name__ == "__main__":
    # Test the fetcher
    print("Testing arXiv fetcher...")
    papers = fetch_papers(["cs.AI"], max_results=5)
    print(f"Fetched {len(papers)} papers")
    for paper in papers[:2]:
        print(f"\n{paper['title']}")
        print(f"ID: {paper['id']}")
        print(f"Authors: {', '.join(paper['authors'][:3])}...")
        print(f"Published: {paper['published_date']}")
