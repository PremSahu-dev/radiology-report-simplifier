from django.db import models
from backend.patients.models import Patient

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scan_type = models.CharField(max_length=50)
    image = models.ImageField(
    upload_to="reports/",
    blank=True,
    null=True
)
    ai_prediction = models.CharField(max_length=255, blank=True, default="")
    confidence = models.FloatField(default=0)

    severity = models.CharField(
    max_length=50,
    default="Pending")

    recommendation = models.TextField(
    blank=True,
    default="")

    status = models.CharField(
    max_length=30,
    default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.patient_name} - {self.scan_type}"