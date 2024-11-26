# Generated by Django 4.2.1 on 2024-02-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]
