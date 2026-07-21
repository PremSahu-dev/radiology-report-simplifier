import os

from rest_framework.decorators import action

from rest_framework.decorators import action
from django.http import FileResponse

import traceback

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Report
from .serializers import ReportSerializer

from ai_model.inference.predict import predict
from nlp.api.interface import process_report

from pdf_generator.generator import generate_pdf

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    queryset = Report.objects.all().order_by("created_at")

    def get_queryset(self):
        qs = Report.objects.all().order_by("created_at")

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

    def perform_create(self, serializer):

        report = serializer.save()

        if report.image:

         image_path = report.image.path

         try:

            result = predict(
                image_path,
                report.scan_type
            )
            

            # AI Prediction
            report.ai_prediction = result["prediction"]
            report.confidence = result["confidence"]
            # NLP Simplification
            nlp_report = process_report(
                result,
                report.scan_type
            )
            
            report.severity = nlp_report.get(
                "severity",
                "Pending"
            )

            report.recommendation = nlp_report.get(
                   "recommendation",
                       ""
            )

            report.severity = nlp_report.get(
                "severity",
                "Pending"
            )

            report.status = "Completed"
            report.save()
            report_json = {

                "title": "AI Generated Medical Report",

                "patient": report.patient.name,

                "scan_type": report.scan_type,

                "prediction": report.ai_prediction,

                "confidence": report.confidence,

                "recommendation": report.recommendation,

                "status": report.status

                 }

            pdf_result = generate_pdf(

                 report_json,

                f"media/pdfs/report_{report.id}.pdf"

            )
            report.pdf_file = f"pdfs/report_{report.id}.pdf"
            report.save()
            print(pdf_result)

         except Exception as e:
            traceback.print_exe()
            report.status = "Failed"
            report.recommendation = str(e)

        report.save() 
    
    @action(detail=True, methods=["get"])
    
    def download_pdf(self, request, pk=None):

      report = self.get_object()

      if not report.pdf_file:
        return Response(
            {"error": "PDF not found"},
            status=404
        )

      return FileResponse(
        open(report.pdf_file.path, "rb"),
        as_attachment=True,
        filename=f"report_{report.id}.pdf"
    )
        
    