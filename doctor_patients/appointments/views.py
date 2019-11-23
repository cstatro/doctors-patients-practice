from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.


class AppointmentsList(APIView):
    def get(self, request, format=None):
        appointments = Appointment.objects.all()
        serialized_appointments = AppointmentSerializer(
            appointments, many=True)
        return Response(serialized_appointments)
