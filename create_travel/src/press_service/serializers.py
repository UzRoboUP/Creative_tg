from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.News
        fields="__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

