from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

import requests
import json
import uuid

from .serializers import (HotelSerializer, AirTicketRequestSerializer, RegionAutoSearchSerializer, 
                          AirportCodeSerializer, AirportBookingSerializer, AirportBookingFormSerializer, 
                          HotelPageSerializer,HotelBookingFinishSerializer, HotelBookingSerializer, HotelBookingFinishStatusSerializer)
from .models import HotelSearch, AirCityCodes, PartnerOrderId
from .hashing import md5_time_hashing
from .filters import AviaRegionFilter
from account.models import User

from core.settings.base import (HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST, HOTEL_API_DETAIL_URL,
                                HOTEL_REGION_ID_URL,USER, PASSWORD_AIRTICKET, AGENCY,AIR_TICKET_URL,
                                LOGIN, LOGIN_PASSWORD, HOTEL_PAGE, HOTEL_BOOKING_FORM, HOTEL_BOOKING_FORM_FINISH, HOTEL_BOOKING_FINISH_STATUS)

class AutoRegionSearchAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=RegionAutoSearchSerializer
    
    def post(self, request):
        try:
            payload = json.dumps({
                    "query": request.data['region_name'],
                    "language": request.data['language']
                })
            headers = {
                    'Content-Type': 'application/json'
                }
            region_id_response=requests.request("POST", HOTEL_REGION_ID_URL, headers=headers, auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST),
                                data=payload)
            region_id_list=region_id_response.json()
            return Response(region_id_list)
        except Exception:
            return Response(data=region_id_list['error'],status=region_id_response.status_code)

class HotelAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSerializer
    # permission_classes=[IsAuthenticated,]

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
               
                # if len(hotel['rates'])==0:
                #     print(hotel['rates'])
                #     del hotel_list_respone['data']['hotels'][hotel_id]
                # else:

                hotel_detail_request=json.dumps({"id":hotel['id'], "language":request.data['language']})
                hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=hotel_detail_request, headers=headers) 
                hotel_list_respone['data']['hotels'][hotel_id]['hotel_detail']=hotel_detail_list.json()
            return Response(data=hotel_list_respone)
        except Exception as e:
            return Response(data=hotel_list_respone['error'], status=response.status_code)
    
class HotelPageAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelPageSerializer

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
            hotel_page_response = requests.request("POST", url=HOTEL_PAGE, data=payload, auth=(HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST),)
            
            hotel_page=hotel_page_response.json()
            hotel_detail_request=json.dumps({"id":request.data['id'], "language":request.data['language']})
            hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=hotel_detail_request, headers=headers) 
            hotel_page['data']['hotels'][0]['hotel_detail']=hotel_detail_list.json()
    
            return Response(data=hotel_page, status=hotel_page_response.status_code)
        except Exception:
            return Response(data=hotel_page_response['error'], status=hotel_page_response.status_code)

class HotelBookingFormAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingSerializer

    def post(self, request):
        # getting ip_address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # saving partner_order_id in model
        partner_order_id=uuid.uuid4()
        user=User.objects.filter(id=self.request.user.id).first()

        obj, bool=PartnerOrderId.objects.get_or_create(partner_order_id=partner_order_id, user=user)
        # sending post request to the url to retrieve nessesary data
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
            hotel_booking_form=requests.post(url=HOTEL_BOOKING_FORM,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=payload, headers=headers)
            data=hotel_booking_form.json()
            return Response(data=data)
        except Exception:
            return Response(data=data['error'])
        

class HotelBookingFinishAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishSerializer
    
    def post(self, request):
        payload=json.dumps(request.data)
        headers = {
                        'Content-Type': 'application/json'
                    }
        try:
            hotel_booking_form_finish=requests.post(url=HOTEL_BOOKING_FORM_FINISH,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=payload, headers=headers)
            data=request.data
            return Response(data=data)
        except:
            return Response(data=data['error'])
        
    

class HotelBookingFinishStatusAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishStatusSerializer
    

    def post(self, request):
        payload=json.dumps(request.data)
        headers = {
                        'Content-Type': 'application/json'
                    }
        try:
            hotel_booking_form_finish_finish=requests.post(url=HOTEL_BOOKING_FINISH_STATUS,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=payload, headers=headers)
            data=hotel_booking_form_finish_finish.json()
            return Response(data=data)
        except Response:
            return Response(data=data['error'])
    
    
class HotelBookingFinishCancelation(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelBookingFinishStatusSerializer
    
    def post(self, request):
        return request.data


class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketRequestSerializer
    # permission_classes=[IsAuthenticated,]

    def post(self, request):
        time=str(request.data['context']['time'])
        hash=md5_time_hashing(agency=AGENCY, password=PASSWORD_AIRTICKET, time=time, user=USER)

        payload=json.dumps({
            "context": {
                "agency":AGENCY,
                "user":USER,
                "time":request.data['context']['time'],
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
           
            if len(data['respond']['token']):
                token_payload=json.dumps({            
                    "context": {
                        "agency":AGENCY,
                        "user":10659,
                        "time":request.data['context']['time'],
                        "hash":hash,
                        "locale":request.data['context']['locale'],
                        "time":time,
                        "command": "SEARCHRESULT",
                    },
                    "parameters":{
                        "token": data['respond']['token']
                    }
                })
                token_response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=token_payload)
                token_data=token_response.json()
                
                return Response(data=token_data, status=token_response.status_code)
            else:
                return Response(data=data['respond']['messages'], status=response.status_code)
        except Exception:
            return Response(data=token_data, status=response.status_code)
            

class AirportCodeAPIView(generics.ListAPIView):
    queryset=AirCityCodes.objects.all()
    serializer_class=AirportCodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=AviaRegionFilter


class AirportCreateBookingAPI(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingSerializer
    def post(self, request):
        time=str(request.data['context']['time'])
        hash=md5_time_hashing(agency=AGENCY, password=PASSWORD_AIRTICKET, time=time, user=USER)

        payload=json.dumps({
        
            "context": {
                "agency":AGENCY,
                "user":USER,
                "time":request.data['context']['time'],
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "SELECTFLIGHT",
            },
            "parameters":request.data['parameters']

        })

        response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
        data=response.json()
        if len(data['respond']['token']):
            token_payload=json.dumps({            
                "context": {
                    "agency":AGENCY,
                    "user":USER,
                    "time":request.data['context']['time'],
                    "hash":hash,
                    "locale":request.data['context']['locale'],
                    "time":time,
                    "command": "SELECTRESULT",
                },
                "parameters":{
                    "token": data['respond']['token']
                }
            })
            token_response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=token_payload)
            return Response(data=token_response.json(), status=token_response.status_code)
        else:
            return Response(data=data['respond']['messages'], status=response.status_code)
        

class AirportBookingFormAPI(generics.GenericAPIView):
    queryset=None
    serializer_class=AirportBookingFormSerializer
    def post(self, request):
        time=str(request.data['context']['time'])
        hash=md5_time_hashing(agency=AGENCY, password=PASSWORD_AIRTICKET, time=time, user=USER)

        payload=json.dumps({
        
            "context": {
                "agency":AGENCY,
                "user":USER,
                "time":request.data['context']['time'],
                "hash":hash,
                "locale":request.data['context']['locale'],
                "time":time,
                "command": "CREATEBOOKING",
            },
            "parameters":request.data['parameters']

        })
        response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=payload)
        data=response.json()
        if len(data['respond']['token']):
            token_payload=json.dumps({            
                "context": {
                    "agency":AGENCY,
                    "user":USER,
                    "time":request.data['context']['time'],
                    "hash":hash,
                    "locale":request.data['context']['locale'],
                    "time":time,
                    "command": "CREATERESULT",
                },
                "parameters":{
                    "token": data['respond']['token']
                }
            })
            token_response=requests.post(url=AIR_TICKET_URL,auth=(LOGIN,LOGIN_PASSWORD), data=token_payload)
            return Response(data=token_response.json(), status=token_response.status_code)
        else:
            return Response(data=data['respond']['messages'], status=response.status_code)
    