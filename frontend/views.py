from django.shortcuts import render

def index_page(request):
    return render(request, "index.html")
def login_page(request):
    return render(request, "login_new.html")
def patient_page(request):
    return render(request, "patient.html")
def dashboard_page(request):
    return render(request, "dashboard.html")
def upload_page(request):
    return render(request, "upload.html")

def reports_page(request):
    return render(request, "reports.html")

def profile_page(request):
    return render(request, "profile.html")
def register_page(request):
    return render(request, "register.html")


def forgot_page(request):
    return render(request, "forgot.html")

def result_page(request):
    return render(request, "result.html")