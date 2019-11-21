from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(
        default=-1, validators=[MinValueValidator(0, "must be a postive integer")])
