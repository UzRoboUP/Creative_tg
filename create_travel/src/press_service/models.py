from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

import uuid
# Create your models here.



class News(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    content = models.TextField(verbose_name=_("Содержание"))
    image = models.ImageField(upload_to='image/news', verbose_name=_("Картина"), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    published_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата публикации"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата изменения"))

    slug=models.SlugField(blank=True, null=True)
    
    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        self.updated_at = now()
        super(News, self).save(*args, **kwargs)
        return self
    
    def get_image_url(self):
        return self.image.url
    
    def photo(self): 
        """
        this method responsible for providing the image of shop at admin panel
        """
        return mark_safe(f'<img src = "{self.image.url}" width = "50"/>')
    

    class Meta:
        verbose_name_plural = _('Новости')
        verbose_name = _('Новости')
        db_table = 'news'
        indexes = [
            models.Index(fields=['title']),
        ]
