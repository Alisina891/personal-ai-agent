from security.permission_matrix import PermissionRule
from security.permission_state import PermissionState
from security.risk_level import RiskLevel


def test_permission_rule():
    rule = PermissionRule(
        action="read_private_file",
        permission=PermissionState.ASK,
        risk=RiskLevel.MEDIUM,
        confirmation_required=True,
        verification_required=True,
    )

    assert rule.action == "read_private_file"
    assert rule.permission == PermissionState.ASK
    assert rule.risk == RiskLevel.MEDIUM
    assert rule.confirmation_required is True
    assert rule.verification_required is True