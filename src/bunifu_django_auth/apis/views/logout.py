from rest_framework.response import Response
from rest_framework import status, permissions
from ..serializers.logout import LogoutSerializer
from rest_framework.generics import GenericAPIView

class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK,
        )