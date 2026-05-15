from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..api_docs import post_docs


from ..serializers.logout import LogoutSerializer, LogoutResponseSerializer





class LogoutView(GenericAPIView):
    """
    API endpoint for logging out authenticated users.
    """

    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    @post_docs(
        summary="Logout user",
        description=(
            "Logs out the currently authenticated user by invalidating "
            "the provided refresh token."
        ),
        tags=["Authentication"],
        operation_id="auth_logout",
        request=LogoutSerializer,
        responses=LogoutResponseSerializer,
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK,
        )
