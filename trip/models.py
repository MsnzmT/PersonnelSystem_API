from django.db import models
from user.models import Person
# Create your models here.

class TripAdmin(Person):
    is_trip_admin = models.BooleanField(default=True)