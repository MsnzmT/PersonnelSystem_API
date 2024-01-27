from rest_framework import serializers
from .models import Leave
from employee.serializers import EmployeeSerializer



class LeaveSerializer(serializers.ModelSerializer):
    # start_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.000Z", input_formats=["%Y-%m-%dT%H:%M:%S.000Z"])
    # end_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.000Z", input_formats=["%Y-%m-%dT%H:%M:%S.000Z"])

    class Meta:
        model = Leave
        fields = ['id', 'start_date', 'end_date', 'description', 'is_approved', 'reason', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user.employee
        validated_data['employee'] = user
        return Leave.objects.create(**validated_data)


class LeaveSerializerForManager(serializers.ModelSerializer):
    
    employee_details = EmployeeSerializer(source='employee', read_only=True)
    
    class Meta:
        model = Leave
        fields = ['id', 'start_date', 'end_date', 'description', 'is_approved', 'reason', 'employee_details', 'created_at']