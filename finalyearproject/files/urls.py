from django.urls import path
from .views import upload_scan
from .views import create_account


urlpatterns = [
    # ???
    path('', upload_scan, name="images"),
    path('upload_scan/',upload_scan, name = "images" ),
    path('create_account/', create_account)
]