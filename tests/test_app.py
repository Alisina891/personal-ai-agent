from app import start_application




def test_application_startup():
    result = start_application()

    assert result is True