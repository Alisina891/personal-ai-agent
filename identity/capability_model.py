from identity.agent_capability import AgentCapability


class CapabilityModel:

    def __init__(
        self,
        available: set[AgentCapability] | None = None,
    ):
        self.available = available or set()

    def can(self, capability: AgentCapability) -> bool:
        return capability in self.available

    def cannot(self, capability: AgentCapability) -> bool:
        return capability not in self.available