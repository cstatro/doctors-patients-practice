from rest_framework.serializers import ModelSerializer
from .models import Appointment
from doctors.serializers import DoctorSerializer


class AppointmentSerializer(ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('description')
