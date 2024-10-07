from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import MyUserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer
