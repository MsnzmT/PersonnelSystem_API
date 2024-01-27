from rest_framework import serializers
from .models import Trip
from employee.serializers import EmployeeSerializer


class RequestTripSerializer(serializers.ModelSerializer):
    
    datetime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.000Z", input_formats=["%Y-%m-%dT%H:%M:%S.000Z"])
    employee_detail = EmployeeSerializer(source='employee', read_only=True)
    
    class Meta:
        model = Trip
        fields = ('id', 'source', 'destination', 'type', 'datetime', 'seat', 'trip_created', 'employee_detail')
    
    def create(self, validated_data):
        user = self.context['request'].user.employee
        return Trip.objects.create(
            employee=user,
            source=validated_data['source'],
            destination=validated_data['destination'],
            type=validated_data['type'],
            seat=int(validated_data['seat']),
            datetime=validated_data['datetime'],
        )