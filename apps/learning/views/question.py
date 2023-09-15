from rest_framework import generics

from apps.learning.models import Question, UserAnswer
from apps.learning.serializers.question import QuestionSerializer, QuestionWithAnswerSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionSerializer


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if UserAnswer.objects.filter(question=self.get_object().pk, user=self.request.user.pk).exists():
            return QuestionWithAnswerSerializer
        else:
            return QuestionSerializer


class QuestionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
