from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/accounts/',
        include('backend.accounts.urls')
    ),
    
    path(
        "api/",
        include("backend.patients.urls")
    ),
    path(
        'api/',
        include('backend.reports.urls')
    ),
    path(
        'api/dashboard/',
        include('backend.dashboard.urls')),
    
    path("", include("frontend.urls"))

]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
