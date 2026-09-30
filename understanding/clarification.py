from understanding.uncertainty import UncertaintyLevel


class ClarificationDecision:

    def should_clarify(self, uncertainty: UncertaintyLevel) -> bool:
        return uncertainty in {
            UncertaintyLevel.UNCERTAIN,
            UncertaintyLevel.UNKNOWN,
        }