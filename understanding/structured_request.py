from dataclasses import dataclass

from understanding.entity_value import Entity
from understanding.intent import Intent


@dataclass
class StructuredRequest:
    intent: Intent | None
    entity: Entity | None