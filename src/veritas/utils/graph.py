import json
import os

def generate_graph_json(repo_path):
    """Generate graph.json from a Veritas repository."""
    graph_data = {
        "repositories": []
    }
    for repo in os.listdir(repo_path):
        repo_path_full = os.path.join(repo_path, repo)
        if os.path.exists(os.path.join(repo_path_full, ".veritas")):
            repo_data = parse_repo(repo_path_full)
            graph_data["repositories"].append(repo_data)
    
    with open("graph.json", "w") as f:
        json.dump(graph_data, f, indent=2)