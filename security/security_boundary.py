class SecurityBoundary:

    FORBIDDEN_DIRECT_ACTIONS = {
        "file_delete",
        "file_write",
        "system_command",
        "change_permission",
        "disable_security",
        "access_sensitive_data",
    }

    def is_direct_access_forbidden(self, action: str) -> bool:
        return action in self.FORBIDDEN_DIRECT_ACTIONS