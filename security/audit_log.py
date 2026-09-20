from security.audit_event import AuditEvent


class AuditLog:

    def __init__(self):
        self.events = []

    def record(self, event: AuditEvent) -> None:
        self.events.append(event)

    def get_events(self) -> list[AuditEvent]:
        return self.events