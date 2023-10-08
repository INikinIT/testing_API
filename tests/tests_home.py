from http import HTTPStatus
from api.questions import api


def test_new_user():
    email = "eve.holt@reqres.in"
    password = "12345"
    res = api.create_user(email, password)

    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res.json())


def test_new_user_error():
    email = "eve.holt@reqres.in"
    res = api.create_user_error(email)
    res_body = res.json()

    assert res.status_code == HTTPStatus.BAD_REQUEST
    # Assert.validate_schema(res_body())
    assert res_body
    example = {
            "error": "Missing password"
         }
    assert example == res_body
