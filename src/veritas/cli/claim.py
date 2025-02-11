import os
import uuid
import click
from datetime import datetime

# Template paths
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

@click.command()
@click.argument("title")
@click.option("--repo", default=".", help="Path to the repository.")
def claim_add(title, repo):
    """Add a claim to a repository."""
    repo_path = os.path.abspath(repo)
    if not os.path.exists(os.path.join(repo_path, ".veritas")):
        raise click.ClickException(f"Not a Veritas repository: {repo_path}")
    
    claim_id = f"CLAIM-{uuid.uuid4().hex[:6].upper()}"
    date = datetime.now().strftime("%Y-%m-%d")
    
     # Load claim template
    with open(os.path.join(TEMPLATES_DIR, "claim.md"), "r") as f:
        template = f.read()

    content = template.format(
        id=claim_id,
        created=date,
        modified=date,
        title=title.strip()
    )

    claim_path = os.path.join(repo_path, "claims", f"{claim_id}.md")
    os.makedirs(os.path.dirname(claim_path), exist_ok=True)
    with open(claim_path, "w") as f:
        f.write(claim_content)
    click.echo(f"✅ Claim '{claim_id}' added to {repo_path}: {title}")