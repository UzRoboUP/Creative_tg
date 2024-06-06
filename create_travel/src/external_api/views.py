from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .geolocatioon import get_latitude, get_longitude
import requests
from .serializers import HotelSerializer, AirTicketSerializer
from .models import HotelSearch


from core.settings.base import HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST, HOTEL_API_DETAIL_URL

class HotelAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSerializer
    # permission_classes=[IsAuthenticated,]
    def post(self,request):

        
        # serializer=HotelSerializer(request.data)
        # serializer.is_valid(raise_exception=True)
        
        try:
            region_name=request.data['region_name']
            longitude=get_longitude(region_name=region_name)
            latitude=get_latitude(region_name=region_name)

            hotel_search_data_by_location={"latitude":latitude, "longitude":longitude, "radius":4000, 
              "checkin":request.data["checkin"], "checkout":request.data["checkout"],
              "guests":request.data["guests"], "language":request.data["language"], 
              "currency":request.data["currency"], "residency":request.data["residency"]}
            
            # retieving avialible hotels
            hotel_search_response = requests.post(url=HOTEL_API_URL, auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), json=hotel_search_data_by_location)
        
            data = hotel_search_response.json()
           
            hotel_detail_list={}
            for hotel_id in range(len(data['data']['hotels'])):
                hotel=data['data']['hotels'][hotel_id]
                print(hotel)
                hotel_detail_request:dict={"id":hotel['id'], "language":request.data['language']}
                hotel_detail_list=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), json=hotel_detail_request)   
                data['data']['hotels'][hotel_id]['hotel_detail']=hotel_detail_list.json()

            return Response(data=data)
        except Exception:
            raise Response(hotel_search_response.status_code or hotel_detail_list.status_code)
        


class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketSerializer
    
    def post(self, request):
        data=request.data
        return Response(data=data)
