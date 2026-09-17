from config import settings
from database.database import initialize_database


def start_application():
    print("Starting Personal AI Agent...")

    print(f"App mode: {settings.APP_MODE}")
    print(f"AI provider: {settings.AI_PROVIDER or 'not configured'}")
    print(f"Privacy mode: {settings.PRIVACY_MODE}")

    print("Initializing database...")
    initialize_database()

    print("Security system: not implemented yet")
    print("Identity system: not implemented yet")

    print("Personal AI Agent is ready.")

    return True


if __name__ == "__main__":
    start_application()