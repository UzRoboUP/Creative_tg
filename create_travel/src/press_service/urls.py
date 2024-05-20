from django.urls import path
from . import views

urlpatterns=[
    path('news/', view=views.NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>', view=views.NewsRetrieveView.as_view(), name='news_list'),

]