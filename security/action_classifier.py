from security.action_type import ActionType


class ActionClassifier:

    def classify(self, action: str) -> ActionType:
        action = action.lower()

        if "delete" in action:
            return ActionType.FILE_DELETE

        if "write" in action or "create" in action:
            return ActionType.FILE_WRITE

        if "read" in action:
            return ActionType.FILE_READ

        if "search" in action:
            return ActionType.WEB_SEARCH

        if "web" in action:
            return ActionType.WEB_READ

        raise ValueError("Unknown action")