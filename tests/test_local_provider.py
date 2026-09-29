import pytest

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