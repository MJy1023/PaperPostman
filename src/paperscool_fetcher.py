"""
Papers.cool Web Scraper

Scrapes conference papers from papers.cool venue pages.
"""

import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time


def fetch_venue_papers(
    conference: str,
    year: int = None,  # If None, extract from page title
    base_url: str = "https://papers.cool/venue"
) -> List[Dict]:
    """
    Fetch papers from a specific conference venue on papers.cool.

    Args:
        conference: Conference name (e.g., "NeurIPS", "ICLR")
        year: Year of the conference (optional, will extract from page if None)
        base_url: Base URL for papers.cool venue pages

    Returns:
        List of paper dictionaries with keys:
        - id: Paper ID (if available)
        - title: Paper title (clean, without buttons)
        - authors: List of author names
        - affiliations: List of author affiliations (may be empty)
        - summary: Paper abstract (if available)
        - link: URL to paper on papers.cool or arXiv
        - published_date: Publication date (if available)
        - conference: Conference name
        - conference_year: Conference year (extracted from page title)
        - track: Paper track (e.g., "Oral", "Poster")
        - source: "paperscool"
    """
    url = f"{base_url}/{conference}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract conference info from page header
        conference_info = _extract_conference_info(soup)

        # Override year with extracted year if not provided
        if year is None and conference_info.get('conference_year'):
            year = conference_info['conference_year']

        papers = parse_paperscool_html(soup, conference, conference_info)

        print(f"Fetched {len(papers)} papers from {conference}")
        return papers

    except requests.RequestException as e:
        print(f"Error fetching venue page for {conference}: {e}")
        return []


def fetch_multiple_venues(
    conferences: List[str],
    year: int,
    base_url: str = "https://papers.cool/venue"
) -> Dict[str, List[Dict]]:
    """
    Fetch papers from multiple conference venues.

    Args:
        conferences: List of conference names
        year: Year of the conferences
        base_url: Base URL for papers.cool venue pages

    Returns:
        Dictionary mapping conference names to lists of papers
    """
    results = {}

    for conference in conferences:
        print(f"Fetching papers from {conference}...")
        papers = fetch_venue_papers(conference, year, base_url)
        if papers:
            results[conference] = papers

        # Polite delay between requests
        time.sleep(1)

    return results


def _extract_conference_info(soup: BeautifulSoup) -> Dict:
    """
    Extract conference information from page header.

    Args:
        soup: BeautifulSoup object of the page

    Returns:
        Dictionary with conference_name, conference_year
    """
    conference_info = {
        'conference_name': '',
        'conference_year': None,
        'total_papers': 0
    }

    # Get conference name and year from <h1 class="notranslate">
    h1 = soup.find('h1', class_='notranslate')
    if h1:
        h1_text = h1.get_text(strip=True)
        # Parse "NeurIPS.2025" format
        if '.' in h1_text:
            parts = h1_text.split('.')
            if len(parts) == 2:
                conference_info['conference_name'] = parts[0]
                try:
                    conference_info['conference_year'] = int(parts[1])
                except ValueError:
                    pass

    # Get total papers count
    info_elem = soup.find('p', class_='info notranslate')
    if info_elem:
        total_text = info_elem.get_text(strip=True)
        # Extract "Total: XXX"
        match = re.search(r'Total:\s*(\d+)', total_text)
        if match:
            conference_info['total_papers'] = int(match.group(1))

    return conference_info


def parse_paperscool_html(soup: BeautifulSoup, conference: str, conference_info: Dict) -> List[Dict]:
    """
    Parse papers from papers.cool HTML content.

    The papers.cool page structure:
    - Papers are in <div class="panel paper">
    - Title is in <a class="title-link notranslate">
    - Authors are in <p class="metainfo authors notranslate"> with <a class="author notranslate">
    - Summary is in <p class="summary notranslate">
    - Track/Subject is in <p class="metainfo subjects notranslate"> with <a class="subject-X">

    Args:
        soup: BeautifulSoup object of the page
        conference: Conference name
        conference_info: Dictionary with conference metadata

    Returns:
        List of paper dictionaries
    """
    papers = []

    # papers.cool structure: <div class="panel paper">
    paper_elements = soup.find_all('div', class_='panel paper')

    for element in paper_elements:
        paper = _parse_paper_panel(element, conference, conference_info)
        if paper and paper['title']:  # Ensure we have at least a title
            papers.append(paper)

    return papers


def _parse_paper_panel(panel_div, conference: str, conference_info: Dict) -> Optional[Dict]:
    """
    Parse a single paper panel div.

    Args:
        panel_div: BeautifulSoup div element for a paper
        conference: Conference name
        conference_info: Dictionary with conference metadata

    Returns:
        Paper dictionary or None
    """
    try:
        # Find title - it's in <a class="title-link notranslate">
        title_elem = panel_div.find('a', class_='title-link notranslate')
        if not title_elem:
            return None

        title = title_elem.get_text(strip=True)
        link = title_elem.get('href', '')

        # Extract paper ID from link
        paper_id = None
        if link:
            if 'openreview.net' in link:
                # Extract ID from openreview URL
                match = re.search(r'id=([^&]+)', link)
                if match:
                    paper_id = match.group(1)
            elif 'arxiv' in link.lower():
                # Extract ID from arXiv URL
                parts = link.split('/')
                if parts:
                    paper_id = parts[-1]
            elif 'papers.cool' in link:
                # Extract ID from papers.cool URL
                parts = link.split('/')
                if len(parts) > 1:
                    paper_id = parts[-1]

        # Find authors - in <p class="metainfo authors notranslate">
        authors = []
        authors_elem = panel_div.find('p', class_='metainfo authors notranslate')
        if authors_elem:
            author_links = authors_elem.find_all('a', class_='author notranslate')
            authors = [a.get_text(strip=True) for a in author_links if a.get_text(strip=True)]

        # Find abstract - in <p class="summary notranslate">
        abstract = ""
        abstract_elem = panel_div.find('p', class_='summary notranslate')
        if abstract_elem:
            # Get the full abstract text
            abstract = abstract_elem.get_text(strip=True)
            # Remove any "more" or similar text if present
            abstract = re.sub(r'\.\.\.$', '.', abstract)

        # Extract track/subject info - in <p class="metainfo subjects notranslate">
        track = None
        subjects_elem = panel_div.find('p', class_='metainfo subjects notranslate')
        if subjects_elem:
            # Parse links like "/venue/NeurIPS.2025?group=Oral"
            subject_links = subjects_elem.find_all('a')
            for subject_link in subject_links:
                link_text = subject_link.get_text(strip=True)
                href = subject_link.get('href', '')
                # Extract track from link
                if 'group=' in href:
                    match = re.search(r'group=([^&]+)', href)
                    if match:
                        track = match.group(1)
                        break

        # Build conference display string with year and track
        conference_display = conference_info.get('conference_name', conference)
        conference_year = conference_info.get('conference_year')
        if conference_year:
            conference_display += f'.{conference_year}'
        if track:
            conference_display += f' - {track}'

        return {
            "id": paper_id,
            "title": title,
            "authors": authors,
            "affiliations": [],
            "summary": abstract,
            "link": link,
            "published_date": None,
            "conference": conference_display,
            "conference_year": conference_year,
            "track": track,
            "source": "paperscool"
        }

    except Exception as e:
        print(f"Error parsing paper panel: {e}")
        return None


def search_papers(
    query: str,
    base_url: str = "https://papers.cool"
) -> List[Dict]:
    """
    Search papers on papers.cool by keyword.

    Args:
        query: Search query string
        base_url: Base URL for papers.cool

    Returns:
        List of paper dictionaries
    """
    search_url = f"{base_url}/search?q={requests.utils.quote(query)}"

    try:
        response = requests.get(search_url, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # For search, conference info might not be available
        conference_info = {'conference_name': 'search', 'conference_year': None, 'total_papers': 0}
        papers = parse_paperscool_html(soup, 'search', conference_info)

        return papers

    except requests.RequestException as e:
        print(f"Error searching papers.cool: {e}")
        return []


if __name__ == "__main__":
    # Test the fetcher
    print("Testing papers.cool fetcher...")
    papers = fetch_venue_papers("NeurIPS", 2024)
    print(f"Fetched {len(papers)} papers from NeurIPS")
    for paper in papers[:3]:
        print(f"\nTitle: {paper['title']}")
        print(f"ID: {paper['id']}")
        print(f"Conference: {paper['conference']}")
        print(f"Track: {paper['track']}")
        print(f"Authors: {', '.join(paper['authors'][:3])}...")
        print(f"Summary length: {len(paper['summary'])}")
