from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import UserAnswer, Question, Answer
from apps.learning.serializers.user_answer import UserAnswerSerializer


class UserAnswerCreateAPIView(generics.CreateAPIView):
    """Создание ответа пользователя на вопрос.
       Для создания ответа необходимо ввести текст ответа и pk вопроса.
       Доступно только для авторизованных пользователей."""
    serializer_class = UserAnswerSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_ans = serializer.save()
        question = Question.objects.get(pk=new_ans.question.pk)
        correct_answer = Answer.objects.get(question=question.pk)
        if new_ans.answer.lower() == correct_answer.text.lower():
            new_ans.is_passed = True
        elif new_ans.answer.lower() != correct_answer.text.lower():
            new_ans.is_passed = False
        new_ans.user = self.request.user
        new_ans.save()


class UserAnswerDeleteAPIView(generics.DestroyAPIView):
    """Удаление ответа пользователя.
       Доступно только для авторизованных пользователей."""
    queryset = UserAnswer.objects.all()
    #permission_classes = [IsAuthenticated]
