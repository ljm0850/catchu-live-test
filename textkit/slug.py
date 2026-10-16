import re


def slugify(text: str) -> str:
    """영문·숫자만 남기고 나머지는 하이픈으로 바꾼다."""
    lowered = text.strip().lower()
    replaced = re.sub(r"[^a-z0-9]+", "-", lowered)
    return replaced.strip("-")
