import requests

from src.enums.global_enums import *
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_get_request():
    r = requests.get(url=Config.SERVICE_URL.value)
    response = Response(r)

    response.assert_status_code(200).json_validate(Post)
