from security.data_classification import DataClassification


def test_data_classifications_exist():
    assert DataClassification.PUBLIC.value == "PUBLIC"
    assert DataClassification.PRIVATE.value == "PRIVATE"
    assert DataClassification.SENSITIVE.value == "SENSITIVE"
    assert DataClassification.LOCAL_ONLY.value == "LOCAL_ONLY"