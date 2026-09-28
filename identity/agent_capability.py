from enum import Enum


class AgentCapability(str, Enum):
    FILE_READ = "file_read"
    WEB_SEARCH = "web_search"
    VOICE_INPUT = "voice_input"
    IMAGE_ANALYSIS = "image_analysis"
    SYSTEM_COMMAND = "system_command"
    EMAIL_SEND = "email_send"