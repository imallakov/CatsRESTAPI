from django.urls import path

from .views import UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/', TokenRefreshView.as_view(), name='token'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),  # Add this line
]
