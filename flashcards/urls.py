from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = "flashcards"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flashcard_id>/", views.detail, name="detail")
]
