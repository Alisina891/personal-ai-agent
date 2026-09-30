from understanding.intent import Intent
from understanding.intent_detector import IntentDetector


def test_detects_question():
    detector = IntentDetector()

    assert detector.detect(
        "What is Python?"
    ) == Intent.QUESTION


def test_detects_file():
    detector = IntentDetector()

    assert detector.detect(
        "Read README.md"
    ) == Intent.FILE


def test_detects_memory():
    detector = IntentDetector()

    assert detector.detect(
        "What did we discuss about Day 30?"
    ) == Intent.MEMORY


def test_detects_search():
    detector = IntentDetector()

    assert detector.detect(
        "Search Python documentation"
    ) == Intent.SEARCH


def test_detects_task():
    detector = IntentDetector()

    assert detector.detect(
        "Create a new project"
    ) == Intent.TASK


def test_detects_action():
    detector = IntentDetector()

    assert detector.detect(
        "Run the tests"
    ) == Intent.ACTION


def test_unknown_request_returns_none():
    detector = IntentDetector()

    assert detector.detect(
        "banana spaceship"
    ) is None