from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by("-created_at")
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Report.objects.all().order_by("-created_at")

        patient = self.request.query_params.get("patient")
        scan_type = self.request.query_params.get("scan_type")
        status = self.request.query_params.get("status")

        if patient:
            qs = qs.filter(patient_id=patient)

        if scan_type:
            qs = qs.filter(scan_type__icontains=scan_type)

        if status:
            qs = qs.filter(status__iexact=status)

        return qs
