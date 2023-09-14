from django.urls import path

from apps.learning.views.material import MaterialCreateAPIView, MaterialListAPIView, MaterialDetailAPIView, \
    MaterialUpdateAPIView, MaterialDeleteAPIView
from apps.learning.views.section import SectionCreateAPIView, SectionListAPIView, SectionDetailAPIView, \
    SectionUpdateAPIView, SectionDeleteAPIView
from apps.learning.views.test import TestCreateAPIView, TestListAPIView, TestDetailAPIView, TestUpdateAPIView, \
    TestDeleteAPIView

app_name = 'learning'

urlpatterns = [
    # section
    path('add_section/', SectionCreateAPIView.as_view(), name='add_section'),
    path('sections/', SectionListAPIView.as_view(), name='sections'),
    path('sections/<int:pk>/', SectionDetailAPIView.as_view(), name='section'),
    path('sections/update/<int:pk>/', SectionUpdateAPIView.as_view(), name='section_update'),
    path('sections/delete/<int:pk>/', SectionDeleteAPIView.as_view(), name='section_delete'),

    # material
    path('add_material/', MaterialCreateAPIView.as_view(), name='add_material'),
    path('materials/', MaterialListAPIView.as_view(), name='materials'),
    path('materials/<int:pk>/', MaterialDetailAPIView.as_view(), name='material'),
    path('materials/update/<int:pk>/', MaterialUpdateAPIView.as_view(), name='material_update'),
    path('materials/delete/<int:pk>/', MaterialDeleteAPIView.as_view(), name='material_delete'),

    # test
    path('add_test/', TestCreateAPIView.as_view(), name='add_test'),
    path('tests/', TestListAPIView.as_view(), name='tests'),
    path('tests/<int:pk>/', TestDetailAPIView.as_view(), name='test'),
    path('tests/update/<int:pk>/', TestUpdateAPIView.as_view(), name='test_update'),
    path('tests/delete/<int:pk>/', TestDeleteAPIView.as_view(), name='test_delete'),
]
