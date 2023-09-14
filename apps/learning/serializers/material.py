from rest_framework import serializers

from apps.learning.models import Material, Subscription, Test
from apps.learning.serializers.test import TestSerializer


class MaterialSerializer(serializers.ModelSerializer):
    tests = TestSerializer(read_only=True, many=True)
    subscription = serializers.SerializerMethodField()
    test_count = serializers.SerializerMethodField()

    def get_subscription(self, material):
        return Subscription.objects.filter(material=material).exists()

    def get_test_count(self, material):
        return Test.objects.filter(material=material.pk).count()

    class Meta:
        model = Material
        fields = '__all__'
