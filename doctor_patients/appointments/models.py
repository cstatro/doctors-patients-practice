from django.db import models

# Create your models here.


class Appointment(models.Model):
    doctor = models.ForeignKey(
        'doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE, related_name='appointments')
    description = models.CharField(max_length=250)
