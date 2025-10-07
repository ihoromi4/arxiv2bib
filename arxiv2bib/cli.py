import click

@click.command()
@click.argument("arxiv_id")
def main(arxiv_id):
    """
    A CLI utility to fetch BibTeX citations from arXiv IDs.
    """
    click.echo(f"Fetching BibTeX for arXiv ID: {arxiv_id}")
    click.echo("Searching for the paper on arXiv...")
    click.echo("Searching for the paper on CrossRef...")
    click.echo("Generating BibTeX...")
    click.echo("Done!")

if __name__ == "__main__":
    main()
