# Generated by Django 4.2.5 on 2023-10-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_serie_pub_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serierelation',
            name='relation',
            field=models.CharField(blank=True, choices=[('Secuela', 'Secuela'), ('Precuela', 'Precuela'), ('Historia Principal', 'Historia Principal'), ('Historia Paralela', 'Historia Paralela'), ('Historia Completa', 'Historia Completa'), ('Resumen', 'Resumen')], default=None, max_length=50, null=True),
        ),
    ]