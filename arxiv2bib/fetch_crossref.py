from typing import Dict, Any, Optional
from crossref.restful import Works, Etiquette

my_etiquette = Etiquette(
    'arxiv2bib',
    '0.1.0',
    'https://github.com/dushyant-khosla/arxiv2bib',
    'anonymous@arxiv2bib.com'
)
works = Works(etiquette=my_etiquette)

def get_publication_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    """
    Fetches publication metadata from CrossRef using its DOI.
    Args:
        doi: The DOI of the publication.
    Returns:
        A dictionary containing the publication's metadata or None if not found.
    """

    if not doi:
        return None

    try:
        data = works.doi(doi)
        if not data:
            return None

        title = data.get("title", [None])[0]
        authors = data.get("author", [])
        author_names = [f"{author.get('given', '')} {author.get('family', '')}".strip()
                        for author in authors]

        published_date = data.get("published-print", data.get("published-online", {}))
        year = published_date.get("date-parts", [[None]])[0][0]

        return {
            "title": title,
            "authors": author_names,
            "year": year,
            "doi": data.get("DOI"),
            "url": data.get("URL"),
            "publisher": data.get("publisher"),
            "journal": data.get("container-title", [None])[0],
        }
    except Exception:
        return None

def get_publication_by_title(title: str) -> Optional[Dict[str, Any]]:
    """
    Fetches publication metadata from CrossRef by title.
    Args:
        title: The title of the publication.
    Returns:
        A dictionary containing the publication's metadata or None if not found.
    """
    if not title:
        return None

    try:
        # Using the first result as the most likely match
        results = works.query(bibliographic=title).sort('relevance').order('desc')
        data = next(iter(results), None)

        if not data:
            return None

        title = data.get("title", [None])[0]
        authors = data.get("author", [])
        author_names = [f"{author.get('given', '')} {author.get('family', '')}".strip()
                        for author in authors]

        published_date = data.get("published-print", data.get("published-online", {}))
        year = published_date.get("date-parts", [[None]])[0][0]

        return {
            "title": title,
            "authors": author_names,
            "year": year,
            "doi": data.get("DOI"),
            "url": data.get("URL"),
            "publisher": data.get("publisher"),
            "journal": data.get("container-title", [None])[0],
        }
    except Exception:
        return None
