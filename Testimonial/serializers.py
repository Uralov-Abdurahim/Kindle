from rest_framework import serializers
from Testimonial.models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'