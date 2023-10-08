import re
from api.http_bin_api import http_bin_api
from http import HTTPStatus
from utils.assertions import Assert


def test_ip():
    res = http_bin_api.get_ip()

    assert res.status_code == HTTPStatus.OK
    if res.headers['Content-Type'] == 'application/json':
        # Assert.validate_schema(res.json())

        origin = res.json()['origin']
        assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', origin)
