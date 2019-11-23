from django.db import models

# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.last_name}"
