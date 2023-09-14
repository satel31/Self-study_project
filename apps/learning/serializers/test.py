from rest_framework import serializers

from apps.learning.models import Test


class TestSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer
    # try_count = serializers.SerializerMethodField()

    #def get_try_count(self, test):
        #return Try.objects.filter(test=test.pk).count()

    class Meta:
        model = Test
        fields = '__all__'
