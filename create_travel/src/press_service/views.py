from django.shortcuts import render
from rest_framework import generics
from app.pagination import ThreePagination

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from . import models
from . import serializers
# Create your views here.



class NewsListView(generics.ListAPIView):
    queryset=models.News.objects.all()
    serializer_class=serializers.NewsSerializer
    lookup_field = 'slug'
    # pagination_class=ThreePagination

    @method_decorator(cache_page(60 * 20))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class NewsRetrieveView(generics.RetrieveAPIView):
    queryset=models.News.objects.all()
    serializer_class=serializers.NewsSerializer
    lookup_field = 'slug'
