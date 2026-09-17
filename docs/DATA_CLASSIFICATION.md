# Data Classification

The Personal AI Agent classifies data before deciding how the data may be used.

## Classifications

### PUBLIC

Data that is safe to share publicly.

Examples:
- Public documentation
- Public project information

### PRIVATE

Personal data that should not normally be shared without permission.

Examples:
- Personal notes
- Private documents
- Personal preferences

### SENSITIVE

Data that requires strong protection.

Examples:
- Passwords
- API keys
- Authentication tokens
- Credentials

### LOCAL_ONLY

Data that should remain on the user's local device unless the user explicitly allows otherwise.

Examples:
- Private photos
- Certain personal files
- Local recordings

## Important Difference

SENSITIVE and LOCAL_ONLY are different concepts.

SENSITIVE means the data requires strong protection.

LOCAL_ONLY means the data should remain on the local device.

## Purpose

Data classification is the foundation for the future permission and security policy system.

The classification itself does not decide whether an action is allowed.

Future security components will use the classification to make permission decisions.