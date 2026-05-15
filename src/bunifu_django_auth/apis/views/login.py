from ..api_docs import post_docs
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from ..serializers.login import (
    LoginSerializer,
    RefreshSerializer,
    LoginResponseSerializer,
    RefreshResponseSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Authenticate user and return JWT access/refresh tokens.
    """
    permission_classes = [permissions.AllowAny]

    @post_docs(
        summary="Login user",
        description=(
            "Authenticates a user using their credentials and returns "
            "JWT access and refresh tokens."
        ),
        tags=["Authentication"],
        operation_id="auth_login",
        request=LoginSerializer,
        responses=LoginResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Refresh JWT access token.
    """
    permission_classes = [permissions.AllowAny]

    @post_docs(
        summary="Refresh access token",
        description=("Generates a new access token using a valid refresh token."),
        tags=["Authentication"],
        operation_id="auth_token_refresh",
        request=RefreshSerializer,
        responses=RefreshResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
