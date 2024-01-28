from rest_framework import serializers
from .models import Conversation, Message
from employee.serializers import EmployeeSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = EmployeeSerializer()
    receiver = EmployeeSerializer()
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message_text', 'created_at')

class ConversationSerializer(serializers.ModelSerializer):
    
    messages = MessageSerializer(many=True)
    user1 = EmployeeSerializer()
    user2 = EmployeeSerializer()
    
    class Meta:
        model = Conversation
        fields = ('id','created_at', 'updated_at','user1', 'user2', 'messages')
    


class ConversationSerializer2(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ('id','created_at', 'updated_at','user')
    
    
    def get_user(self, obj):
        request = self.context.get('request')
        logged_in_user = request.user.employee

        if obj.user1 == logged_in_user:
            return f'{obj.user2.first_name} {obj.user2.last_name}'
        elif obj.user2 == logged_in_user:
            return f'{obj.user1.first_name} {obj.user1.last_name}'
