from enum import Enum


class DataClassification(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    SENSITIVE = "SENSITIVE"
    LOCAL_ONLY = "LOCAL_ONLY"