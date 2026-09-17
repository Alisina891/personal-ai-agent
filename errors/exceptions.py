class AgentError(Exception):
    """Base error for the Personal AI Agent."""


class ValidationError(AgentError):
    """Raised when user or application input is invalid."""


class SecurityError(AgentError):
    """Raised when a security rule is violated."""


class ToolError(AgentError):
    """Raised when a tool cannot complete its operation."""


class DatabaseError(AgentError):
    """Raised when a database operation fails."""


class AIError(AgentError):
    """Raised when an AI provider or AI operation fails."""


class NetworkError(AgentError):
    """Raised when a network operation fails."""