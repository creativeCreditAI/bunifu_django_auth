from rest_framework.generics import CreateAPIView
from ..serializers.register import RegisterSerializer
from ...models.users import BunifuUser


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = BunifuUser.objects.all()
