from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RequestTripSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Trip
# Create your views here.


class RequestTripView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = RequestTripSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


class TripView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trips = Trip.objects.filter(is_approved=False).exclude(status='Rejected')
        serializer = RequestTripSerializer(trips, many=True)
        return Response(serializer.data, status=200)


class TripEmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, trip_id):
        trip = Trip.objects.get(id=trip_id)
        serializer = RequestTripSerializer(trip)
        return Response(serializer.data, status=200)
        


class AcceptTripView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, trip_id):
        trip = Trip.objects.get(id=trip_id)
        trip.is_approved = True
        if trip.type == 'havayi':
            trip.status = 'Send to Airline'
        else:
            trip.status = 'Accepted'
        trip.save()
        return Response({'message': 'Trip Accepted'}, status=200)


class RejectTripView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, trip_id):
        trip = Trip.objects.get(id=trip_id)
        trip.is_approved = False
        trip.status = 'Rejected'
        trip.save()
        return Response({'message': 'Trip Rejected'}, status=200)
    


class AllEmployeeTripsView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, personnel_number):
        trips = Trip.objects.filter(employee__personnelNumber=personnel_number)
        serializer = RequestTripSerializer(trips, many=True)
        return Response(serializer.data, status=200)