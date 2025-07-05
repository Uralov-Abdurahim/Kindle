from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from About.models import About
from About.serializers import AboutSerializer

class AboutApiView(APIView):
    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about)
        return Response(serializer.data)