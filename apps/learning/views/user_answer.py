from rest_framework import generics

from apps.learning.models import UserAnswer, Question, Answer
from apps.learning.serializers.user_answer import UserAnswerSerializer


class UserAnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer

    def perform_create(self, serializer):
        new_ans = serializer.save()
        question = Question.objects.get(pk=new_ans.question.pk)
        correct_answer = Answer.objects.get(question=question.pk)
        if new_ans.answer.lower() == correct_answer.text.lower():
            new_ans.is_passed = True
        elif new_ans.answer.lower() != correct_answer.text.lower():
            new_ans.is_passed = False
        # new_ans.user = self.request.user
        new_ans.save()


class UserAnswerDeleteAPIView(generics.DestroyAPIView):
    queryset = UserAnswer.objects.all()
