from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = 'user'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # user
    path('add_user/', UserCreateAPIView.as_view(), name='add_user'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),

]
