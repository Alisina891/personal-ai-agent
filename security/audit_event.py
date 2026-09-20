from enum import Enum


class AuditEvent(Enum):
    REQUESTED = "requested"
    ALLOWED = "allowed"
    DENIED = "denied"
    ATTEMPTED = "attempted"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    UNVERIFIED = "unverified"