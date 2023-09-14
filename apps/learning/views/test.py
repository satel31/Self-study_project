from rest_framework import generics

from apps.learning.models import Test
from apps.learning.serializers.test import TestSerializer


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = TestSerializer


class TestListAPIView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestDeleteAPIView(generics.DestroyAPIView):
    queryset = Test.objects.all()
