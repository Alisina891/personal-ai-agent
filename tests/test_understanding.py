from understanding.structured_request import StructuredRequest
from understanding.understanding import Understanding


def test_understanding_extracts_intent_and_entity():
    understanding = Understanding()

    result = understanding.understand(
        "read README.md"
    )

    assert result == StructuredRequest(
        intent="READ",
        entity="README.md",
    )


def test_understanding_handles_intent_without_entity():
    understanding = Understanding()

    result = understanding.understand(
        "search"
    )

    assert result == StructuredRequest(
        intent="SEARCH",
        entity=None,
    )


def test_understanding_handles_empty_request():
    understanding = Understanding()

    result = understanding.understand("")

    assert result == StructuredRequest(
        intent=None,
        entity=None,
    )