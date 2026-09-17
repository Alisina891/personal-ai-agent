from config import settings
from database.database import get_connection


def check_configuration():
    if settings.APP_MODE:
        return "healthy"

    return "unhealthy"


def check_database():
    try:
        connection = get_connection()

        connection.execute("SELECT 1")

        connection.close()

        return "healthy"

    except Exception:
        return "unhealthy"


def check_security():
    return "not_ready"


def get_health_status():
    configuration = check_configuration()
    database = check_database()
    security = check_security()

    checks = {
        "configuration": configuration,
        "database": database,
        "security": security,
    }

    if "unhealthy" in checks.values():
        overall_status = "unhealthy"
    elif "not_ready" in checks.values():
        overall_status = "not_ready"
    else:
        overall_status = "healthy"

    return {
        "status": overall_status,
        "checks": checks,
    }