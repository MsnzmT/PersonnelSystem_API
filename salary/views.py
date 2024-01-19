from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .models import PaySlip
from .serializers import SlipSerializer
from django.shortcuts import get_object_or_404



class SlipView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaySlip.objects.filter(is_paid=False)
    serializer_class = SlipSerializer


class SlipDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SlipSerializer

    def get_queryset(self):
        return PaySlip.objects.all()

    def get_object(self):
        employee_personnel_number = self.kwargs.get('personnelNumber')
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, employee__personnelNumber=employee_personnel_number)
        return obj


class ModifySlipView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        employee_personnel_number = self.kwargs.get('personnelNumber')
        queryset = PaySlip.objects.filter(is_paid=False)
        obj = get_object_or_404(queryset, employee__personnelNumber=employee_personnel_number)
        obj.salary_value = request.data.get('salary_value')
        obj.save()
        return Response({"message": "Slip has been modified successfully."})

class PaymentSlipView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        employee_personnel_number = self.kwargs.get('personnelNumber')
        queryset = PaySlip.objects.filter(is_paid=False)
        obj = get_object_or_404(queryset, employee__personnelNumber=employee_personnel_number)
        obj.is_paid = True
        obj.save()
        return Response({"message": "Slip has been paid successfully."})
