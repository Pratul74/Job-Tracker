from django.shortcuts import render
from .serializers import UserListSerializer, UserRegisterSerializer
from .models import User
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer

class UserRegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer






