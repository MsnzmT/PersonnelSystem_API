from django.db import models
from user.models import Person

class Employee(Person):
    
    DEPARTMENT_CHOICES = (
        ("INSTRUMENT","INSTRUMENT"),
        ("MAINTENANCE","MAINTENANCE"),
        ("MECHANICAL","MECHANICAL"),
        ("ELECTRICITY","ELECTRICITY"),
        ("IT","IT"),
        ("MANAGEMENT","MANAGEMENT"),
    )
    
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True)