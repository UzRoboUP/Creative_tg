from django_filters import rest_framework as filters
from .models import AirCityCodes

class AviaRegionFilter(filters.FilterSet):
    country=filters.CharFilter(lookup_expr='icontains')
    airport=filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=AirCityCodes
        fields=['code']