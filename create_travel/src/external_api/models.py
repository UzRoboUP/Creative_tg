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
    country = models.CharField(max_length=255)
    airport=models.CharField(max_length=255)
    code =models.CharField(max_length=3)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    def __str__(self) -> str:
        return f"{self.created_at}"

    class Meta:
        verbose_name_plural = 'airport_code_list'
        verbose_name = 'airport_code_list'
        # db_table = 'airport_code_list'
        indexes = [
            models.Index(fields=['country','airport','code']),
        ]
    

class ClientDeposit(models.Model):
    class Meta:
        verbose_name_plural = _('Баланс клиента')
        verbose_name = _('Баланс клиента')
        # db_table = 'client_balance'
        indexes = [
            models.Index(fields=['user',]),
        ]    
    id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True, verbose_name=_("Пользователь"))
    amount=models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True, verbose_name=_("Количество"))
    description=models.TextField(null=True, blank=True, verbose_name=_("Заметка"))

    def save(self, *args, **kwargs):
        self.updated_at = now()

        super(ClientDeposit, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return f"{self.created_at}"
    
class ClientSpentDeposit(models.Model):
    class Meta:
        verbose_name_plural = _('Депозит, потраченный клиентом')
        verbose_name = _('Депозит, потраченный клиентом')
        # db_table = 'client_spent_deposit'
        indexes = [
            models.Index(fields=['user',]),
        ]    
    
    id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True, verbose_name=_("Пользователь"))
    amount=models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True, verbose_name=_("Количество"))
    description=models.TextField(null=True, blank=True, verbose_name=_("Заметка"))
    
    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(ClientSpentDeposit, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return f"{self.created_at}"

class PartnerOrderId(models.Model):
    class Meta:
        verbose_name_plural = _('Идентификатор партнерского заказа')
        verbose_name = _('Идентификатор партнерского заказа')
        # db_table = 'partner_order_id'
        indexes = [
            models.Index(fields=['partner_order_id', 'order_id',]),
        ]
    id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True, verbose_name=_("Пользователь"))
    
    partner_order_id=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Идентификатор заказа партнера"))
    item_id=models.IntegerField(blank=True, null=True, verbose_name=_("Идентификатор товара"))
    order_id=models.IntegerField(blank=True, null=True, verbose_name=_("Идентификатор заказа"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
          
    def __str__(self) -> str:
        return f"{self.created_at}"

class HotelOrderHistory(models.Model):
    class Meta:
        verbose_name_plural = _('История заказов в отеле')
        verbose_name = _('История заказов в отеле')
        # db_table = 'hotel_order_history'
        indexes = [
            models.Index(fields=['order_id','id']),
        ]
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True, verbose_name=_("Пользователь"))
    order_id=models.IntegerField(blank=True, null=True, verbose_name=_("Идентификатор заказа"))
    order_cost=models.FloatField(blank=True, null=True, verbose_name=_("Цена заказа"))
    guests=models.JSONField(blank=True, null=True, verbose_name=_("Полное имя гостя"))
    hotel_id=models.CharField(max_length=255, null=True, blank=True,verbose_name= _("Идентификатор отеля"))
    check_in=models.DateField(auto_now_add=True, blank=True, null=True, verbose_name=_("Регистрироваться"))
    check_out=models.DateField(auto_now_add=True, blank=True, null=True, verbose_name=_("Проверить"))
    hotel_name=models.CharField(max_length=255, blank=True, verbose_name=_("Название отеля"))
    room_name=models.CharField(max_length=255, blank=True, verbose_name=_("Название комнаты"))
    country=models.CharField(max_length=255, blank=True, verbose_name=_("Страна"))
    city=models.CharField(max_length=255, blank=True ,verbose_name=_("Город"))
    free_cancelation=models.DateTimeField(null=True, blank=True, verbose_name=_("Бесплатная отмена"))
    partner_order_id=models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Идентификатор заказа партнера"))

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(HotelOrderHistory, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return f"{self.created_at}"
    
class AirTicketOrderhistory(models.Model):
    class Meta:
        verbose_name_plural = _('История заказов в авиабилета')
        verbose_name = _('История заказов в авиабилета')
        # db_table = 'air_ticket_history'
    
    id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    user=models.ForeignKey(to=User, 
                           on_delete=models.SET_NULL,
                           blank=True, 
                           null=True, 
                           verbose_name=_("Пользователь"))
    fligths_group=models.JSONField(blank=True, null=True, verbose_name=_("группа полетов"))

    def __str__(self) -> str:
        return f"{self.created_at}"

class AirTicketStatusToken(models.Model):
    class Meta:
        verbose_name_plural = _('Статус авиабилета')
        verbose_name = _('Статус авиабилета')
        # db_table = 'air_ticket_status'
    
    id = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))
    user=models.ForeignKey(to=User, on_delete=models.SET_NULL ,blank=True, null=True, verbose_name=_("Пользователь"))
    token=models.CharField(max_length=255,null=True, blank=True,verbose_name=_("Токен"))

    def __str__(self) -> str:
        return f"{self.created_at}"    
    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(AirTicketStatusToken, self).save(*args, **kwargs)
        return self.user.username

