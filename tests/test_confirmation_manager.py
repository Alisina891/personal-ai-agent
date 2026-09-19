from security.confirmation_manager import ConfirmationManager


def test_confirmation_is_accepted():
    manager = ConfirmationManager()

    result = manager.confirm(True)

    assert result is True


def test_confirmation_is_rejected():
    manager = ConfirmationManager()

    result = manager.confirm(False)

    assert result is False