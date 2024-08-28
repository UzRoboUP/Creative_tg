# Generated by Django 4.2.10 on 2024-08-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0004_alter_airticketorderhistory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airticketorderhistory',
            name='location_begin',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='airticketorderhistory',
            name='location_end',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='airticketorderhistory',
            name='ticket_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Цена билета'),
        ),
        migrations.AddField(
            model_name='airticketorderhistory',
            name='travel_duration',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='partnerorderid',
            name='item_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Идентификатор товара'),
        ),
    ]
