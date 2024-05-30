from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.News
        fields=['title', 'content','slug','published_at','id','image','is_active']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

