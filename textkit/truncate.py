def truncate(text: str, limit: int) -> str:
    """limit 글자를 넘으면 자르고 말줄임표를 붙인다."""
    if len(text) > limit:
        return text[:limit] + "..."
    return text
