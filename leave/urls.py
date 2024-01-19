from django.urls import path
from .views import LeaveRequestView


urlpatterns = [
    path('request/', LeaveRequestView.as_view()),
]