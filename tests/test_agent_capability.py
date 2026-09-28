from identity.agent_capability import AgentCapability


def test_agent_capability_values():
    assert AgentCapability.FILE_READ.value == "file_read"
    assert AgentCapability.WEB_SEARCH.value == "web_search"
    assert AgentCapability.VOICE_INPUT.value == "voice_input"
    assert AgentCapability.IMAGE_ANALYSIS.value == "image_analysis"
    assert AgentCapability.SYSTEM_COMMAND.value == "system_command"
    assert AgentCapability.EMAIL_SEND.value == "email_send"