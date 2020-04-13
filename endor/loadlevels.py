from enum import Enum


class LoadLevel(Enum):
    LOW = 'green'
    MEDIUM = 'yellow'
    HIGH = 'orange'
    CRITICAL = 'red'


def get_load_level(percent):
    if 0 <= percent < 25:
        return LoadLevel.LOW
    elif 25 <= percent < 50:
        return LoadLevel.MEDIUM
    elif 50 <= percent < 75:
        return LoadLevel.HIGH
    else:
        return LoadLevel.CRITICAL
