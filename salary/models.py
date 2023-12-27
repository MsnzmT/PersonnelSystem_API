from django.db import models
from user.models import Person
# Create your models here.

class PaySalaryAdmin(Person):
    is_paysalary_admin = models.BooleanField(default=True)