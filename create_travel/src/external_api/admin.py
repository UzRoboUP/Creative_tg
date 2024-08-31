from django.contrib import admin
from .models import ClientDeposit, HotelOrderHistory, AirTicketStatusToken, ClientSpentDeposit, PartnerOrderId, AirTicketOrderhistory
# Register your models here.


class ClientDepositAdmin(admin.ModelAdmin):
    search_fields=['user__username',]
    list_display=['user','amount', 'created_at']
    list_display_links=['user','amount', 'created_at']

class ClientSpentDepositAdmin(admin.ModelAdmin):
    search_fields=['user__username',]
    list_display=['user','amount', 'created_at']
    list_display_links=['user','amount', 'created_at']

class HotelBookingHistoryAdmin(admin.ModelAdmin):
    search_fields=['user__username', 'hotel_name']
    list_display=['user', 'hotel_name', 'order_cost','check_in', 'check_out']
    list_display_links=['user', 'hotel_name', 'order_cost','check_in', 'check_out']

class AirTicketTokenAdmin(admin.ModelAdmin):
    search_fields=['user__username', 'token']
    list_display=['user', 'token', 'created_at']
    list_display_links=['user', 'token', 'created_at']
admin.site.register(ClientDeposit, ClientDepositAdmin)
admin.site.register(ClientSpentDeposit, ClientSpentDepositAdmin)
admin.site.register(HotelOrderHistory, HotelBookingHistoryAdmin)
admin.site.register(AirTicketStatusToken, AirTicketTokenAdmin)
admin.site.register(PartnerOrderId)
# admin.site.register(AirTicketOrderhistory)



