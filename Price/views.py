from django.shortcuts import render
from rest_framework.views import APIView
from Price.serializer import PriceSerializer
from Price.models import Price
from rest_framework.response import Response


class PriceView(APIView):
    def get(self, reqeust):
        price = Price.objects.all()
        serializer = PriceSerializer(price, many=True)
        return Response(serializer.data)