from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from Home.models import Home
from Home.serializer import HomeSerializer

class HomeView(APIView):
    def get(self, request):
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data)
        