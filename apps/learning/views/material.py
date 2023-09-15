from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Material
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.material import MaterialSerializer


class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialDetailAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class MaterialDeleteAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
