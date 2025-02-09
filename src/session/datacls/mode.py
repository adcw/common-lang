from enum import Enum

class MODE(Enum):
    PREPARE_DATA = "prepare data"
    TRAIN = "train"
    EXIT = "exit"

    @classmethod
    def from_value(cls: Enum, value: str) -> 'MODE':
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f"Value '{value}' not found in Enum {cls.__name__}")
