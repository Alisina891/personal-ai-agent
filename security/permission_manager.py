from security.permission_matrix import PermissionRule
from security.permission_state import PermissionState


class PermissionManager:
    def evaluate(self, rule: PermissionRule) -> PermissionState:
        return rule.permission