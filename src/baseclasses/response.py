from typing import Union

import requests

from src.enums.global_enums import *


class Response:
    def __init__(self, response: Union[requests.models.Response]):
        self.response = response

    def assert_status_code(self, status_code: Union[int, list]):
        if isinstance(status_code, int):
            assert self.response.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        elif isinstance(status_code, list):
            assert self.response.status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            raise TypeError("Unsupported type")

        return self

    def json_validate(self, schema):
        response_json = self.response.json()

        assert schema.model_validate(response_json) is not None

        return self
