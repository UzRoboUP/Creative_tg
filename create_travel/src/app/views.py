from django.shortcuts import render

from rest_framework import generics

from .models import TravelSpots, Galery
from .serializers import TravelSpotsSerializer, GalerySerializer
from .pagination import TenPagination, TwentyPagination
# Create your views here.

class TravelSpotsListView(generics.ListAPIView):
    queryset=TravelSpots.objects.all()
    serializer_class=TravelSpotsSerializer
    pagination_class=TenPagination

class GaleryListView(generics.ListAPIView):
    queryset=Galery.objects.all()
    serializer_class=GalerySerializer
    pagination_class=TwentyPagination