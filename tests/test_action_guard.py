from security.action_guard import ActionGuard
from security.permission_state import PermissionState


def test_allow_can_execute():
    guard = ActionGuard()

    result = guard.can_execute(PermissionState.ALLOW)

    assert result is True


def test_ask_cannot_execute():
    guard = ActionGuard()

    result = guard.can_execute(PermissionState.ASK)

    assert result is False


def test_deny_cannot_execute():
    guard = ActionGuard()

    result = guard.can_execute(PermissionState.DENY)

    assert result is False

def test_denied_action_cannot_bypass_guard():
    guard = ActionGuard()

    permission = PermissionState.DENY

    result = guard.can_execute(permission)

    assert result is False