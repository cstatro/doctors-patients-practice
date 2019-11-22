from django.test import TestCase
from .models import Patient
from .serializers import PatientSerializer
from .views import PatientsListView
from django.http import HttpRequest


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


class TestPatientView(TestCase):

    def test_patient_post(self):
        """checks to see if post request properly returns data"""
        view_api = PatientsListView()
        request = HttpRequest()
        request.data = dict(first_name="Jeb", last_name="Bush", age=53)
        response = view_api.post(request)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data.get('first_name'), 'jeb')

    def test_rejects_bad_age(self):
        """checks to see if it will reject invalid age number"""
        view_api = PatientsListView()
        request = HttpRequest()
        request.data = dict(first_name="Jeb", last_name="Bush", age=-1)
        response = view_api.post(request)
        self.assertEquals(response.status_code, 400)
