
# Bunifu Django Auth

A standardized authentication framework for Django projects built on:

- Django
- Django Allauth
- Django REST Framework
- SimpleJWT

Designed for internal organizational consistency and centralized user model management.

---

## Features

- Email-based authentication
- JWT access & refresh tokens
- Token rotation & blacklisting
- DRF-ready endpoints
- Automatic safe default configuration
- Pluggable and override-friendly
- Production-ready test suite (pytest + factoryboy)

---

## Installation

### TestPypi Repository

```bash
uv pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple  bunifu-django-auth       
```

---

## Quick Start

### 1️⃣ Add to Installed Apps

```python
INSTALLED_APPS = [
    "allauth",
    "allauth.account",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "bunifu_django_auth",
]
```

### 2️⃣ Include URLs

```python
from django.urls import path, include

urlpatterns = [
    path("auth/", include("bunifu_django_auth.urls")),
]

```

### Migrate the tables

```python
python manage.py makemigrations bunifu_django_auth
python manage.py makemigrations account
python manage.py migrate
```

### Include the JWTAuthorization

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}
```

That’s it.

No additional configuration required.

---

## Available Endpoints

| Endpoint          | Method | Description                        |
| ----------------- | ------ | ---------------------------------- |
| `/auth/register/` | POST   | Register new user                  |
| `/auth/login/`    | POST   | Obtain JWT access & refresh tokens |
| `/auth/refresh/`  | POST   | Refresh access token               |
| `/auth/logout/`   | POST   | Blacklist refresh token            |

---

## Default Configuration

The package automatically applies safe defaults:

* Email authentication
* JWT token rotation
* 15-minute access tokens
* 7-day refresh tokens
* Refresh token blacklisting
* DRF JWT authentication backend

All settings can be overridden in the host project.

Example:

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
}
```

---

## Overriding Serializers

You may override serializers if needed:

```python
BUNIFU_REGISTER_SERIALIZER = "yourapp.serializers.CustomRegisterSerializer"
```

---

## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=bunifu_django_auth
```

---

## License

MIT License © 2026 Bunifu
