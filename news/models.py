from django.db import models
from user.models import Person
# Create your models here.

class NewsAdmin(Person):
    is_news_admin = models.BooleanField(default=True)