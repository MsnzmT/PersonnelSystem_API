from django.urls import path
from .views import RequestTripView, TripView, TripEmployeeDetailView, AcceptTripView, RejectTripView, AllEmployeeTripsView

urlpatterns = [
    path('request/', RequestTripView.as_view()),
    path('all/', TripView.as_view()),
    path('detail/<int:trip_id>/', TripEmployeeDetailView.as_view()),
    path('accept/<int:trip_id>/', AcceptTripView.as_view()),
    path('reject/<int:trip_id>/', RejectTripView.as_view()),
    path('all/', AllEmployeeTripsView.as_view()),
]