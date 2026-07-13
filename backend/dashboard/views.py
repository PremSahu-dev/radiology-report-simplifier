from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.patients.models import Patient
from backend.reports.models import Report


class DashboardAPIView(APIView):

    def get(self, request):

        data = {
            "total_patients": Patient.objects.count(),
            "total_reports": Report.objects.count(),
            "pending_reports": Report.objects.filter(status="Pending").count(),
            "completed_reports": Report.objects.filter(status="Completed").count(),
        }

        return Response(data)

