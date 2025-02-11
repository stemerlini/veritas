import frontmatter
import yaml

def parse_markdown(file_path):
    """Parse a Markdown file with frontmatter."""
    with open(file_path, "r") as f:
        return frontmatter.load(f)

def parse_yaml(file_path):
    """Parse a YAML file."""
    with open(file_path, "r") as f:
        return yaml.safe_load(f)