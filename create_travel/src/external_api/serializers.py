from rest_framework import serializers
from . import models

# Hotel serializer

class RegionAutoSearchSerializer(serializers.Serializer):
    region_name=serializers.CharField(max_length=255)
    language=serializers.CharField(max_length=2)

class GuestsSerializer(serializers.Serializer):
    adults=serializers.IntegerField(min_value=1, max_value=6)
    children=serializers.ListField(child=serializers.IntegerField(max_value=17), min_length=0, max_length=4)

class HotelSerializer(serializers.Serializer):
    
    checkin=serializers.DateField() #Check-in date, no later than 730 days from the day on which the request is made. required: True
    checkout=serializers.DateField() #Check-out date, no later than 30 days from checkin date. required: True
    language=serializers.CharField(max_length=2)
    guests=serializers.ListField(child=GuestsSerializer())  #Number of adult guests.required: True min_value: 1 max_value: 6                                                   
    region_id=serializers.IntegerField()
    currency=serializers.CharField(max_length=3, required=False)
    residency=serializers.CharField(max_length=2)

    def validate(self, attrs):
        data=super().validate(attrs)
        if data['checkin']>data['checkout']:
            raise serializers.ValidationError("checkin date must not be greater than checkout date")


        
# #AirticketSerializer
class AviaLocationSerializer(serializers.Serializer):
    code=serializers.CharField(max_length=3)
    name=serializers.CharField(max_length=255)


class RouteSerializer(serializers.Serializer):
    date=serializers.DateField()
    locationBegin=AviaLocationSerializer()
    locationEnd=AviaLocationSerializer()

class SeatsSerializer(serializers.Serializer):
    count=serializers.IntegerField(min_value=1)
    passengerType= serializers.CharField(max_length=255)

class AirTicketParametrSerializer(serializers.Serializer):
    route=serializers.ListField(child=RouteSerializer())
    seats=serializers.ListField(child=SeatsSerializer(), max_length=6)
    serviceClass=serializers.CharField(max_length=100)
    skipConnected=serializers.CharField(max_length=255, required=False)
    eticketsOnly=serializers.BooleanField(default=True)
    mixedVendors=serializers.BooleanField(default=True)
    preferredAirlines=serializers.ListField(required=False)

class AirTicketContextSerializer(serializers.Serializer):
    time=serializers.DateTimeField()
    locale=serializers.CharField(max_length=2)


class AirTicketRequestSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirTicketParametrSerializer()

class AirportCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.AirCityCodes
        fields=['country','airport','code']





























# # TranseferSerializer
# class TransferSerializer(serializers.Serializer):
#     daparture_city=serializers.CharField()
#     arrivial_city=serializers.CharField()
#     where_from=serializers.CharField()
#     where_to=serializers.CharField()
#     time=serializers.DateField()
#     submission_time=serializers.DateTimeField()
#     number_of_passenger=serializers.IntegerField()
#     number_of_luggage=serializers.IntegerField()
#     baby_chair=serializers.BooleanField(default=False)
#     stop_along_way=serializers.BooleanField(default=False)

# # RentCarSerializer

# class RentCarAdditionalInfoSerilaizer():
#     vehicle_type=serializers.CharField()
#     clutch_type=serializers.CharField()
#     full_name=serializers.CharField()
#     email=serializers.EmailField()
#     contact_number=serializers.CharField()
#     gps=serializers.BooleanField(default=False)
#     winter_tire=serializers.BooleanField(default=False)

# class RentCarSerilizer(serializers.Serializer):
#     pickup_location=serializers.CharField()
#     date_of_receiving=serializers.DateField()
#     receipt_time=serializers.TimeField()
#     return_date=serializers.DateField()
#     return_time=serializers.TimeField()
#     number_of_passenger=serializers.IntegerField()
#     number_of_luggage=serializers.IntegerField()
#     baby_chair=serializers.BooleanField(default=False)
#     stop_along_way=serializers.BooleanField(default=False)
#     additional_info=RentCarAdditionalInfoSerilaizer()

