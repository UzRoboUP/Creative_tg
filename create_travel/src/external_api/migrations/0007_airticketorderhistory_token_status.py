# Generated by Django 4.2.10 on 2024-09-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0006_rename_fligths_group_airticketorderhistory_flights_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='airticketorderhistory',
            name='token_status',
            field=models.IntegerField(blank=True, null=True, verbose_name='статус токена'),
        ),
    ]
