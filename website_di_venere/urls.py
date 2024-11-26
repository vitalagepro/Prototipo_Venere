from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="home-starting-page"),
    path("Medico/", include("section_medico.urls")),
    path("Paziente/", include("section_paziente.urls")),
]