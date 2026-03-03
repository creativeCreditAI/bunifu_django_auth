import pytest
from rest_framework.test import APIClient
from ..factories.users import UserFactory


@pytest.mark.django_db
def test_user_account_login():
    raw_password = "password123"
    user = UserFactory(password=raw_password)
    client = APIClient()
    
    response = client.post(
        "/login/",
        {"email": user.email, "password": raw_password},
        format="json",
    )
    assert response.status_code == 200