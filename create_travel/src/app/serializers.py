from rest_framework import serializers

from .models import TravelSpots, Galery

class TravelSpotsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TravelSpots
        fields='__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class GalerySerializer(serializers.ModelSerializer):

    class Meta:
        model=Galery
        fields='__all__'

