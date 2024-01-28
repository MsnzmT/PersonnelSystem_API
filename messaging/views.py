from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from employee.models import Employee
from .models import Conversation, Message
from .serializers import ConversationSerializer, ConversationSerializer2
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class MessagingView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user.employee
        conversations = Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)
        conversations = conversations.order_by('-updated_at')

        return Response(ConversationSerializer2(conversations, many=True, context={'request': request}).data, status=200)

    def post(self, request):
        sender_user = request.user.employee
        receiver_personnel_number = request.data['personnel_number']
        receiver_user = Employee.objects.get(personnelNumber=receiver_personnel_number)
        
        message_text = request.data['message_text']
        conversationn = Conversation.objects.filter(user1=sender_user, user2=receiver_user).first()
        if not conversationn:
            conversationn = Conversation.objects.filter(user1=receiver_user, user2=sender_user).first()
        if not conversationn:
            conversationn = Conversation.objects.create(user1=sender_user, user2=receiver_user)
            
        new_message = Message.objects.create(conversation=conversationn, sender=sender_user, receiver=receiver_user, message_text=message_text)
        return Response({'message': 'message sent successfully'})


class ConversationMessagesView(APIView):
    def get(self, request, conversation_id):
        conversation = Conversation.objects.get(id=conversation_id)
        return Response(ConversationSerializer(conversation).data, status=200)