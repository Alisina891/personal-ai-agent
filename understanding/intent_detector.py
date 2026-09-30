from understanding.intent import Intent


class IntentDetector:

    def detect(self, text: str) -> Intent | None:
        normalized = text.strip().lower()

        if not normalized:
            return None

        if normalized.startswith(
            ("remember ", "recall ", "what did we discuss ")
        ):
            return Intent.MEMORY

        if normalized.startswith(
            ("what ", "why ", "how ", "when ", "where ", "who ")
        ):
            return Intent.QUESTION

        if normalized.startswith(
            ("read ", "open ", "show ", "file ")
        ):
            return Intent.FILE

        if normalized.startswith(
            ("search ", "find ", "look up ", "google ")
        ):
            return Intent.SEARCH

        if normalized.startswith(
            ("create ", "make ", "build ", "write ", "plan ")
        ):
            return Intent.TASK

        if normalized.startswith(
            ("delete ", "send ", "run ", "execute ", "shutdown ")
        ):
            return Intent.ACTION

        return None