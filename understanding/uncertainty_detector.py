from understanding.uncertainty import UncertaintyLevel


class UncertaintyDetector:

    def detect(
        self,
        intent: str | None,
        entity: str | None,
    ) -> UncertaintyLevel:

        if not intent and not entity:
            return UncertaintyLevel.UNKNOWN

        if not intent or not entity:
            return UncertaintyLevel.UNCERTAIN

        return UncertaintyLevel.CONFIDENT