from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Doctor
from .serializers import DoctorSerializer
# Create your views here.


class DoctorListView(APIView):
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serialized = DoctorSerializer(doctors, many=True)
        return Response(serialized.data)
