# Generated by Django 4.2.10 on 2024-09-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0009_remove_airticketorderhistory_carrier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airticketorderhistory',
            name='flights_group',
        ),
        migrations.AddField(
            model_name='airticketorderhistory',
            name='fligths_group',
            field=models.JSONField(blank=True, null=True, verbose_name='группа полетов'),
        ),
        migrations.AlterField(
            model_name='clientdeposit',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Заметка'),
        ),
        migrations.AlterField(
            model_name='clientspentdeposit',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Заметка'),
        ),
    ]
