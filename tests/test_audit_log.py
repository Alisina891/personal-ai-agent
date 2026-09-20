from security.audit_event import AuditEvent
from security.audit_log import AuditLog


def test_audit_log_records_event():
    log = AuditLog()

    log.record(AuditEvent.REQUESTED)

    assert log.get_events() == [AuditEvent.REQUESTED]


def test_audit_log_records_multiple_events():
    log = AuditLog()

    log.record(AuditEvent.REQUESTED)
    log.record(AuditEvent.ALLOWED)
    log.record(AuditEvent.ATTEMPTED)
    log.record(AuditEvent.SUCCEEDED)

    assert log.get_events() == [
        AuditEvent.REQUESTED,
        AuditEvent.ALLOWED,
        AuditEvent.ATTEMPTED,
        AuditEvent.SUCCEEDED,
    ]