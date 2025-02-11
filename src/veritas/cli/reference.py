import os
import click
import yaml
from veritas.utils import slugify

@click.command()
@click.argument("doi")
@click.option("--desc", prompt="Description")
@click.option("--repo", default=".", help="Path to the repository.")
def ref_add(doi, desc, repo):
    """Add a dataset to a repository."""
    repo_path = os.path.abspath(repo)
    if not os.path.exists(os.path.join(repo_path, ".veritas")):
        raise click.ClickException(f"Not a Veritas repository: {repo_path}")
    
    ref_id = f"REF-{slugify(doi)}"
    ref_entry = {"id": ref_id, "DOI": {doi}, "description": desc, "linked_claims": []}
    ref_file = os.path.join(repo_path, ".veritas", "references.yml")
    
    # Load existing reference
    reference = []
    if os.path.exists(ref_file):
        with open(ref_file, "r") as f:
            reference = yaml.safe_load(f) or []
    # Append new reference
    reference.append(ref_entry)
    with open(ref_file, "w") as f:
        yaml.dump(reference, f)
    click.echo(f"✅ Data '{ref_id}' added to {repo_path}: {doi}")