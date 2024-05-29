from django.urls import path
from . import views
urlpatterns=[
    path('airtickets/', view=views.AirTicketAPIView.as_view(), name='airtickets'),
    path('hotel/', view=views.HotelAPIView.as_view(), name='hotel-list')
]