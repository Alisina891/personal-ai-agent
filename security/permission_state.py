from enum import Enum


class PermissionState(str, Enum):
    ALLOW = "ALLOW"
    ASK = "ASK"
    DENY = "DENY"