from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Answer
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class AnswerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]

