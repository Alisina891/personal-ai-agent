from identity.agent_identity import AgentIdentity


class ToolAuthorization:

    def is_allowed(self, agent: AgentIdentity, tool_name: str) -> bool:
        if tool_name in agent.denied_tools:
            return False

        if tool_name in agent.allowed_tools:
            return True

        return False