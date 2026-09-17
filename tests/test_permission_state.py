from security.permission_state import PermissionState


def test_permission_states_exist():
    assert PermissionState.ALLOW.value == "ALLOW"
    assert PermissionState.ASK.value == "ASK"
    assert PermissionState.DENY.value == "DENY"