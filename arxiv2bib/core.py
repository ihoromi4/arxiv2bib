from typing import Dict, Any, Optional

from .fetch_arxiv import fetch_arxiv_data
from .fetch_crossref import get_publication_by_doi, get_publication_by_title


def find_publication_on_arxiv(arxiv_id: str) -> Optional[Dict[str, Any]]:
    """
    Finds the publication metadata for a given arXiv ID from arXiv.

    Args:
        arxiv_id: The arXiv ID of the paper.

    Returns:
        A dictionary with the publication metadata or None if not found.
    """

    return fetch_arxiv_data(arxiv_id)


def find_publication_on_crossref(
        arxiv_meta: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:

    """
    Finds the publication metadata for a given arXiv metadata on CrossRef.

    If a DOI is available, it uses CrossRef to find the published version.
    Otherwise, it searches CrossRef by title.

    Args:
        arxiv_meta: The arXiv metadata of the paper.

    Returns:
        A dictionary with the publication metadata or None if not found.
    """

    publication_meta = None
    if arxiv_meta.get("doi"):
        publication_meta = get_publication_by_doi(arxiv_meta["doi"])

    if not publication_meta:
        publication_meta = get_publication_by_title(arxiv_meta["title"])

    return publication_meta
