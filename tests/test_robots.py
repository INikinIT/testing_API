import re
from api.http_bin_api import http_bin_api
from http import HTTPStatus


def test_robots():
    res = http_bin_api.robots_txt()

    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r".*User-agent: \*.*Disallow: /deny.*", res.text, flags=re.DOTALL)
