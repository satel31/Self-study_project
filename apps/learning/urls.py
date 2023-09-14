from django.urls import path

from apps.learning.views.section import SectionCreateAPIView, SectionListAPIView, SectionDetailAPIView, \
    SectionUpdateAPIView, SectionDeleteAPIView

app_name = 'learning'

urlpatterns = [
    # section
    path('add_section/', SectionCreateAPIView.as_view(), name='add_section'),
    path('sections/', SectionListAPIView.as_view(), name='sections'),
    path('sections/<int:pk>/', SectionDetailAPIView.as_view(), name='section'),
    path('sections/update/<int:pk>/', SectionUpdateAPIView.as_view(), name='section_update'),
    path('sections/delete/<int:pk>/', SectionDeleteAPIView.as_view(), name='section_delete'),

]