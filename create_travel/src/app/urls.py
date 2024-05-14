from django.urls import path

from . import views
urlpatterns=[
    path('travelspot/', views.TravelSpotsListView.as_view(), name='travel_spot'),
    path('galery/', views.GaleryListView.as_view(), name='galery'),
]

