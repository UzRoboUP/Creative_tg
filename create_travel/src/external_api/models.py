from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

import uuid
from account.models import User

# Create your models here.

class HotelSearch(models.Model):
    region_id=models.IntegerField()
    checkin=models.DateField()
    checkout=models.DateField()
    guests=models.JSONField()
    language=models.CharField(max_length=2)
    currency=models.CharField(max_length=3)
    residency=models.CharField(max_length=2)


class AirCityCodes(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    country = models.CharField(max_length=255)
    airport=models.CharField(max_length=255)
    code =models.CharField(max_length=3)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    def __str__(self) -> str:
        return self.airport +" " + self.code

    class Meta:
        verbose_name_plural = 'airport_code_list'
        verbose_name = 'airport_code_list'
        db_table = 'airport_code_list'
        indexes = [
            models.Index(fields=['country','airport','code']),
        ]


class PartnerOrderId(models.Model):
    partner_order_id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    
    def __str__(self) -> str:
        return self.user.username + self.partner_order_id
    

    