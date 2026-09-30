from understanding.uncertainty import UncertaintyLevel


def test_uncertainty_levels_exist():
    assert UncertaintyLevel.CONFIDENT.value == "confident"
    assert UncertaintyLevel.UNCERTAIN.value == "uncertain"
    assert UncertaintyLevel.UNKNOWN.value == "unknown"