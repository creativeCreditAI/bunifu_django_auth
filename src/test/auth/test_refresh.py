import pytest
from rest_framework.test import APIClient
from ..factories.users import UserFactory

@pytest.mark.django_db
def test_token_refresh():
    raw_password = "password123"
    user = UserFactory(password=raw_password)
    client = APIClient()
    login_resp = client.post(
        "/login/",
        {"email": user.email, "password": raw_password},
        format="json"
    )

    assert login_resp.status_code == 200
    assert "refresh" in login_resp.data
    assert "access" in login_resp.data

    refresh_token = login_resp.data["refresh"]

    refresh_resp = client.post(
        "/refresh/",
        {"refresh": refresh_token},
        format="json"
    )

    assert refresh_resp.status_code == 200
    assert "access" in refresh_resp.data
    assert refresh_resp.data["access"] != login_resp.data["access"]


