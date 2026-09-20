class PromptInjectionGuard:

    EXTERNAL_SOURCES = {
        "website",
        "pdf",
        "file",
        "email",
        "api",
    }

    INJECTION_PATTERNS = {
        "ignore previous instructions",
        "ignore all previous instructions",
        "disable security",
        "change permission",
        "bypass security",
        "execute this command",
    }

    def is_external_data(self, source: str) -> bool:
        return source.lower() in self.EXTERNAL_SOURCES

    def contains_injection_attempt(self, content: str) -> bool:
        content = content.lower()

        return any(
            pattern in content
            for pattern in self.INJECTION_PATTERNS
        )