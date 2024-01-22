from enum import Enum


class Config(Enum):
    SERVICE_URL = "https://eos.greymass.com"


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equals to expected."
    WRONG_ELEMENTS_COUNT = "Received amount of elements is not equal to expected."
