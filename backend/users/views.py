from django.shortcuts import render
from .serializers import UserListSerializer, UserRegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        users=User.objects.all()
        serializer=UserListSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

