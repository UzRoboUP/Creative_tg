from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

import uuid

# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False, unique=True,)
    username=models.CharField(max_length=255, unique=True, blank=True, null=True)
    user=models.CharField(max_length=255, verbose_name=_("Имя"))
    email=models.EmailField(verbose_name=_("Электронная почта"), blank=True,)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    def save(self, *args, **kwargs):
        self.username = self.username.upper() if self.username else self.username
        self.updated_at = now()
        super(User, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return self.username