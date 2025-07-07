from rest_framework import serializers
from Overview.models import Overview

class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'