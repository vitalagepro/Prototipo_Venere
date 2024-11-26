from django.db import models

# Create your models here.
class Prenotazioni(models.Model):
    giorno = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    nome_prenotazione = models.CharField(max_length=255)
    orario_prenotazione = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_prenotazione

    
class ApiKeys(models.Model):
    Api = models.CharField(max_length=500)
    ApiKeys = models.CharField(max_length=500)