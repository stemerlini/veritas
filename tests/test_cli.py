from veritas.cli.init import init
import os
import pytest

def test_init_command(tmpdir):
    # # Change to the temporary directory
    os.chdir(tmpdir)
    
    # Run the init command
    repo_name = "test-repo"
    init([repo_name])  # Pass the repository name as a list of arguments
    
    # Verify the repository was created
    assert os.path.exists(repo_name)
    assert os.path.exists(os.path.join(repo_name, "claims"))
    assert os.path.exists(os.path.join(repo_name, ".veritas"))