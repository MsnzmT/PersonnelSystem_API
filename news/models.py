from django.db import models
from user.models import Person
# Create your models here.

class NewsAdmin(Person):
    is_news_admin = models.BooleanField(default=True)


class News(models.Model):
    
    STATUS_CHOICES = (
        ('P', 'Published'),
        ('U', 'Unpublished'),
        ('A', 'Archived'),
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(NewsAdmin, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images', blank=True, null=True)
    def __str__(self):
        return self.title

