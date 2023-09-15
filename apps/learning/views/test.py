from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.learning.models import Test
from apps.learning.permissions import ModeratorPermission
from apps.learning.serializers.test import TestSerializer


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, ModeratorPermission]


class TestListAPIView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]


class TestDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]


class TestUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]


class TestDeleteAPIView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermission]
