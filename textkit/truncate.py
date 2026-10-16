def truncate(text: str, limit: int, suffix: str = "...") -> str:
    """말줄임표를 포함해 limit 글자를 넘지 않게 자른다."""
    if limit < len(suffix):
        raise ValueError("limit이 말줄임표보다 짧다")
    if len(text) <= limit:
        return text
    return text[: limit - len(suffix)] + suffix
