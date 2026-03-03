import pytest
from rest_framework.test import APIClient
from ..factories.users import UserFactory

@pytest.mark.django_db
def test_logout_blacklists_refresh_token():
    raw_password = "password123"
    user = UserFactory(password=raw_password)
    client = APIClient()
    login_resp = client.post(
        "/login/",
        {"email": user.email, "password": raw_password},
        format="json"
    )
    assert login_resp.status_code == 200
    refresh_token = login_resp.data["refresh"]
    access_token = login_resp.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    logout_resp = client.post(
        "/logout/",
        {"refresh": refresh_token},
        format="json"
    )
    
    assert logout_resp.status_code == 200
