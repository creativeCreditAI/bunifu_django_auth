import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_user_account_creation():
    client = APIClient()
    response = client.post(
        "/register/",
        {"email": "jeckonia@gmail.com", "password": "macy3663"},
        format="json",
    )

    assert response.status_code == 201
    from bunifu_django_auth.models.users import BunifuUser
    assert BunifuUser.objects.filter(email="jeckonia@gmail.com").exists()

