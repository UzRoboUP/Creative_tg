from modeltranslation.translator import TranslationOptions, register
from .models import Tags, News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','content')

@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ('title',)

    