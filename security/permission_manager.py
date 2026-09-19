from security.permission_matrix import PermissionRule
from security.permission_state import PermissionState
from security.action_type import ActionType


class PermissionManager:

    def evaluate(self, rule: PermissionRule) -> PermissionState:

        if rule.action == ActionType.UNKNOWN.value:
            return PermissionState.DENY

        return rule.permission