from .models import Patient
from rest_framework import serializers

from django.core.validators import MinValueValidator


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'age', 'id')

    def create(self):
        new_patient = Patient(**self.validated_data)
        new_patient.first_name = new_patient.first_name.lower()
        new_patient.last_name = new_patient.last_name.lower()
        new_patient.save()
        return PatientSerializer(new_patient).data

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("It's below 0")
        else:
            return value
