from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

import uuid
# Create your models here.

class HotelSearch(models.Model):
    region_id=models.IntegerField()
    checkin=models.DateField()
    checkout=models.DateField()
    guests=models.JSONField()
    language=models.CharField(max_length=2)
    currency=models.CharField(max_length=3)
    residency=models.CharField(max_length=2)


class CityName(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, verbose_name=_("Имя"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))


    class Meta:
        verbose_name_plural = _('Города')
        verbose_name = _('Город')
        db_table = 'city'
        indexes = [
            models.Index(fields=['name']),
        ]