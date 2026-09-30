from understanding.structured_request import StructuredRequest


class Understanding:

    def understand(self, user_request: str) -> StructuredRequest:
        text = user_request.strip()

        if not text:
            return StructuredRequest(
                intent=None,
                entity=None,
            )

        words = text.split(maxsplit=1)

        intent = words[0].upper()

        entity = words[1] if len(words) > 1 else None

        return StructuredRequest(
            intent=intent,
            entity=entity,
        )