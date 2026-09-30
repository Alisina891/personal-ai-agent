from enum import Enum


class EntityType(Enum):
    FILE = "file"
    DATE = "date"
    PERSON = "person"
    PROJECT = "project"
    LOCATION = "location"