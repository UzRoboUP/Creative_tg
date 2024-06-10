from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


import requests
import json
from .serializers import HotelSerializer, AirTicketSerializer, RegionAutoSearchSerializer
from .models import HotelSearch


from core.settings.base import (HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST, HOTEL_API_DETAIL_URL,
                                HOTEL_REGION_ID_URL)

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
        except Exception as e:
            return Response(region_id_response.status_code or e)

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
                if len(hotel['rates'])==0:
                    del hotel_list_respone['data']['hotels'][hotel_id]
                else:
                    hotel_detail_request=json.dumps({"id":hotel['id'], "language":request.data['language']})
                    hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), data=hotel_detail_request, headers=headers)   
                    hotel_list_respone['data']['hotels'][hotel_id]['hotel_detail']=hotel_detail_list.json()

            return Response(data=hotel_list_respone)
        except Exception as e:
            return Response(response.status_code)
      
class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketSerializer
    
    def post(self, request):
        data=request.data
        return Response(data=data)
