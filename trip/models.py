from django.db import models
from user.models import Person
from employee.models import Employee
from django.utils import timezone
# Create your models here.

class TripAdmin(Person):
    is_trip_admin = models.BooleanField(default=True)



class Trip(models.Model):
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
    datetime = models.DateTimeField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    seat = models.IntegerField(null=True)
    type = models.CharField(max_length=50, null=True)
    is_approved = models.BooleanField(default=False)
    status = models.CharField(max_length=50, null=True, default='Pending')
    trip_created = models.DateField(default=timezone.now)