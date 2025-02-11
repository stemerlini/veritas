import os
import click
from veritas.utils.server import start_web_app

@click.command()
def viz():
    """Launch the Veritas web app."""
    start_web_app()