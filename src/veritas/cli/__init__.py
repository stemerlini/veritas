import click
from veritas.cli.init import init
from veritas.cli.claim import claim_add
from veritas.cli.data import data_add
from veritas.cli.link import link_claim
from veritas.cli.reference import ref_add
from veritas.cli.viz import viz
# from veritas.cli.template import template

@click.group()
def cli():
    """Veritas CLI: Lowering the entropy of knowledge."""
    pass

# Add commands
cli.add_command(init)
cli.add_command(claim_add)
cli.add_command(data_add)
cli.add_command(ref_add)
cli.add_command(link_claim)
cli.add_command(viz)
# cli.add_command(template)