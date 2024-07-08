from django.shortcuts import render

from rest_framework import generics

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from .models import TravelSpots, Galery
from .serializers import TravelSpotsSerializer, GalerySerializer
from .pagination import TwentyPagination, ThreePagination
# Create your views here.


class TravelSpotsListView(generics.ListAPIView):
    queryset=TravelSpots.objects.all()
    serializer_class=TravelSpotsSerializer
    # pagination_class=ThreePagination
    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class TravelSpotsRetrieveView(generics.RetrieveAPIView):
    queryset=TravelSpots.objects.all()
    serializer_class=TravelSpotsSerializer
    lookup_field = 'slug'
    

class GaleryListView(generics.ListAPIView):
    queryset=Galery.objects.all()
    serializer_class=GalerySerializer
    # pagination_class=TwentyPagination

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class GaleryRetrieveView(generics.RetrieveAPIView):
    queryset=Galery.objects.all()
    serializer_class=GalerySerializer