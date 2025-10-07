import click
from rich.console import Console

from .core import find_publication_on_arxiv, find_publication_on_crossref


@click.command()
@click.argument("arxiv_id")
def main(arxiv_id: str):
    """
    A CLI utility to fetch BibTeX citations from arXiv IDs.
    """

    console = Console()
    console.print(f"Fetching BibTeX for arXiv ID: [bold]{arxiv_id}[/bold]")

    with console.status("[bold green]Searching for the publication on arXiv...[/bold green]"):
        arxiv_data = find_publication_on_arxiv(arxiv_id)

    if arxiv_data:
        console.print("✅ Found paper on arXiv:")
        console.print(f"  [bold]Title:[/bold] {arxiv_data['title']}")
        authors = ", ".join(arxiv_data['authors'])
        console.print(f"  [bold]Authors:[/bold] {authors}")

        with console.status("[bold green]Searching for the publication on CrossRef...[/bold green]"):
            crossref_data = find_publication_on_crossref(arxiv_data)

        if crossref_data:
            console.print("✅ Found paper on CrossRef:")
            console.print(f"  [bold]Title:[/bold] {crossref_data['title']}")
            authors = ", ".join(crossref_data['authors'])
            console.print(f"  [bold]Authors:[/bold] {authors}")
            if "journal" in crossref_data and crossref_data["journal"]:
                console.print(f"  [bold]Journal:[/bold] {crossref_data['journal']}")
        else:
            console.print("ℹ️  Could not find a publication on CrossRef.")

        # Placeholder for next steps
        click.echo("Generating BibTeX...")
        click.echo("Done!")

    else:
        console.print(f"[bold red]Error: Could not find paper with arXiv ID: {arxiv_id}[/bold red]")

if __name__ == "__main__":
    main()
