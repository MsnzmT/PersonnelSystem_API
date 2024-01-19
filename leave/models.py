from django.db import models
from user.models import Person



class LeaveAdmin(Person):
    is_leave_admin = models.BooleanField(default=True)


