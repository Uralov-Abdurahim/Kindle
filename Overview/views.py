from django.shortcuts import render
from rest_framework.views import APIView
from Overview.models import Overview
from Overview.serializer import OverviewSerializer
from rest_framework.response import Response

class OverviewAPI(APIView):
    def get(self, request):
        overview = Overview.objects.all()
        serializer = OverviewSerializer(overview, many=True)
        return Response(serializer.data)