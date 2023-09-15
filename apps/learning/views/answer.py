from rest_framework import generics

from apps.learning.models import Answer
from apps.learning.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer


class AnswerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
