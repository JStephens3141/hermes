from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):

    working_date = models.DateField()
    on_schedule = models.BooleanField()
    worked = models.BooleanField()
    took_lunch = models.BooleanField()
    took_breaks = models.BooleanField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
