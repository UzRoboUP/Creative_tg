# Generated by Django 4.2.10 on 2024-09-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0004_alter_airticketorderhistory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelorderhistory',
            name='partner_order_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Идентификатор заказа партнера'),
        ),
    ]