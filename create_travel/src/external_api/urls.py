from django.urls import path
from . import views
urlpatterns=[
    path('airtickets/', view=views.AirTicketAPIView.as_view(), name='airtickets'),
    path('hotel/', view=views.HotelAPIView.as_view(), name='hotel-list'),
    path('hotel_auto_search/', view=views.AutoRegionSearchAPIView.as_view(), name='hotel_auto_search'),
    path('airport_code/', view=views.AirportCodeAPIView.as_view(), name='airport_code'),
    path('airport_create_booking/', view=views.AirportCreateBookingAPI.as_view(), name='airport_create_booking'),
    path('airport_booking_form/', view=views.AirportBookingFormAPI.as_view(), name='airport_booking_form'),
]

