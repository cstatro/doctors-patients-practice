from .models import Patient
from rest_framework import serializers

from django.core.validators import MinValueValidator


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'age', 'id')

    def create(self):
        if self.is_valid():
            new_patient = Patient(**self.validated_data)
            PatientSerializer(new_patient.save())
            return PatientSerializer(new_patient).data
        else:
            return self.errors

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("It's below 0")
        else:
            return value
