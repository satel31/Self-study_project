from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Question, UserAnswer
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.question import QuestionSerializer, QuestionWithAnswerSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    """Создание вопроса.
       Для создания вопроса необходимо ввести тест вопроса и pk теста, к которому относится вопрос.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class QuestionListAPIView(generics.ListAPIView):
    """Получение списка вопросов.
       Есть фильтр и поиск по тесту.
       Доступно только для авторизованных пользователей."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['test']
    filterset_fields = ('test',)


class QuestionDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного вопроса по его pk.
       Если пользователь уже отвечал на этот вопрос, то будет выведен также ответ пользователя.
       Доступно только для авторизованных пользователей."""
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if UserAnswer.objects.filter(question=self.get_object().pk, user=self.request.user.pk).exists():
            return QuestionWithAnswerSerializer
        else:
            return QuestionSerializer


class QuestionUpdateAPIView(generics.UpdateAPIView):
    """Обновление вопроса.
       Доступно только для пользователя с ролью модератора."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class QuestionDeleteAPIView(generics.DestroyAPIView):
    """Удаление вопроса.
       Доступно только для пользователя с ролью модератора."""
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
