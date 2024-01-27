from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import LeaveSerializer, LeaveSerializerForManager
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Leave




class LeaveRequestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeeAllLeaveRequestsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeaveSerializerForManager
    queryset = Leave.objects.filter(status='Pending')


class AproveLeaveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        leave_id = kwargs['leave_id']
        leave = Leave.objects.get(id=leave_id)
        leave.is_approved = True
        leave.status = 'Approved'
        leave.save()
        return Response({"status":"ok"},status=200)
    
class RejectLeaveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        leave_id = kwargs['leave_id']
        leave = Leave.objects.get(id=leave_id)
        leave.is_approved = False
        leave.status = 'Rejected'
        leave.save()
        return Response({"status":"ok"},status=200)


class SeeAllLeaveRequestsForEmployeeView(ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = LeaveSerializer
    def get_queryset(self):
        personnel_number = self.kwargs.get('personnel_number')
        return Leave.objects.filter(employee__personnelNumber=personnel_number)
    

class LeaveDetailsView(APIView):
    
    def get(self, request, leave_id):
        leave = Leave.objects.get(id=leave_id)
        serializer = LeaveSerializerForManager(instance=leave)
        return Response(serializer.data, status=200)