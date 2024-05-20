from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from  . import models
# Register your models here.

@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ["title", "created_at","photo"]
    list_per_page = 20
    readonly_fields = ['photo']

