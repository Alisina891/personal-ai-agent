from dataclasses import dataclass, field

from identity.agent_status import AgentStatus


@dataclass
class AgentIdentity:
    assistant_id: str
    status: AgentStatus = AgentStatus.ACTIVE
    allowed_tools: set[str] = field(default_factory=set)
    denied_tools: set[str] = field(default_factory=set)

    def __post_init__(self):
        overlap = self.allowed_tools & self.denied_tools

        if overlap:
            raise ValueError(
                f"Tool cannot be both allowed and denied: {overlap}"
            )