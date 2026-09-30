from understanding.clarification import ClarificationDecision
from understanding.uncertainty import UncertaintyLevel


def test_confident_does_not_require_clarification():
    decision = ClarificationDecision()

    assert decision.should_clarify(
        UncertaintyLevel.CONFIDENT
    ) is False


def test_uncertain_requires_clarification():
    decision = ClarificationDecision()

    assert decision.should_clarify(
        UncertaintyLevel.UNCERTAIN
    ) is True


def test_unknown_requires_clarification():
    decision = ClarificationDecision()

    assert decision.should_clarify(
        UncertaintyLevel.UNKNOWN
    ) is True