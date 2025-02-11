import os
import click
import frontmatter
import yaml

@click.command()
@click.argument("claim_id")
@click.argument("target_id")
@click.option("--type", type=click.Choice(["support", "disproof"]), required=True)
def link_claim(claim_id, target_id, type):
    """Link data/reference to a claim as support or disproof."""
    # Load the claim's MD file
    claim_path = os.path.join("claims", f"{claim_id}.md")
    with open(claim_path, "r") as f:
        claim = frontmatter.load(f)
    
    # Determine if target is data or reference
    if target_id.startswith("DATA-"):
        field = "data"
        data_file = os.path.join(".veritas", "data.yml")
    elif target_id.startswith("REF-"):
        field = "reference"
        data_file = os.path.join(".veritas", "references.yml")
    else:
        raise click.ClickException("Invalid target ID. Must start with DATA- or REF-")
    
    # Update claim frontmatter
    if type == "support":
        claim["supports"].append({field: target_id})
    else:
        claim["disproofs"].append({field: target_id})
    
    # Save the claim
    with open(claim_path, "w") as f:
        f.write(frontmatter.dumps(claim))
    
    # Update data/reference YAML
    with open(data_file, "r") as f:
        entries = yaml.safe_load(f) or []
    for entry in entries:
        if entry["id"] == target_id:
            entry.setdefault("linked_claims", []).append({
                "claim": claim_id,
                "type": type
            })
            break
    with open(data_file, "w") as f:
        yaml.dump(entries, f)
    
    click.echo(f"✅ Linked {target_id} to {claim_id} as {type}.")