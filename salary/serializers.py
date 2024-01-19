from rest_framework.serializers import ModelSerializer
from .models import PaySlip
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class SlipSerializer(ModelSerializer):
    
    employee_details = EmployeeSerializer(source='employee', read_only=True)
        
    class Meta:
        model = PaySlip
        fields = ['id', 'month', 'year', 'is_paid', 'salary_value', 'employee_details']