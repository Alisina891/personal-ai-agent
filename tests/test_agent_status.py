from identity.agent_status import AgentStatus


def test_agent_status_values():
    assert AgentStatus.ACTIVE.value == "ACTIVE"
    assert AgentStatus.DISABLED.value == "DISABLED"
    assert AgentStatus.LOCKED.value == "LOCKED"