class PromptInjectionGuard:

    def is_external_data(self, source: str) -> bool:
        external_sources = {
            "website",
            "pdf",
            "file",
            "email",
            "api",
        }

        return source.lower() in external_sources