from database.database import initialize_database
from database.repository import SettingsRepository


def test_settings_table_exists():
    initialize_database()

    repository = SettingsRepository()

    result = repository.get("test_setting")

    assert result is None


def test_settings_repository():
    initialize_database()

    repository = SettingsRepository()

    repository.save("ai_provider", "local")

    result = repository.get("ai_provider")

    assert result == "local"