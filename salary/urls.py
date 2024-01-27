from django.urls import path
from .views import SlipView, SlipDetailView, ModifySlipView, PaymentSlipView, PaidSlipForEmployeeView


urlpatterns = [
    path('slip/', SlipView.as_view()),
    path('slip-details/<str:personnelNumber>/', SlipDetailView.as_view()),
    path('modify-slip/<str:personnelNumber>/', ModifySlipView.as_view()),
    path('payment-slip/<str:personnelNumber>/', PaymentSlipView.as_view()),
    path('paid-slip/<int:personnelNumber>/', PaidSlipForEmployeeView.as_view()),
]