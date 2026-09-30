from enum import Enum


class Intent(Enum):
    QUESTION = "question"
    TASK = "task"
    FILE = "file"
    MEMORY = "memory"
    SEARCH = "search"
    ACTION = "action"