from django.urls import path

from . import views
urlpatterns=[
    path('travelspot/', views.TravelSpotsListView.as_view(), name='travel_spot'),
    path('travelspot/<slug:slug>', views.TravelSpotsRetrieveView.as_view(), name='travel_spot_single'),
    path('galery/', views.GaleryListView.as_view(), name='galery'),
    path('galery/<int:pk>', views.GaleryRetrieveView.as_view(), name='galery_single'),


]

