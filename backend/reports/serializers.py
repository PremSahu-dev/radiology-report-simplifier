from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True,
    )

    class Meta:
        model = Report
        fields = [
            "id",
            "patient",
            "patient_name",
            "scan_type",
            "image",
            "ai_prediction",
            "confidence",
            "severity",
            "recommendation",
            "status",
            "created_at",
        ]
        def to_representation(self, instance):
         data = super().to_representation(instance)
         data["patient_name"] = instance.patient.name
         return data
