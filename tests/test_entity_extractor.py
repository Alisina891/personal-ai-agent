from understanding.entity import EntityType
from understanding.entity_extractor import EntityExtractor


def test_extracts_markdown_file():
    extractor = EntityExtractor()

    result = extractor.extract(
        "Read README.md"
    )

    assert result is not None
    assert result.type == EntityType.FILE
    assert result.value == "README.md"


def test_extracts_python_file():
    extractor = EntityExtractor()

    result = extractor.extract(
        "Open main.py"
    )

    assert result is not None
    assert result.type == EntityType.FILE
    assert result.value == "main.py"


def test_returns_none_for_unknown_entity():
    extractor = EntityExtractor()

    result = extractor.extract(
        "Hello there"
    )

    assert result is None


def test_returns_none_for_empty_text():
    extractor = EntityExtractor()

    result = extractor.extract("")

    assert result is None