from understanding.structured_request import StructuredRequest


def test_structured_request_stores_intent_and_entity():
    request = StructuredRequest(
        intent="FILE_READ",
        entity="README.md",
    )

    assert request.intent == "FILE_READ"
    assert request.entity == "README.md"


def test_structured_request_allows_missing_values():
    request = StructuredRequest(
        intent=None,
        entity=None,
    )

    assert request.intent is None
    assert request.entity is None