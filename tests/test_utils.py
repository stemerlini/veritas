from veritas.utils.parser import parse_markdown
import frontmatter

def test_parse_markdown():
    content = """---
id: CLAIM-001
title: Test Claim
---

# Test Claim
"""
    with open("test.md", "w") as f:
        f.write(content)
    
    parsed = parse_markdown("test.md")
    assert parsed["id"] == "CLAIM-001"
    assert parsed["title"] == "Test Claim"