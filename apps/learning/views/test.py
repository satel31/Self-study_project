from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Test
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.test import TestSerializer


class TestCreateAPIView(generics.CreateAPIView):
    """Создание теста.
       Для создания теста необходимо ввести имя теста и описание.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class TestListAPIView(generics.ListAPIView):
    """Получение списка тестов.
       Есть фильтр и поиск по имени теста и метариала.
       Доступно только для авторизованных пользователей."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['test_name', 'material']
    filterset_fields = ('test_name', 'material',)


class TestDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного теста по его pk.
       Доступно только для авторизованных пользователей."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]


class TestUpdateAPIView(generics.UpdateAPIView):
    """Обновление теста.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class TestDeleteAPIView(generics.DestroyAPIView):
    """Удаление теста.
       Доступно только для пользователя с ролью модератора."""
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
