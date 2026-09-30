from understanding.uncertainty import UncertaintyLevel
from understanding.uncertainty_detector import UncertaintyDetector


def test_detects_confident():
    detector = UncertaintyDetector()

    result = detector.detect(
        intent="FILE_READ",
        entity="README.md",
    )

    assert result == UncertaintyLevel.CONFIDENT


def test_detects_uncertain_when_intent_missing():
    detector = UncertaintyDetector()

    result = detector.detect(
        intent=None,
        entity="README.md",
    )

    assert result == UncertaintyLevel.UNCERTAIN


def test_detects_uncertain_when_entity_missing():
    detector = UncertaintyDetector()

    result = detector.detect(
        intent="FILE_READ",
        entity=None,
    )

    assert result == UncertaintyLevel.UNCERTAIN


def test_detects_unknown():
    detector = UncertaintyDetector()

    result = detector.detect(
        intent=None,
        entity=None,
    )

    assert result == UncertaintyLevel.UNKNOWN