from rest_framework.serializers import ModelSerializer
from .models import Doctor
from appointments.serializers import AppointmentSerializer


class DoctorSerializer(ModelSerializer):
    appointments = AppointmentSerializer(many=true)

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'appointments')
