from django.urls import path
from .views import LeaveRequestView, SeeAllLeaveRequestsView, AproveLeaveView, RejectLeaveView, SeeAllLeaveRequestsForEmployeeView


urlpatterns = [
    path('request/', LeaveRequestView.as_view()),
    path('see-all/', SeeAllLeaveRequestsView.as_view()),
    path('approve/<int:leave_id>/', AproveLeaveView.as_view()),
    path('reject/<int:leave_id>/', RejectLeaveView.as_view()),
    path('see-all-for-employee/<int:personnel_number>/', SeeAllLeaveRequestsForEmployeeView.as_view()),
]