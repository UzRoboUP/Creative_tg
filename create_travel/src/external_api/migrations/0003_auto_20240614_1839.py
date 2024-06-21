# Generated by Django 4.2.10 on 2024-06-14 18:39
import pandas as pd

from django.db import migrations

def create_code_airport(apps, schema_editor):
    AirCityCodes = apps.get_model('external_api', 'AirCityCodes')

    
    data_airport = pd.read_excel('airport_codes.xlsx')
    code=data_airport[0:]['Code']
    airport=data_airport[0:]['Airport']
    country=data_airport[0:]['Country']
    for number_in_line in range(len(code)):
        AirCityCodes.objects.get_or_create(code=code[number_in_line], country=country[number_in_line], 
                                                                        airport=airport[number_in_line])
        

class Migration(migrations.Migration):
    

    dependencies = [
        ('external_api', '0002_aircitycodes'),
    ]

    operations = [
        migrations.RunPython(create_code_airport),
    ]
