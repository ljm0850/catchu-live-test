from textkit.slug import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_trims_symbols():
    assert slugify("  --Catch U!  ") == "catch-u"
