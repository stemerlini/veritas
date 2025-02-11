import os
import click
from git import Repo

@click.command()
@click.argument("repo_name")
def init(repo_name):
    """Initialize a new Veritas repository."""
    os.makedirs(repo_name, exist_ok=True)
    os.makedirs(os.path.join(repo_name, "claims"), exist_ok=True)
    os.makedirs(os.path.join(repo_name, ".veritas"), exist_ok=True)
    open(os.path.join(repo_name, "references.md"), "w").close()
    open(os.path.join(repo_name, "data.md"), "w").close()
    Repo.init(repo_name)
    click.echo(f"✅ Repository '{repo_name}' initialized.")