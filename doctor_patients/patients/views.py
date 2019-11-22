from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer


class PatientsListView(APIView):
    def post(self, request, format=None):
        patient = PatientSerializer(data=request.data)
        if patient.is_valid():
            patient_record = patient.create()
            return Response(patient_record, status=status.HTTP_201_CREATED)
        else:
            return Response(patient.errors, status=status.HTTP_400_BAD_REQUEST)
