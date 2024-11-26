from django.contrib import admin

# Register your models here.
from .models import Prenotazioni, ApiKeys

admin.site.register(Prenotazioni)
admin.site.register(ApiKeys)
