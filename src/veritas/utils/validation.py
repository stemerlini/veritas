def validate_claim(claim):
    """Validate a claim's structure."""
    required_fields = ["id", "title", "supports", "disproofs"]
    for field in required_fields:
        if field not in claim:
            raise ValueError(f"Claim is missing required field: {field}")