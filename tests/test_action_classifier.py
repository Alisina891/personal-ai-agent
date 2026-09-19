import pytest

from security.action_classifier import ActionClassifier
from security.action_type import ActionType


def test_unknown_action():
    classifier = ActionClassifier()

    with pytest.raises(ValueError):
        classifier.classify("Do something unknown")

def test_classify_file_delete():
    classifier = ActionClassifier()

    result = classifier.classify("Delete this file")

    assert result == ActionType.FILE_DELETE


def test_classify_file_read():
    classifier = ActionClassifier()

    result = classifier.classify("Read this file")

    assert result == ActionType.FILE_READ


def test_classify_file_write():
    classifier = ActionClassifier()

    result = classifier.classify("Write this file")

    assert result == ActionType.FILE_WRITE


def test_classify_web_search():
    classifier = ActionClassifier()

    result = classifier.classify("Search the web")

    assert result == ActionType.WEB_SEARCH


def test_classify_web_read():
    classifier = ActionClassifier()

    result = classifier.classify("Read this web page")

    assert result == ActionType.FILE_READ