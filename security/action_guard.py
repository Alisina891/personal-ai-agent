from security.permission_state import PermissionState


class ActionGuard:

    def can_execute(self, permission: PermissionState) -> bool:
        return permission == PermissionState.ALLOW