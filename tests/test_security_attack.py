from security.action_guard import ActionGuard
from security.confirmation_manager import ConfirmationManager
from security.permission_state import PermissionState


def test_fake_approval_does_not_pass_when_confirmation_is_false():
    confirmation_manager = ConfirmationManager()
    guard = ActionGuard()

    confirmed = confirmation_manager.confirm(False)

    assert confirmed is False

    result = guard.can_execute(PermissionState.ASK)

    assert result is False