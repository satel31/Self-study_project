from rest_framework import serializers

from apps.learning.models import Question
from apps.learning.serializers.user_answer import UserAnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    user_answers = UserAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'
