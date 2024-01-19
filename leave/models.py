from django.db import models
from user.models import Person
from employee.models import Employee



class LeaveAdmin(Person):
    is_leave_admin = models.BooleanField(default=True)


class Leave(models.Model):
    
    REASON_CHOICES = (
        ('Sick', 'Sick'),
        ('Marriage', 'Marriage'),
        ('Death', 'Death'),
        ('Childbirth', 'Childbirth'),
        ('Other', 'Other'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    reason = models.CharField(max_length=100, choices=REASON_CHOICES)