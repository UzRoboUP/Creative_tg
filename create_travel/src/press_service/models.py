from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

import uuid
# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название тегов"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(Tags, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Ярлык')
        verbose_name = _('Ярлык')
        db_table = 'tags'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    content = models.TextField(verbose_name=_("Содержание"))
    image = models.ImageField(upload_to='image/news', verbose_name=_("Картина"), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    published_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата публикации"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    tags = models.ManyToManyField(Tags, blank=True, related_name="tags", verbose_name=_("Теги"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(News, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Новости')
        verbose_name = _('Новости')
        db_table = 'news'
        indexes = [
            models.Index(fields=['title']),
        ]