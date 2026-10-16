def word_count(text: str) -> int:
    """공백으로 나눈 단어 수. 빈 문자열은 0."""
    if not text.strip():
        return 0
    return len(text.split())


def char_count(text: str, *, spaces: bool = True) -> int:
    """글자 수. spaces=False면 공백을 뺀다."""
    if spaces:
        return len(text)
    return len("".join(text.split()))
