import os
import click
import yaml
from veritas.utils import slugify

@click.command()
@click.argument("name")
@click.option("--desc", prompt="Description")
@click.option("--repo", default=".", help="Path to the repository.")
def data_add(name, desc, repo):
    """Add a dataset to a repository."""
    repo_path = os.path.abspath(repo)
    if not os.path.exists(os.path.join(repo_path, ".veritas")):
        raise click.ClickException(f"Not a Veritas repository: {repo_path}")
    
    data_id = f"DATA-{slugify(name)}"
    data_entry = {"id": data_id, "name": name, "description": desc}
    data_file = os.path.join(repo_path, ".veritas", "data.yml")
    
    # Load existing data
    data = []
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            data = yaml.safe_load(f) or []
    
    # Append new data
    data.append(data_entry)
    with open(data_file, "w") as f:
        yaml.dump(data, f)
    
    click.echo(f"✅ Data '{data_id}' added to {repo_path}: {name}")