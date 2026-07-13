from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")
def patient_page(request):
    return render(request, "patient.html")