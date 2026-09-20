from security.action_guard import ActionGuard
from security.permission_state import PermissionState


def test_unauthorized_tool_is_blocked():
    guard = ActionGuard()

    permission = PermissionState.DENY

    can_execute = guard.can_execute(permission)

    assert can_execute is False