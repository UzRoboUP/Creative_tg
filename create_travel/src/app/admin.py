from django.contrib import admin
from .models import TravelSpots, Galery
from modeltranslation.admin import TranslationAdmin
# Register your models here.

# @admin.register(TravelSpots)
# class TravelSpotsAdmin(TranslationAdmin):
#     list_display=('title',)



@admin.register(TravelSpots)
class TravelSpotsAdmin(TranslationAdmin):
    list_display = ["title", "created_at","photo"]

    class Media:
        js=(
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http.//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',

        )
        css={
            'screen':('modeltranslation/css/tabbed_translation_fields.css')
        }
    readonly_fields = ['photo']
    list_per_page = 20
@admin.register(Galery)

class GaleryAdmin(TranslationAdmin):
    list_display = ["title", "created_at","photo"]
    list_per_page = 20
    readonly_fields = ['photo']



