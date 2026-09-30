import pytest
import requests
from errors.exceptions import AIError


from ai.local_provider import LocalAIProvider


def test_local_provider_name():
    provider = LocalAIProvider()

    assert provider.provider_name == "ollama"


def test_local_provider_configuration():
    provider = LocalAIProvider(
        model="qwen3:4b",
        base_url="http://127.0.0.1:11434",
    )

    assert provider.model == "qwen3:4b"
    assert provider.base_url == "http://127.0.0.1:11434"


@pytest.mark.integration
def test_local_provider_generates_response():
    provider = LocalAIProvider()

    result = provider.generate(
        "Say hello in one short sentence."
    )

    assert isinstance(result, str)
    assert result.strip() != ""



def test_local_provider_handles_connection_failure(monkeypatch):
    provider = LocalAIProvider()

    def failed_request(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Connection refused")

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        failed_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_handles_timeout(monkeypatch):
    provider = LocalAIProvider()

    def timed_out_request(*args, **kwargs):
        raise requests.exceptions.Timeout("Request timed out")

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        timed_out_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_handles_http_error(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            raise requests.exceptions.HTTPError("Server error")

    def failed_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        failed_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_handles_missing_response(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {}

    def failed_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        failed_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_rejects_empty_response(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": ""}

    def fake_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        fake_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_rejects_whitespace_response(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "   "}

    def fake_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        fake_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_rejects_non_string_response(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": 123}

    def fake_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        fake_request,
    )

    with pytest.raises(AIError):
        provider.generate("Hello")


def test_local_provider_accepts_valid_response(monkeypatch):
    provider = LocalAIProvider()

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "Hello, I am your local AI."}

    def fake_request(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai.local_provider.requests.post",
        fake_request,
    )

    result = provider.generate("Hello")

    assert result == "Hello, I am your local AI."