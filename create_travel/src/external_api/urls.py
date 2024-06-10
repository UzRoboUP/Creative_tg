from django.urls import path
from . import views
urlpatterns=[
    path('airtickets/', view=views.AirTicketAPIView.as_view(), name='airtickets'),
    path('hotel/', view=views.HotelAPIView.as_view(), name='hotel-list'),
    path('hotel_auto_search/', view=views.AutoRegionSearchAPIView.as_view(), name='hotel_auto_search')

]