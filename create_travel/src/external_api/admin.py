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



{

  "context": {
    "locale": "en"
  },

  
  "parameters": {
    "flightsGroup": {
      "flightGroup": [
        {
          "token": 0,
          "itineraries": {
            "itinerary": [
              {
                "token": 0,
                "flights": {
                  "flight": [
                    {
                      "token": 0
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    },
    "token": "24af10df02f210b362003285a6a7b768",
    "customer": {
             "name": "Khatamov Ravshan Tolib" ,
             "email": "asas@gmail.com" ,
             "countryCode": "1" ,
             "areaCode": "234" ,
             "phoneNumber": "5432123" 
    },

    "passengers": {
      "passenger": [
        {
          "passport": {
            "firstName": "string",
            "lastName": "string",
            "middleName": "string",
            "citizenship": {
              "code": "stri",
              "name": "string"
            },
            "issued": "string",
            "expired": "2024-08-31T06:10:11.213Z",
            "number": "string",
            "type": "string",
            "birthday": "2024-08-31",
            "gender": "string"
          },
          "type": "string",
          "phoneType": "string",
          "phoneNumber": "string",
          "countryCode": "string",
          "areaCode": "string",
          "email": "user@example.com",
          "isEmailRefused": false,
          "isEmailAbsent": false
          
    "passengers": {
      "passenger": [
                {
                   "passport": {
                      "firstName": "Ravshan" ,
                      "lastName": "Khatamov" ,
                      "middleName": "Tolib" ,
                      "citizenship": {
                         "code": "RU" ,
                         "name": "Russian Federation"
                      } ,
                      "issued": "" ,
                      "expired": "2029-08-31T11:06+05:00" ,
                      "number": "12 34 321234" ,
                      "type": "INTERNAL" ,
                      "birthday": "2000-04-02T00:00+05:00" ,
                      "gender": "MALE"
                   } ,
                   "type": "ADULT" ,
                   "phoneType": "HOME_PHONE" ,
                   "phoneNumber": "3123454" ,
                   "countryCode": "1" ,
                   "areaCode": "234" ,
                   "email": "ravsha@gmail.com" ,
                   "isEmailRefused": false ,
                   "isEmailAbsent": false
                }
             ]
    }
  },
  "history_list": {
    "flights_group": {}
  }
}

{
  "context": {
    "locale": "st"
  },
  "parameters": {
    "flightsGroup": {
      "flightGroup": [
        {
          "token": 0,
          "itineraries": {
            "itinerary": [
              {
                "token": 0,
                "flights": {
                  "flight": [
                    {
                      "token": 0
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    },
    "token": "string",
    "customer": {
      "name": "string",
      "email": "user@example.com",
      "countryCode": "string",
      "areaCode": "string",
      "phoneNumber": "string"
    },
    "passengers": {
      "passenger": [
        {
          "passport": {
            "firstName": "string",
            "lastName": "string",
            "middleName": "string",
            "citizenship": {
              "code": "stri",
              "name": "string"
            },
            "issued": "string",
            "expired": "2024-08-31T06:10:11.213Z",
            "number": "string",
            "type": "string",
            "birthday": "2024-08-31",
            "gender": "string"
          },
          "type": "string",
          "phoneType": "string",
          "phoneNumber": "string",
          "countryCode": "string",
          "areaCode": "string",
          "email": "user@example.com",
          "isEmailRefused": false,
          "isEmailAbsent": false
        }
      ]
    }
  },
  "history_list": {
    "flights_group": "string"
  }
}