from abc import ABC, abstractmethod


class AIProvider(ABC):

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

