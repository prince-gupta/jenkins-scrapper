from enum import Enum


class Status(Enum):

    SUCCESS = 1
    FAILED = 2

    def is_success(self, status):
        return