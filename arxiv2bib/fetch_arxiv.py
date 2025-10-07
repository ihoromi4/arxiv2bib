from typing import Dict, Any, Optional

import arxiv


def fetch_arxiv_data(arxiv_id: str) -> Optional[Dict[str, Any]]:
    """
    Fetches paper metadata from arXiv using its ID.

    Args:
        arxiv_id: The arXiv ID of the paper.

    Returns:
        A dictionary containing the paper's metadata or None if not found.
    """

    try:
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(search.results())

        authors = [author.name for author in paper.authors]

        metadata = {
            "title": paper.title,
            "authors": authors,
            "year": paper.published.year,
            "doi": paper.doi,
            "url": paper.entry_id,
            "pdf_url": paper.pdf_url,
        }
        return metadata
    except StopIteration:
        return None
