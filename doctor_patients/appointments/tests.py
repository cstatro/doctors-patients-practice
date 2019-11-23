from django.test import TestCase
from doctors.models import Doctor
from patients.models import Patient
from .models import Appointment
from .serializers import AppointmentSerializer

# Create your tests here.


class AppointmentCreate(TestCase):
    def setUp(self):
        d = Doctor.objects.create(first_name="Selmy",
                                  last_name="Geb!", speciality="applesauce")
        p = Patient.objects.create(
            first_name="sally", last_name="white", age=12)
        Appointment.objects.create(
            doctor=d, patient=p, description="applesauce in my boot")

    def test_appointment_created(self):
        """checks to see if appointments are creating from model"""
        appt = Appointment.objects.first()
        self.assertIsInstance(appt, Appointment)
        self.assertEqual(appt.patient.first_name, "sally")

    def test_serializer_works_appointment(self):
        """test that the serializer is working on appointment"""
        appt = Appointment.objects.first()
        serialized = AppointmentSerializer(appt)
        self.assertEquals(serialized.data.get(
            'description'), 'applesauce in my boot')
