from django_filters import rest_framework as filters
from .models import AirCityCodes, PartnerOrderId

class AviaRegionFilter(filters.FilterSet):
    country=filters.CharFilter(lookup_expr='icontains')
    airport=filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=AirCityCodes
        fields=['code']


class HotelPartnerIdFilter(filters.FilterSet):
    class Meta:
        model=PartnerOrderId
        fields=['order_id']
        
