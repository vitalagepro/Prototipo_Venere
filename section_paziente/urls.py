from django.urls import path
from . import views

urlpatterns = [
    path("Login/", views.LoginPaziente.as_view(), name="login-paziente"),
    path("Home_Page", views.HomePageRendering, name="home-page-paziente"),
    path("Profilo_Paziente", views.ProfiloPaziente, name="profilo-paziente")
] 