from django.urls import path
from .views import MessagingView, ConversationMessagesView


urlpatterns = [
    path('', MessagingView.as_view()),
    path('<int:conversation_id>/', ConversationMessagesView.as_view()),
]