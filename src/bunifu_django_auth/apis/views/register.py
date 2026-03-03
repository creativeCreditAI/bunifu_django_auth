from rest_framework.generics import CreateAPIView
from ..serializers.register import RegisterSerializer
from ...models.users import User


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
