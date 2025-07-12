from rest_framework import serializers
from Home.models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'