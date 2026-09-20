from security.security_boundary import SecurityBoundary


def test_file_delete_is_forbidden():
    boundary = SecurityBoundary()

    result = boundary.is_direct_access_forbidden("file_delete")

    assert result is True


def test_system_command_is_forbidden():
    boundary = SecurityBoundary()

    result = boundary.is_direct_access_forbidden("system_command")

    assert result is True


def test_disable_security_is_forbidden():
    boundary = SecurityBoundary()

    result = boundary.is_direct_access_forbidden("disable_security")

    assert result is True


def test_normal_action_is_not_forbidden():
    boundary = SecurityBoundary()

    result = boundary.is_direct_access_forbidden("normal_read")

    assert result is False