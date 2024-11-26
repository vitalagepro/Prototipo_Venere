from django.urls import path
from . import views

urlpatterns = [
    path("Login/", views.LoginMedico.as_view(), name="login-medico"),
    path("Home_Page", views.HomePageRendering, name="home-page"),
    path("Nuovo Assistito", views.NuovoAssistito, name="nuovo-assistito"),
    path("Archivio Pazienti", views.ArchivioPazienti, name="archivio-pazienti"),
    path("Archivio Pazienti/Cartella Paziente", views.Cartella_Paziente, name="cartella-paziente"),
    path("Calendario Prenotazioni", views.Calendario_Prenotazioni, name="calendario-prenotazioni"),
    path("Longevity", views.Longevity, name="longevity") 
] 

