from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ApplicationSerializer
from .models import Application

class ApplicationListView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        applications=Application.objects.filter(user=request.user)
        serializer=ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    
class ApplicationCreateView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        serializer=ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

