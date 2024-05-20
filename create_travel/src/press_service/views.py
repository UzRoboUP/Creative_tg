from django.shortcuts import render
from rest_framework import generics
from app.pagination import ThreePagination

from . import models
from . import serializers
# Create your views here.



class NewsListView(generics.ListAPIView):
    queryset=models.News.objects.all()
    serializer_class=serializers.NewsSerializer
    lookup_field = 'slug'
    # pagination_class=ThreePagination

class NewsRetrieveView(generics.RetrieveAPIView):
    queryset=models.News.objects.all()
    serializer_class=serializers.NewsSerializer
    lookup_field = 'slug'
