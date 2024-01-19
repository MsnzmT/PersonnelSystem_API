from rest_framework import serializers
from .models import Leave
from datetime import datetime

class LeaveSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%a %b %d %Y %H:%M:%S %Z%z (Iran Standard Time)", input_formats=["%a %b %d %Y %H:%M:%S GMT%z (Iran Standard Time)"])
    end_date = serializers.DateTimeField(format="%a %b %d %Y %H:%M:%S %Z%z (Iran Standard Time)", input_formats=["%a %b %d %Y %H:%M:%S GMT%z (Iran Standard Time)"])

    class Meta:
        model = Leave
        fields = ['id', 'start_date', 'end_date', 'description', 'is_approved', 'reason']

    def create(self, validated_data):
        user = self.context['request'].user.employee
        validated_data['employee'] = user
        return Leave.objects.create(**validated_data)
