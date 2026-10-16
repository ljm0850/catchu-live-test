import sys

from textkit.slug import slugify


def main() -> int:
    for line in sys.stdin:
        print(slugify(line))
    return 0
