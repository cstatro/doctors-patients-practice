from django.test import TestCase
from .models import Patient


class TestPatientCreate(TestCase):
    def setUp(self):
        patient_one = Patient.objects.create(
            first_name="Bob", last_name="Barker", age=7)

    def test_patient_one(self):
        """checking to see if the patient creates"""
        patient = Patient.objects.first()
        self.assertEqual(patient.first_name, "bob")
        self.assertEqual(patient.last_name, "barker")
        self.assertEqual(patient.age, 7)
