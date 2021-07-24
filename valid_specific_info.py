from enum import Enum


class SpecificInfo(Enum):
    OPEN = 'Open'
    CLOSE = 'Close'
    LOW = 'Low'
    HIGH = 'High'
    ADJ_CLOSE = 'Adj Close'
    VOLUME = 'Volume'


def valid_specific_info(specific_info: str) -> bool:
    if specific_info.upper() in [x.name for x in SpecificInfo]:
        return True
    else:
        return False
