from django.shortcuts import render
from rest_framework.views import APIView
from Testimonial.models import Testimonial
from Testimonial.serializers import TestimonialSerializer
from rest_framework.response import Response

class TestimonialView(APIView):
    def get(self, request):
        testimonial = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonial, many=True)
        return Response(serializer.data)
    
