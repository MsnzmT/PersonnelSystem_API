from django.db import models
from user.models import Person
from employee.models import Employee
from django.utils import timezone


class LeaveAdmin(Person):
    is_leave_admin = models.BooleanField(default=True)


class Leave(models.Model):
    
    REASON_CHOICES = (
        ('اعیاد رسمی', 'اعیاد رسمی'),
        ('معمولی', 'معمولی'),
        ('اضطراری', 'اضطراری'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    reason = models.CharField(max_length=100, choices=REASON_CHOICES)
    created_at = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, null=True, default='Pending')