from enum import Enum

"""
класс Enum c описанием ошибки для использования в assert.
"""


class GlobalErrors(Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected'
