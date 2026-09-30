from understanding.ambiguity import AmbiguityLevel
from understanding.ambiguity_detector import AmbiguityDetector
from understanding.entity import EntityType
from understanding.entity_value import Entity


def test_detects_ambiguous_pdf_reference():
    detector = AmbiguityDetector()

    entity = Entity(
        type=EntityType.FILE,
        value="that PDF",
    )

    result = detector.detect(entity)

    assert result == AmbiguityLevel.AMBIGUOUS


def test_detects_clear_file():
    detector = AmbiguityDetector()

    entity = Entity(
        type=EntityType.FILE,
        value="report.pdf",
    )

    result = detector.detect(entity)

    assert result == AmbiguityLevel.CLEAR


def test_none_entity_is_ambiguous():
    detector = AmbiguityDetector()

    result = detector.detect(None)

    assert result == AmbiguityLevel.AMBIGUOUS