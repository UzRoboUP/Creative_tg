# Generated by Django 4.2.10 on 2024-09-06 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0005_hotelorderhistory_partner_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airticketorderhistory',
            old_name='fligths_group',
            new_name='flights_group',
        ),
    ]
