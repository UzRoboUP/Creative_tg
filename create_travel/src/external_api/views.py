from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from django.db.models import Sum, Count
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from rest_framework.decorators import action
# from django.views.decorators.vary import vary_on_cookie, vary_on_headers

import requests
import json
import uuid

from .serializers import (HotelSerializer, AirTicketRequestSerializer, RegionAutoSearchSerializer,
                          AirportCodeSerializer, AirportBookingSerializer, AirportBookingFormSerializer,
                          HotelPageSerializer, HotelBookingFinishSerializer, HotelBookingSerializer,
                          HotelBookingFinishStatusSerializer, AirportCreateBookingTokenSerializer,
                          AirportBookingStatusSerializer, ClientDepositSerializer, AirTicketTokenSerializer,
                         HotelBookingHistoryListSerializer, ClientSpentDepositSerializer, AirportHistoryListSerializer,PartnerOrderIdSerializer, HotelFinancialInformationSerializer)
from .models import (AirCityCodes, PartnerOrderId, ClientDeposit,AirTicketOrderhistory,
                     AirTicketStatusToken, HotelOrderHistory, ClientSpentDeposit)
from .hashing import md5_time_hashing
from .filters import AviaRegionFilter, HotelPartnerIdFilter
from account.models import User

from .utils import current_time

from core.settings.base import (HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST, HOTEL_API_DETAIL_URL,
                                HOTEL_REGION_ID_URL,AIRTICKET_USER, PASSWORD_AIRTICKET, AGENCY,AIR_TICKET_URL,
                                LOGIN, LOGIN_PASSWORD, HOTEL_PAGE, HOTEL_BOOKING_FORM, HOTEL_BOOKING_FORM_FINISH, 
                                HOTEL_BOOKING_FINISH_STATUS, HOTEL_BOOKING_CANCELLATION,HOTEL_CONTRACT_DATA_INFORMATION)

class ClientDepositListView(generics.ListAPIView):
    queryset=ClientDeposit.objects.all()
    serializer_class=ClientDepositSerializer
    permission_classes=[IsAuthenticated,]
    
    def get_queryset(self):
        queryset=ClientDeposit.objects.filter(user__id=self.request.user.id)
        return queryset
    
class ClientSpentDepositListView(generics.ListAPIView):
    queryset=ClientSpentDeposit.objects.all()
    serializer_class=ClientSpentDepositSerializer
    permission_classes=[IsAuthenticated,]
    
    def get_queryset(self):
        queryset=ClientSpentDeposit.objects.filter(user__id=self.request.user.id)
        return queryset
    
class AutoRegionSearchAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=RegionAutoSearchSerializer
    permission_classes=[IsAuthenticated]
   
    def post(self, request):

        try:
            payload = json.dumps({
                    "query": request.data['region_name'],
                    "language": request.data['language']
                })
            headers = {
                    'Content-Type': 'application/json'
                }
            region_id_response=requests.request("POST", HOTEL_REGION_ID_URL, 
                                                headers=headers, 
                                                auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST),
                                data=payload)
            region_id_list=region_id_response.json()
            return Response(region_id_list)
        except Exception:
            return Response(data=region_id_list['error'],status=region_id_response.status_code)

 
class HotelFinancialInformationAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelFinancialInformationSerializer
    permission_classes=[IsAuthenticated]
   
    def get(self, request):

        try:

            region_id_response=requests.request("GET", HOTEL_CONTRACT_DATA_INFORMATION, 
                                                auth=(HOTEL_KEY_ID,
                                                      HOTEL_KEY_TOKEN_TEST),)
            region_id_list=region_id_response.json()
            return Response(region_id_list)
        except Exception:
            return Response(data=region_id_list['error'],status=region_id_response.status_code)

class HotelAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            payload = json.dumps({
                        "checkin": request.data['checkin'],
                        "checkout": request.data['checkout'],
                        "language": request.data['language'],
                        "guests": request.data['guests'],
                        "region_id": request.data['region_id'],
                        "currency": request.data['currency'],
                        "residency": request.data['residency'],
                        "hotels_limit": 20

                    })
            headers = {
                    'Content-Type': 'application/json'
                }
            response = requests.request("POST", url=HOTEL_API_URL, data=payload, auth=(HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST),)
            hotel_list=response.json()
    
            hotel_list_respone=response.json()
            for hotel_id in range(len(hotel_list['data']['hotels'])):
                hotel=hotel_list['data']['hotels'][hotel_id]
                hotel_detail_request=json.dumps({"id":hotel['id'], 
                                                 "language":request.data['language']})
                hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,
                                                auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), 
                                                data=hotel_detail_request, headers=headers) 
                hotel_list_respone['data']['hotels'][hotel_id]['hotel_detail']=hotel_detail_list.json()
            return Response(data=hotel_list_respone)
        except Exception as e:
            return Response(data=hotel_list_respone['error'], status=response.status_code)
    
class HotelPageAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelPageSerializer
    permission_classes=[IsAuthenticated]
  
    def post(self, request):
        try:
            payload = json.dumps({
                        "id": request.data['id'],
                        "checkin": request.data['checkin'],
                        "checkout": request.data['checkout'],
                        "language": request.data['language'],
                        "guests": request.data['guests'],
                        "currency": request.data['currency'],
                        "residency": request.data['residency'],
                    })
            headers = {
                    'Content-Type': 'application/json'
                }
            hotel_page_response = requests.request("POST", 
                                                   url=HOTEL_PAGE, 
                                                   data=payload, 
                                                   auth=(HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST),)
            
            hotel_page=hotel_page_response.json()
            hotel_detail_request=json.dumps({"id":request.data['id'], 
                                             "language":request.data['language']})
            hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), 
                                            data=hotel_detail_request, 
                                            headers=headers) 
            hotel_page['data']['hotels'][0]['hotel_detail']=hotel_detail_list.json()
    
            return Response(data=hotel_page, 
                            status=hotel_page_response.status_code)
        except Exception:
            return Response(data=hotel_page['error'], 
                                status=hotel_page_response.status_code)

class HotelBookingFormAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        # getting ip_address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # saving partner_order_id in model
        partner_order_id=uuid.uuid4()

        try: 
            payload = json.dumps({
                            "partner_order_id": str(partner_order_id),
                            "book_hash": request.data['book_hash'],
                            "user_ip": ip,
                            "language": request.data['language'],   
                        })
            headers = {
                        'Content-Type': 'application/json'
                    }
            hotel_booking_form=requests.post(url=HOTEL_BOOKING_FORM,
                                             auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), 
                                             data=payload, 
                                             headers=headers)
            data=hotel_booking_form.json()

            # it is for saving pertner order id in our data base to get information about status of room booking
            if data['data'] and data['status']=="ok":
                PartnerOrderId.objects.create(user=self.request.user, 
                                              partner_order_id=data['data']['partner_order_id'], 
                                              order_id=data['data']['order_id'],
                                              item_id=data['data']['item_id'])
            return Response(data=data)
        except Exception:
            return Response(data=data['error'])
        
class HotelBookingFinishAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        data=dict(request.data)
        booking_data=data.pop("history_list")
    
        payload=json.dumps(data)
   
        headers = {
                        'Content-Type': 'application/json'
                    }
        
        try:
            hotel_booking_form_finish=requests.post(url=HOTEL_BOOKING_FORM_FINISH,
                                                    auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), 
                                                    data=payload, 
                                                    headers=headers)
            
            data=hotel_booking_form_finish.json()
            if data['status']=='ok':
                HotelOrderHistory.objects.create(user=self.request.user, **booking_data)
            return Response(data=data)
        except:
            return Response(data=data['error'])
        
class HotelBookingFinishStatusAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        payload=json.dumps(request.data)
        headers = {
                        'Content-Type': 'application/json'
                    }
        try:
            hotel_booking_form_finish_finish=requests.post(url=HOTEL_BOOKING_FINISH_STATUS,
                                                           auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), 
                                                           data=payload, 
                                                           headers=headers)
            data=hotel_booking_form_finish_finish.json()
            return Response(data=data)
        except Response:
            return Response(data=data['error'])
    
    
class HotelBookingFinishCancelation(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        payload=json.dumps(request.data)
        headers = {
                        'Content-Type': 'application/json'
                    }
        try:
            hotel_booking_form_finish_cancel=requests.post(url=HOTEL_BOOKING_CANCELLATION,
                                                           auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST),
                                                             data=payload, 
                                                             headers=headers)
            data=hotel_booking_form_finish_cancel.json()
            return Response(data=data)
        except Response:
            return Response(data=data['error'])
    
class HotelBookedHistoryListView(generics.ListAPIView):
    queryset = HotelOrderHistory.objects.all()
    serializer_class = HotelBookingHistoryListSerializer

    def get_queryset(self,):
        queryset=HotelOrderHistory.objects.filter(user=self.request.user)
        return queryset
    
class HotelPartnerOrderIdAPIView(generics.ListAPIView):
    queryset=PartnerOrderId.objects.all()
    serializer_class=PartnerOrderIdSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=HotelPartnerIdFilter
    permission_classes=[IsAuthenticated]

    def get_queryset(self,):
        queryset=PartnerOrderId.objects.filter(user=self.request.user)
        return queryset
    

##################################################################################################################################
##########################################STOP!IF YOU DO NOT HAVE BUSINESS WITH AVIA TICKET#######################################
##################################################################################################################################

class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketRequestSerializer
    permission_classes=[IsAuthenticated,]


    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))
        
        payload=json.dumps({
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "SEARCHFLIGHTS",
            },
            "parameters":request.data['parameters']
        })
        try:
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()
           
            if data['respond']['token']:
                token_payload=json.dumps({            
                    "context": {
                        "agency":int(AGENCY),
                        "user":int(AIRTICKET_USER),
                        "hash":hash,
                        "locale":request.data['context']['locale'],
                        "time":time,
                        "command": "SEARCHRESULT",
                    },
                    "parameters":{
                        "token": data['respond']['token']
                    }
                })
                try:
                    token_response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=token_payload)
                    token_data=token_response.json()
                    return Response(data=token_data, status=token_response.status_code)
                except Exception:
                    return Response(data=token_data['respond']['messages'], status=response.status_code)   
        except Exception:
            return Response(data=data, status=response.status_code)  
            

class AirportCodeAPIView(generics.ListAPIView):
    queryset=AirCityCodes.objects.all()
    serializer_class=AirportCodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=AviaRegionFilter
    permission_classes=[IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AirportCreateBookingAPI(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), 
                              password=PASSWORD_AIRTICKET, 
                              time=time, 
                              user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "SELECTFLIGHT",
            },
            "parameters":request.data['parameters']

        })
        try:

            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()
            
            return Response(data=data, status=response.status_code)
        
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)


class AirportCreateBookingTokenAPI(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportCreateBookingTokenSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))
        token_payload=json.dumps({            
                "context": {
                    "agency":int(AGENCY),
                    "user":int(AIRTICKET_USER),
                    "hash":hash,
                    "locale":request.data['context']['locale'],
                    "time":time,
                    "command": "SELECTRESULT",
                },
                "parameters": request.data['parameters']
                
            })
        try:
            token_response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=token_payload)
            token_data=token_response.json()
            return Response(data=token_data, status=token_response.status_code)
        except Exception:
            return Response(data=token_data['respond']['messages'], status=token_response.status_code)
    

class AirportBookingFormAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = AirportBookingFormSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
     
        time = current_time()
        hash = md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))
        history_data = request.data.get('history_list')
        locale = request.data.get('context', {}).get('locale')
        parameters = request.data.get('parameters')
        
        payload = {
            "context": {
                "agency": int(AGENCY),
                "user": int(AIRTICKET_USER),
                "hash": hash,
                "locale": locale,
                "time": time,
                "command": "CREATEBOOKING",
            },
            "parameters": parameters
        }
        try:
            response = requests.post(url=AIR_TICKET_URL, auth=(LOGIN, LOGIN_PASSWORD), json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()

            if data['respond']['token']:
                token_payload = {
                    "context": {
                        "agency": int(AGENCY),
                        "user": int(AIRTICKET_USER),
                        "hash": hash,
                        "locale": locale,
                        "time": time,
                        "command": "CREATERESULT",
                    },
                    "parameters": {
                        "token": data['respond']['token']
                    }
                }
                try:
                    token_response = requests.post(url=AIR_TICKET_URL, auth=(LOGIN, LOGIN_PASSWORD), json=token_payload)
                    token_response.raise_for_status()
                    token_data = token_response.json()

                    if token_data['respond']['status'] == 'BOOKING':
                        AirTicketStatusToken.objects.create(user=self.request.user, token=token_data['respond']['token'])
                        AirTicketOrderhistory.objects.create(user=self.request.user, **history_data)
                        return Response(data=token_data, status=token_response.status_code)
                    elif token_data['respond']['status'] != 'BOOKING':
                        return Response(data=token_data, status=response.status_code) 
                except Exception as e:
                        return Response(data=token_data, status=response.status_code) 
                    
      
        except Exception:
            return Response(data=data, status=response.status_code)  
            

class AirportBookingStatusView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "DISPLAYSTATUS",
            },
            "parameters":request.data['parameters']
        })


        try:
                
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()

            return Response(data=data, status=response.status_code)
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)
            
class AirportBookingCancellation(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "CANCELBOOKING",
            },
            "parameters":request.data['parameters']
        })


        try:
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()

            return Response(data=data, status=response.status_code)
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)
        
class AirportBookingDisplayOrder(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "DISPLAYORDER",
            },
            "parameters":request.data['parameters']
        })
        try:
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()

            return Response(data=data, status=response.status_code)
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)
        
class AirportBookingDisplayCreate(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "DISPLAYCREATE",
            },
            "parameters":request.data['parameters']
        })
        try:
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()

            return Response(data=data, status=response.status_code)
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)

class AirportBookingDisplayTickets(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingStatusSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        time=current_time()
        hash=md5_time_hashing(agency=int(AGENCY), password=PASSWORD_AIRTICKET, time=time, user=int(AIRTICKET_USER))

        payload=json.dumps({
        
            "context": {
                "agency":int(AGENCY),
                "user":int(AIRTICKET_USER),
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "DISPLAYTICKETS",
            },
            "parameters":request.data['parameters']
        })
        try:
            response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
            data=response.json()

            return Response(data=data, status=response.status_code)
        except Exception:
            return Response(data=data['respond']['messages'], status=response.status_code)


class AirTicketTokenListView(generics.ListAPIView):
    queryset=AirTicketStatusToken.objects.all()
    serializer_class=AirTicketTokenSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user).order_by('-created_at')
        return queryset

class AirTicketTokenCreateView(generics.CreateAPIView):
    queryset=AirTicketStatusToken.objects.all()
    serializer_class=AirTicketTokenSerializer
    permission_classes=[IsAuthenticated]


class AirTicketTokenUpdateView(generics.UpdateAPIView):
    queryset=AirTicketStatusToken.objects.all()
    serializer_class=AirTicketTokenSerializer
    permission_classes=[IsAuthenticated,]
    
class AirTicketTokenRetrieveView(generics.RetrieveAPIView):
    queryset=AirTicketStatusToken.objects.all()
    serializer_class=AirTicketTokenSerializer
    permission_classes=[IsAuthenticated,]

class AirTicketHistoryAPIView(generics.ListAPIView):
    queryset=AirTicketOrderhistory.objects.all()
    serializer_class=AirportHistoryListSerializer
    permission_classes=[IsAuthenticated,]


