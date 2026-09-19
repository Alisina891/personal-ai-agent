from enum import Enum


class ActionType(Enum):
    FILE_READ = "file_read"
    FILE_WRITE = "file_write"
    FILE_DELETE = "file_delete"
    WEB_READ = "web_read"
    WEB_SEARCH = "web_search"
    UNKNOWN = "unknown"