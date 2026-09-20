from security.prompt_injection_guard import PromptInjectionGuard


def test_website_is_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("website") is True


def test_pdf_is_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("pdf") is True


def test_file_is_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("file") is True


def test_email_is_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("email") is True


def test_api_is_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("api") is True


def test_user_is_not_external_data():
    guard = PromptInjectionGuard()

    assert guard.is_external_data("user") is False