# Generated by Django 4.2.10 on 2024-05-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_galery_title_ru_galery_title_uz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelspots',
            name='image',
            field=models.ImageField(upload_to='image/travel-spots', verbose_name='изображение'),
        ),
    ]
