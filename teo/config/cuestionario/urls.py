from django.urls import path
from . import views

urlpatterns = [
    path("", views.hola, name="up"),
    path("f/", views.genai_request, name="gen"),
    path("results/", views.forms_request, name="r")
]