from django.contrib import admin
from .models import Conversation, Message
# Register your models here.

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    list_display = ['sender', 'receiver', 'message_text', 'created_at']


class ConversationAdmin(admin.ModelAdmin):
    list_display = ['user1', 'user2', 'created_at', 'updated_at']
    inlines = [MessageInline]

admin.site.register(Conversation, ConversationAdmin)