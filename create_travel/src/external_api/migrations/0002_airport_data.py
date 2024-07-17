# Generated by Django 4.2.10 on 2024-07-17 20:07

from django.db import migrations
import pandas as pd


def create_lead_parsing_data(apps, schema_editor):
    AirCityCodes = apps.get_model('external_api', 'AirCityCodes')
    data = pd.read_excel('airport_data.xlsx')
    code = data['Code'].tolist()
    airport = data['Airport'].tolist()
    country = data['Country'].tolist()

    # Create the groups and items
    for entry in range(len(code)):
        code_value=code[entry]
        airport_value=airport[entry]
        country_value=country[entry]
        group, created = AirCityCodes.objects.get_or_create(code=code_value,
                                                            airport=airport_value,
                                                            country=country_value)


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(create_lead_parsing_data),
        ]