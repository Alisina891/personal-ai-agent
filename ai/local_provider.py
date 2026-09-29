from ai.provider import AIProvider
import requests


class LocalAIProvider(AIProvider):

    def __init__(
        self,
        model: str = "qwen3:4b",
        base_url: str = "http://127.0.0.1:11434",
    ):
        self.model = model
        self.base_url = base_url

    @property
    def provider_name(self) -> str:
        return "ollama"

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=240,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]