from django.test import TestCase
from .models import Patient
from .serializers import PatientSerializer


class TestPatientCreate(TestCase):
    def setUp(self):
        patient_one = Patient.objects.create(
            first_name="Bob", last_name="Barker", age=7)

    def test_patient_one(self):
        """checking to see if the patient creates directly from Model"""
        patient = Patient.objects.first()
        self.assertEqual(patient.first_name, "Bob")
        self.assertEqual(patient.last_name, "Barker")
        self.assertEqual(patient.age, 7)

    def test_patient_two_creates(self):
        """Testing the serializer creates a patient"""
        patient_two = PatientSerializer(
            data=dict(first_name="Jeb", last_name="Bush", age=53))
        x = patient_two.create()
        self.assertEqual(x.get('age'), 53)
