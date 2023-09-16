from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.user.models import User
from apps.user.permissions import IsOwnerPermission
from apps.user.serializers import UserSerializer, StrangerUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя.
       Для создания секции необходимо ввести e-mail и пароль.
       Доступно только для любого пользователя."""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """Получение списка пользователей.
       Доступно только для авторизованных пользователей."""
    queryset = User.objects.all()
    serializer_class = StrangerUserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного пользователя по его pk.
       Доступно только для авторизованных пользователей."""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.email == self.get_object().email:
            return UserSerializer
        return StrangerUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователя (можно обновить только своего пользователя).
       Доступно только для авторизованных пользователей."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]


class UserDeleteAPIView(generics.DestroyAPIView):
    """Удаление пользователя (можно удалить только своего пользователя).
       Доступно только для авторизованных пользователей."""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]
