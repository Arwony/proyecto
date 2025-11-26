from django.urls import path
from . import views
from django.urls import register_converter
import uuid

class UUIDConverter:
    regex = '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'
    def to_python(self, value):
        return uuid.UUID(value)
    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path("", views.main, name="main"),
    path("prompt", views.hola, name="up"),
    path("f/", views.genai_request, name="gen"),
    path("results/", views.forms_request, name="r"),
    path("about/", views.about, name="about"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/<int:id>", views.user_profile, name="profile"),
    path("guardar_formulario/", views.guardar_formulario, name="guardar_formulario"),
    path("formulario/<uuid:form_id>/", views.formulario_detail, name="ver_formulario"),
    path("formulario/<uuid:form_id>/toggle_public/", views.toggle_public, name="toggle_public"),
]
