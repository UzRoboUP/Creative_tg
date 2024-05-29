from rest_framework import serializers

from .models import TravelSpots, Galery

class TravelSpotsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TravelSpots
        fields=['title', 'description', 'uuid', 'image', 'slug', 'in_uzbekistan',]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class GalerySerializer(serializers.ModelSerializer):

    class Meta:
        model=Galery
        fields=['id','title','image']

