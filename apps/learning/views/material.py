from rest_framework import generics

from apps.learning.models import Material
from apps.learning.serializers.material import MaterialSerializer


class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDetailAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDeleteAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
