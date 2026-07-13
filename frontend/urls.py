from django.urls import path
from .views import (patient_page,login_page)

urlpatterns = [
    
     path(
        "login/",
        login_page,
        name="login"
    ),

    path("patients/", patient_page),
]