from django.test import TestCase
from .models import Doctor
# Create your tests here.


class TestModelCreate(TestCase):

    def test_doctor_creates(self):
        """testing to make sure the doctor creates from the model"""
        doc = Doctor.objects.create(
            first_name="jeb", last_name="bush", speciality="losing bigly")
        self.assertEquals(doc.first_name, 'jeb')
