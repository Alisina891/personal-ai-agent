from enum import Enum


class UncertaintyLevel(Enum):
    CONFIDENT = "confident"
    UNCERTAIN = "uncertain"
    UNKNOWN = "unknown"