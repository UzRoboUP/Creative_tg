from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

import uuid

# Create your models here.

class TravelSpots(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    title=models.CharField(max_length=40, verbose_name=_("Адрес"))
    image=models.ImageField(upload_to='image/travel_spots', verbose_name=_("изображение"))
    description=models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    in_uzbekistan=models.BooleanField(default=True, verbose_name=_("в узбекистане"))

    objects = models.Manager()


    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(TravelSpots, self).save(*args, **kwargs)
        return self


    class Meta:
        verbose_name = _("Место для путешествий")
        verbose_name_plural = _("Места для путешествий")
        db_table = 'travel_spot'


    def __str__(self):
        return self.title
    
class Galery(models.Model):
    title=models.CharField(max_length=30, verbose_name=_("заголовок"))
    image=models.ImageField(upload_to='image/galery', verbose_name=_("изображение"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    objects = models.Manager()


    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(TravelSpots, self).save(*args, **kwargs)
        return self


    class Meta:
        verbose_name = _("Галерея")
        verbose_name_plural = _("Галерея")
        db_table = 'galery_table'


    def __str__(self):
        return self.title