from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
urlpatterns=[
    path('hotel/search/', view=views.HotelAPIView.as_view(), name='hotel-list'),
    path('hotel/region_search/', view=views.AutoRegionSearchAPIView.as_view(), name='hotel_auto_search'),
    path('hotel/hotel_page/', view=views.HotelPageAPIView.as_view(), name='hotel_page'),
    path('hotel/booking_form/', view=views.HotelBookingFormAPIView.as_view(), name='hotel_booking_form'),
    path('hotel/booking_form_finish/', view=views.HotelBookingFinishAPIView.as_view(), name="hotel_booking_form_finish"),
    path('hotel/booking_form_finish_status/', view=views.HotelBookingFinishStatusAPIView.as_view(), name='hotel_booking_finish_status'),
    
    path('airport/code/', view=views.AirportCodeAPIView.as_view(), name='airport_code'),
    path('airport/tickets/', view=views.AirTicketAPIView.as_view(), name='airtickets'),
    path('airport/create_booking/', view=views.AirportCreateBookingAPI.as_view(), name='airport_create_booking'),
    path('airport/create_booking_token/', view=views.AirportCreateBookingTokenAPI.as_view(), name='airport_create_booking_token'),
    path('airport/booking_form/', view=views.AirportBookingFormAPI.as_view(), name='airport_booking_form'),

]





