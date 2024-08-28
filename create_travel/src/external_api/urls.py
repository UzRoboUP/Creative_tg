from django.urls import path
from . import views

urlpatterns=[
    path('client/deposit/', view=views.ClientDepositListView.as_view(),  name='client_deposit'),
    path('client/deposit/spent/', view=views.ClientSpentDepositListView.as_view(),  name='client_deposit_spent'),
    
    path('hotel/search/', view=views.HotelAPIView.as_view(), name='hotel-list'),
    path('hotel/region_search/', view=views.AutoRegionSearchAPIView.as_view(), name='hotel_auto_search'),
    path('hotel/hotel_page/', view=views.HotelPageAPIView.as_view(), name='hotel_page'),
    path('hotel/booking_form/', view=views.HotelBookingFormAPIView.as_view(), name='hotel_booking_form'),
    path('hotel/booking_form_finish/', view=views.HotelBookingFinishAPIView.as_view(), name="hotel_booking_form_finish"),
    path('hotel/booking_form_finish_status/', view=views.HotelBookingFinishStatusAPIView.as_view(), name='hotel_booking_finish_status'),
    path('hotel/booking_history/', view=views.HotelBookedHistoryListView.as_view(), name='hotel_booking_history'),
    path('hotel/partner_order_id/', view=views.HotelPartnerOrderIdAPIView.as_view(), name='hotel_partner_order_id'),
    path('hotel/contract/data/',view=views.HotelFinancialInformationAPIView.as_view(), name="hotel_finance_info"),
    
    path('airport/code/', view=views.AirportCodeAPIView.as_view(), name='airport_code'),
    path('airport/tickets/', view=views.AirTicketAPIView.as_view(), name='air_ticket'),
    path('airport/create_booking/', view=views.AirportCreateBookingAPI.as_view(), name='airport_create_booking'),
    path('airport/create_booking_token/', view=views.AirportCreateBookingTokenAPI.as_view(), name='airport_create_booking_token'),
    path('airport/booking_form/', view=views.AirportBookingFormAPI.as_view(), name='airport_booking_form'),
    path('airport/booking/status/', view=views.AirportBookingStatusView.as_view(), name='booking_status'),
    path('airport/booking/displaycreate/', view=views.AirportBookingDisplayOrder.as_view(), name='booking_display_order'),
    path('airport/booking/displayorder/', view=views.AirportBookingDisplayCreate.as_view(), name='booking_display_create'),
    path('airport/booking/cancellation/', view=views.AirportBookingCancellation.as_view(), name='booking_cancellation'),
    path('airport/booking/displaytickets/', view=views.AirportBookingDisplayTickets.as_view(), name='booking_display_tickets'),
    path('airport/booking/history/', view=views.AirTicketHistoryAPIView.as_view(), name='booking_history_list'),

    
]





