from identity.agent_identity import AgentIdentity
from identity.tool_authorization import ToolAuthorization


def test_allowed_tool_is_authorized():
    agent = AgentIdentity(
        assistant_id="personal-agent-001",
        allowed_tools={"file_read"},
    )

    authorization = ToolAuthorization()

    assert authorization.is_allowed(agent, "file_read") is True


def test_denied_tool_is_not_authorized():
    agent = AgentIdentity(
        assistant_id="personal-agent-001",
        denied_tools={"system_command"},
    )

    authorization = ToolAuthorization()

    assert authorization.is_allowed(agent, "system_command") is False


def test_unknown_tool_is_not_authorized():
    agent = AgentIdentity(
        assistant_id="personal-agent-001",
        allowed_tools={"file_read"},
    )

    authorization = ToolAuthorization()

    assert authorization.is_allowed(agent, "camera") is False