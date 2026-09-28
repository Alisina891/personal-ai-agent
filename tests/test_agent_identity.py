import pytest

from identity.agent_identity import AgentIdentity
from identity.agent_status import AgentStatus


def test_agent_identity_defaults():
    agent = AgentIdentity(
        assistant_id="personal-agent-001"
    )

    assert agent.assistant_id == "personal-agent-001"
    assert agent.status == AgentStatus.ACTIVE
    assert agent.allowed_tools == set()
    assert agent.denied_tools == set()


def test_agent_identity_with_tools():
    agent = AgentIdentity(
        assistant_id="personal-agent-001",
        allowed_tools={"file_read", "web_search"},
        denied_tools={"system_command"},
    )

    assert "file_read" in agent.allowed_tools
    assert "web_search" in agent.allowed_tools
    assert "system_command" in agent.denied_tools


def test_tool_cannot_be_allowed_and_denied():
    with pytest.raises(ValueError):
        AgentIdentity(
            assistant_id="personal-agent-001",
            allowed_tools={"file_read"},
            denied_tools={"file_read"},
        )