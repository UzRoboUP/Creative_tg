from django.shortcuts import render

from rest_framework import generics

from .models import TravelSpots, Galery
from .serializers import TravelSpotsSerializer, GalerySerializer
from .pagination import TwentyPagination, ThreePagination
# Create your views here.

class TravelSpotsListView(generics.ListAPIView):
    queryset=TravelSpots.objects.all()
    serializer_class=TravelSpotsSerializer
    # pagination_class=ThreePagination

class GaleryListView(generics.ListAPIView):
    queryset=Galery.objects.all()
    serializer_class=GalerySerializer
    # pagination_class=TwentyPagination