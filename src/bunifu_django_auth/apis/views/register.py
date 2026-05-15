
from ..api_docs import post_docs

from ...models.users import BunifuUser
from ..serializers.register import RegisterSerializer, RegisterResponseSerializer

from rest_framework.generics import CreateAPIView
from rest_framework import permissions



class RegisterView(CreateAPIView):
    """
    API endpoint for registering new users.
    """

    serializer_class = RegisterSerializer
    queryset = BunifuUser.objects.all()
    permission_classes = [permissions.AllowAny]

    @post_docs(
        summary="Register user",
        description=(
            "Creates a new user account using the provided registration "
            "details."
        ),
        tags=["Authentication"],
        operation_id="auth_register",
        request=RegisterSerializer,
        responses={
            201: RegisterResponseSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
