from django.urls import path
from . import views
urlpatterns=[
    path('airport/tickets/', view=views.AirTicketAPIView.as_view(), name='airtickets'),
    path('hotel/search', view=views.HotelAPIView.as_view(), name='hotel-list'),
    path('hotel/region_search/', view=views.AutoRegionSearchAPIView.as_view(), name='hotel_auto_search'),
    path('airport/code/', view=views.AirportCodeAPIView.as_view(), name='airport_code'),
    path('airport/create_booking/', view=views.AirportCreateBookingAPI.as_view(), name='airport_create_booking'),
    path('airport/booking_form/', view=views.AirportBookingFormAPI.as_view(), name='airport_booking_form'),
]

