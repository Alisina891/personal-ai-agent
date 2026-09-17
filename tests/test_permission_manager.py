from security.permission_manager import PermissionManager
from security.permission_matrix import PermissionRule
from security.permission_state import PermissionState
from security.risk_level import RiskLevel


def test_permission_manager_returns_permission():
    rule = PermissionRule(
        action="read_private_file",
        permission=PermissionState.ASK,
        risk=RiskLevel.MEDIUM,
        confirmation_required=True,
        verification_required=True,
    )

    manager = PermissionManager()

    result = manager.evaluate(rule)

    assert result == PermissionState.ASK