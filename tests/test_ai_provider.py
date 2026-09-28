import pytest

from ai.provider import AIProvider


def test_ai_provider_is_abstract():
    with pytest.raises(TypeError):
        AIProvider()


class FakeProvider(AIProvider):

    @property
    def provider_name(self) -> str:
        return "fake"

    def generate(self, prompt: str) -> str:
        return f"Response: {prompt}"


def test_fake_provider_implements_interface():
    provider = FakeProvider()

    assert provider.provider_name == "fake"
    assert provider.generate("Hello") == "Response: Hello"