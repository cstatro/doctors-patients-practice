from django.db import models
from appointments.models import Appointment
# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    appointments = models.ManyToManyField(Appointment)

    def __str__(self):
        return f"Dr. {self.last_name}"
