from django.db import models
from user.models import Person
from employee.models import Employee
# Create your models here.

class PaySalaryAdmin(Person):
    is_paysalary_admin = models.BooleanField(default=True)


class PaySlip(models.Model):
    
    MONTH_CHOICES = (
        ('Farvardin', 'Farvardin'),
        ('Ordibehesht', 'Ordibehesht'),
        ('Khordad', 'Khordad'),
        ('Tir', 'Tir'),
        ('Mordad', 'Mordad'),
        ('Shahrivar', 'Shahrivar'),
        ('Mehr', 'Mehr'),
        ('Aban', 'Aban'),
        ('Azar', 'Azar'),
        ('Dey', 'Dey'),
        ('Bahman', 'Bahman'),
        ('Esfand', 'Esfand'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    year = models.IntegerField()
    salary_value = models.BigIntegerField()
    is_paid = models.BooleanField(default = False)