from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name