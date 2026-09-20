# Security Attack Tests

## Purpose

Day 29 tests the security system by simulating attempts to bypass important security controls.

The goal is to find weaknesses before the Agent is connected to real computer-control tools.

## Attack Scenarios

### 1. Permission Bypass

The test attempts to continue an action when the permission state is DENY.

Expected behavior:

```text
DENY
→ ActionGuard
→ False
→ Action blocked