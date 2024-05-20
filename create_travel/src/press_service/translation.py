from modeltranslation.translator import TranslationOptions, register

from .models import News

@register(News)
class GaleryTranslationOptions(TranslationOptions):
    fields = ('title','content',)
