from backend.health import get_health_status


def test_health_status():
    result = get_health_status()

    assert "status" in result
    assert "checks" in result

    assert result["checks"]["configuration"] == "healthy"
    assert result["checks"]["database"] == "healthy"
    assert result["checks"]["security"] == "not_ready"