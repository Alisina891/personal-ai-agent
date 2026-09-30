from understanding.entity import EntityType
from understanding.entity_value import Entity


class EntityExtractor:

    def extract(self, text: str) -> Entity | None:
        normalized = text.strip()

        if not normalized:
            return None

        words = normalized.split()

        for word in words:
            if word.endswith(
                (".txt", ".md", ".py", ".json", ".csv", ".pdf", ".docx", ".xlsx")
            ):
                return Entity(
                    type=EntityType.FILE,
                    value=word,
                )

        return None