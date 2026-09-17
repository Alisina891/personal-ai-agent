from dataclasses import dataclass

from security.permission_state import PermissionState
from security.risk_level import RiskLevel


@dataclass(frozen=True)
class PermissionRule:
    action: str
    permission: PermissionState
    risk: RiskLevel
    confirmation_required: bool
    verification_required: bool