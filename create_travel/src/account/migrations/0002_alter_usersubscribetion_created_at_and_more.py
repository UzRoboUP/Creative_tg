# Generated by Django 4.2.10 on 2024-05-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscribetion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='usersubscribetion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
    ]
