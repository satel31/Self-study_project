from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Material
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.material import MaterialSerializer


class MaterialCreateAPIView(generics.CreateAPIView):
    """Создание материала.
       Для создания материала необходимо ввести pk секции, к которому относится материал, название материала и текст.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class MaterialListAPIView(generics.ListAPIView):
    """Получение списка материалов.
       Есть пагинация, фильтр и поиск по имени материала и секции.
       Доступно только для авторизованных пользователей."""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['material_name', 'section']
    filterset_fields = ('material_name', 'section',)


class MaterialDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного материала по его pk.
       Доступно только для авторизованных пользователей."""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialUpdateAPIView(generics.UpdateAPIView):
    """Обновление материала.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class MaterialDeleteAPIView(generics.DestroyAPIView):
    """Удаление материала.
       Доступно только для пользователя с ролью модератора."""
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
