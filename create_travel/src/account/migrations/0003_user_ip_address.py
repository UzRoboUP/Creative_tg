# Generated by Django 4.2.10 on 2024-06-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
    ]