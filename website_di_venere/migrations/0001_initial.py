# Generated by Django 4.2.1 on 2024-01-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prenotazioni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giorno', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
                ('nome_prenotazione', models.CharField(max_length=255)),
                ('orario_prenotazione', models.CharField(max_length=255)),
            ],
        ),
    ]