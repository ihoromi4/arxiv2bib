import click
from rich.console import Console

from .fetch_arxiv import fetch_arxiv_data

@click.command()
@click.argument("arxiv_id")
def main(arxiv_id: str):
    """
    A CLI utility to fetch BibTeX citations from arXiv IDs.
    """

    console = Console()
    console.print(f"Fetching BibTeX for arXiv ID: [bold]{arxiv_id}[/bold]")

    with console.status("[bold green]Searching for the paper on arXiv...[/bold green]"):
        arxiv_data = fetch_arxiv_data(arxiv_id)

    if arxiv_data:
        console.print("✅ Found paper on arXiv:")
        console.print(f"  [bold]Title:[/bold] {arxiv_data['title']}")
        authors = ", ".join(arxiv_data['authors'])
        console.print(f"  [bold]Authors:[/bold] {authors}")
        
        # Placeholder for next steps
        click.echo("Searching for the paper on CrossRef...")
        click.echo("Generating BibTeX...")
        click.echo("Done!")
    else:
        console.print(f"[bold red]Error: Could not find paper with arXiv ID: {arxiv_id}[/bold red]")

if __name__ == "__main__":
    main()
