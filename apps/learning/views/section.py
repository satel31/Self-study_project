from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.section import SectionSerializer
from apps.learning.pagination import SectionPagination
from apps.learning.models import Section


class SectionCreateAPIView(generics.CreateAPIView):
    """Создание секции.
       Для создания секции необходимо ввести имя секции.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class SectionListAPIView(generics.ListAPIView):
    """Получение списка секций.
       Есть пагинация, фильтр и поиск по имени секции.
       Доступно только для авторизованных пользователей."""
    serializer_class = SectionSerializer
    pagination_class = SectionPagination
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['section_name']
    filterset_fields = ('section_name',)


class SectionDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретной секции по его pk.
       Доступно только для авторизованных пользователей."""
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(generics.UpdateAPIView):
    """Обновление секции.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class SectionDeleteAPIView(generics.DestroyAPIView):
    """Удаление вопроса.
       Доступно только для пользователя с ролью модератора."""
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
