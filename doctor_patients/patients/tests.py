from django.test import TestCase
from .models import Patient
from .serializers import PatientSerializer
from .views import PatientsListView
from django.http import HttpRequest
from django.apps import apps
# Dynamically loaded models
Doctor = apps.get_model('doctors', 'Doctor')
Appointment = apps.get_model('appointments', 'Appointment')


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


class TestPatientListGet(TestCase):
    def setUp(self):
        patient_one = Patient.objects.create(
            first_name="Bob", last_name="Barker", age=7)
        doctor_jeb = Doctor.objects.create(
            first_name="jeb", last_name='bush', speciality="butts")
        Appointment.objects.create(
            doctor=doctor_jeb, patient=patient_one, description="checking butts")

    def test_to_see_list_returned(self):
        """checks to see if a list is returned"""
        view_api = PatientsListView()
        request = HttpRequest()
        response = view_api.get(request)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list, " this is not a list")

    def test_to_see_if_appointments_exist(self):
        """makes sure an empty list is being serialized as the appointments"""
        patient = Patient.objects.first()
        self.assertIsInstance(list(patient.appointments.all()), list,
                              "list is not present at appointments")

    def test_to_make_sure_appointment_is_made(self):
        """making sure appointment gets made"""
        patient = Patient.objects.first()
        appt = patient.appointments.first()
        self.assertIsInstance(appt, Appointment)
        self.assertEquals(appt.patient.first_name, "Bob")
