from rest_framework import generics

from apps.learning.serializers.section import SectionSerializer
from apps.learning.pagination import SectionPagination
from apps.learning.models import Section


class SectionCreateAPIView(generics.CreateAPIView):
    serializer_class = SectionSerializer


class SectionListAPIView(generics.ListAPIView):
    serializer_class = SectionSerializer
    pagination_class = SectionPagination
    queryset = Section.objects.all()


class SectionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionDeleteAPIView(generics.DestroyAPIView):
    queryset = Section.objects.all()
