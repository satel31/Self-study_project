from rest_framework import serializers
from rest_framework.request import Request

from apps.learning.models import Test, Question, UserAnswer
from apps.learning.serializers.question import QuestionSerializer


class TestSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()
    right_answers = serializers.SerializerMethodField()
    questions = QuestionSerializer(read_only=True, many=True)

    def get_question_count(self, test):
        return Question.objects.filter(test=test.pk).count()

    def get_right_answers(self, test):
        current_user = self.context['request'].user
        right_answers = 0
        questions = Question.objects.filter(test=test.pk)
        for question in questions:
            try:
                if UserAnswer.objects.filter(question=question.pk, user=current_user).last().is_passed:
                    right_answers += 1
            except AttributeError:
                pass
        return right_answers

    class Meta:
        model = Test
        fields = '__all__'
