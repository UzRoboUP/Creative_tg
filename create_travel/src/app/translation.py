from modeltranslation.translator import TranslationOptions, register
from .models import TravelSpots, Galery


@register(TravelSpots)
class TravelSpotsTranslationOptions(TranslationOptions):
    fields = ('title','description')



    