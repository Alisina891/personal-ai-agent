from dataclasses import dataclass

from understanding.entity import EntityType


@dataclass
class Entity:
    type: EntityType
    value: str