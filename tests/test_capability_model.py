from identity.agent_capability import AgentCapability
from identity.capability_model import CapabilityModel


def test_available_capability():
    model = CapabilityModel(
        available={
            AgentCapability.FILE_READ,
            AgentCapability.WEB_SEARCH,
        }
    )

    assert model.can(AgentCapability.FILE_READ) is True


def test_unavailable_capability():
    model = CapabilityModel(
        available={
            AgentCapability.FILE_READ,
        }
    )

    assert model.can(AgentCapability.EMAIL_SEND) is False


def test_cannot_returns_true_for_unavailable_capability():
    model = CapabilityModel(
        available={
            AgentCapability.FILE_READ,
        }
    )

    assert model.cannot(AgentCapability.SYSTEM_COMMAND) is True


def test_empty_model_has_no_capabilities():
    model = CapabilityModel()

    assert model.can(AgentCapability.FILE_READ) is False
    assert model.cannot(AgentCapability.FILE_READ) is True