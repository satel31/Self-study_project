from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Answer
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    """Создание правильного ответа на вопрос.
       Для создания ответа необходимо ввести текст ответа и pk вопроса, которому принадлежит ответ.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class AnswerUpdateAPIView(generics.UpdateAPIView):
    """Обновление правильного ответа на вопрос.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
