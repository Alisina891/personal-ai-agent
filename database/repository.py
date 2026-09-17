from database.database import get_connection


class SettingsRepository:

    def save(self, key: str, value: str):
        connection = get_connection()

        connection.execute(
            """
            INSERT INTO settings (key, value)
            VALUES (?, ?)
            ON CONFLICT(key)
            DO UPDATE SET value = excluded.value
            """,
            (key, value),
        )

        connection.commit()
        connection.close()

    def get(self, key: str):
        connection = get_connection()

        cursor = connection.execute(
            "SELECT value FROM settings WHERE key = ?",
            (key,),
        )

        result = cursor.fetchone()

        connection.close()

        if result is None:
            return None

        return result[0]