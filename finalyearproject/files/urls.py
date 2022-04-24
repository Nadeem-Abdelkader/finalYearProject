from django.urls import path
from .views import upload_scan


urlpatterns = [
    path('upload_scan/',upload_scan, name = "images" )
]