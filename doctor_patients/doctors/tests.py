from django.test import TestCase
from .models import Doctor
from django.http import HttpRequest
from .views import DoctorListView, DoctorView
# Create your tests here.


class TestModelCreate(TestCase):
    def setUp(self):
        doc = Doctor.objects.create(
            first_name="Harry", last_name="bush", speciality="losing bigly")

    def test_doctor_creates(self):
        """testing to make sure the doctor creates from the model"""
        doc = Doctor.objects.create(
            first_name="jeb", last_name="bush", speciality="losing bigly")
        self.assertEquals(doc.first_name, 'jeb')

    def test_doctors_list_view(self):
        """makes sure api endpoint is returning correctly for list view"""
        request = HttpRequest()
        api = DoctorListView()
        response = api.get(request)
        self.assertEquals(response.status_code, 200, "should be a 200 code!")
        self.assertIsInstance(response.data, list,
                              "should be returning a list")

    def test_doctor_view(self):
        """checks to make sure that doctor view is returning the correct doctor"""
        request = HttpRequest()
        api = DoctorView()
        response = api.get(request, 1)
        self.assertEquals(response.status_code, 200)
