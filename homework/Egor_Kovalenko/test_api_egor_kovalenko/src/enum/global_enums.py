from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'
    WRONG_NAME = 'Name from response is not equal to expected'
