from django.db import models
from employee.models import Employee
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.


class Conversation(models.Model):
    user1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='user2')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        unique_together = (('user1', 'user2'),)
    
    def clean(self):
        super().clean()
        if self.user1 == self.user2:
            raise ValidationError('user1 and user2 must be different.')
        
    def __str__(self):
        return f'مکالمه ی میان  :  {self.user1.first_name} {self.user1.last_name} - {self.user2.first_name} {self.user2.last_name}'



class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver')
    message_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        super().clean()
        if self.sender != self.conversation.user1 and self.sender != self.conversation.user2:
            raise ValidationError('Sender must be either user1 or user2 of the conversation')
        if self.receiver != self.conversation.user1 and self.receiver != self.conversation.user2:
            raise ValidationError('Receiver must be either user1 or user2 of the conversation')
        if self.sender == self.receiver:
            raise ValidationError('Sender and receiver must be different.')