from rest_framework import serializers

from apps.learning.models import Material, Test, Section
from apps.learning.serializers.test import TestSerializer


class MaterialSerializer(serializers.ModelSerializer):
    tests = TestSerializer(read_only=True, many=True)
    test_count = serializers.SerializerMethodField()
    section = serializers.SlugRelatedField(slug_field='section_name', queryset=Section.objects.all())

    def get_test_count(self, material):
        return Test.objects.filter(material=material.pk).count()

    class Meta:
        model = Material
        fields = '__all__'
