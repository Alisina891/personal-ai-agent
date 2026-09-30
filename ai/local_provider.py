import requests

from ai.provider import AIProvider
from errors.exceptions import AIError


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
        try:
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

            result = data["response"]

            if not isinstance(result, str):
                raise AIError(
                    "Local AI provider returned a non-string response."
                )

            if not result.strip():
                raise AIError(
                    "Local AI provider returned an empty response."
                )

            return result

        except requests.exceptions.RequestException as exc:
            raise AIError(
                "Local AI provider request failed."
            ) from exc

        except (ValueError, KeyError, TypeError) as exc:
            raise AIError(
                "Local AI provider returned an invalid response."
            ) from exc