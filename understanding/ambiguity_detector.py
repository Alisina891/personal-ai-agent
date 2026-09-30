from understanding.ambiguity import AmbiguityLevel
from understanding.entity import EntityType
from understanding.entity_value import Entity


class AmbiguityDetector:

    def detect(self, entity: Entity | None) -> AmbiguityLevel:
        if entity is None:
            return AmbiguityLevel.AMBIGUOUS

        if entity.type == EntityType.FILE:
            ambiguous_values = {
                "that pdf",
                "the pdf",
                "that file",
                "the file",
                "this pdf",
                "this file",
            }

            if entity.value.lower() in ambiguous_values:
                return AmbiguityLevel.AMBIGUOUS

        return AmbiguityLevel.CLEAR