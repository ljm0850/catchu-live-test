import re


def slugify(text: str) -> str:
    """글자·숫자를 남기고 나머지는 하이픈으로 바꾼다(유니코드 허용)."""
    lowered = text.strip().lower()
    replaced = re.sub(r"[^\w]+", "-", lowered)
    return replaced.strip("-_")
