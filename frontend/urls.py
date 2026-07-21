from django.urls import path
from .views import *

urlpatterns = [
    path("", index_page),
    path("login/", login_page),
    path("dashboard/", dashboard_page,name="dashboard"),
    path("upload/", upload_page),
    path("reports/", reports_page),
    path("profile/", profile_page),
    path("patients/", patient_page),
    path("result/", result_page),
    path("register/", register_page),
]