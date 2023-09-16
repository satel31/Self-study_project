from rest_framework import serializers

from apps.learning.models import Section, Material
from apps.learning.serializers.material import MaterialSerializer


class SectionSerializer(serializers.ModelSerializer):
    material_count = serializers.SerializerMethodField()
    material = MaterialSerializer(read_only=True, many=True)

    def get_material_count(self, section):
        return Material.objects.filter(section=section.pk).count()

    class Meta:
        model = Section
        fields = '__all__'
