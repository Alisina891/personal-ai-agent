import pytest

from errors.exceptions import (
    AgentError,
    ValidationError,
    SecurityError,
    ToolError,
    DatabaseError,
    AIError,
    NetworkError,
)


def test_error_hierarchy():
    errors = [
        ValidationError,
        SecurityError,
        ToolError,
        DatabaseError,
        AIError,
        NetworkError,
    ]

    for error_type in errors:
        assert issubclass(error_type, AgentError)
        assert issubclass(error_type, Exception)


def test_errors_can_be_raised():
    with pytest.raises(ValidationError):
        raise ValidationError("Invalid input")

    with pytest.raises(SecurityError):
        raise SecurityError("Security rule blocked the action")

    with pytest.raises(ToolError):
        raise ToolError("Tool failed")

    with pytest.raises(DatabaseError):
        raise DatabaseError("Database failed")

    with pytest.raises(AIError):
        raise AIError("AI provider failed")

    with pytest.raises(NetworkError):
        raise NetworkError("Network request failed")