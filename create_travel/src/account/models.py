from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

import uuid

# Create your models here.


class UserSubscription(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False, unique=True,)

    username=models.CharField(max_length=255, verbose_name=_("Имя"))
    email=models.EmailField(verbose_name=_("Электронная почта"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    objects = models.Manager()


    def save(self, *args, **kwargs):
        self.username = self.username.upper() if self.username else self.username
        self.updated_at = now()
        super(UserSubscription, self).save(*args, **kwargs)
        return self


    class Meta:
        verbose_name = _("Подписаться")
        verbose_name_plural = _("Подписаться")
        db_table = 'subscribe'
        indexes = [
            models.Index(fields=['username',]),
        ]

    def __str__(self):
        return self.username