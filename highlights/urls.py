from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = "highlights"
urlpatterns = [
    # path("", views.index, name="index"),
    path("upload/", views.upload_file, name="upload_file"),
    path("process-upload/", views.handle_uploaded_file, name="process_upload"),
]
