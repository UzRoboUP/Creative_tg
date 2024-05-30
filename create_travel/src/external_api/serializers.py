from rest_framework import serializers

# Hotel serializer
class GuestsSerializer(serializers.Serializer):
    adults=serializers.IntegerField(min_value=1, max_value=6)
    children=serializers.ListField(child=serializers.IntegerField(max_value=17), min_length=0, max_length=4)

class HotelSerializer(serializers.Serializer):
    region_id=serializers.IntegerField()
    checkin=serializers.DateField() #Check-in date, no later than 730 days from the day on which the request is made. required: True
    checkout=serializers.DateField() #Check-out date, no later than 30 days from checkin date. required: True
    guests=serializers.ListField(child=GuestsSerializer())  #Number of adult guests.required: True min_value: 1 max_value: 6                                                   
    language=serializers.CharField(max_length=2)
    currency=serializers.CharField(max_length=3, required=False)
    residency=serializers.CharField(max_length=2)

    def validate(self, attrs):
        data=super().validate(attrs)
        if data['checkin']>data['checkout']:
            raise serializers.ValidationError("checkin date must not be greater than checkout date")
        

# #AirticketSerializer

class AirTicketSerializer(serializers.Serializer):
    location_from=serializers.CharField()
    airport_from=serializers.CharField()
    location_to=serializers.CharField()
    airport_from=serializers.CharField()
    airline=serializers.CharField()
    departure_date=serializers.DateField()
    return_date=serializers.DateField()
    adults=serializers.IntegerField(min_value=1)
    children=serializers.IntegerField()
    babies=serializers.IntegerField()
    travel_status=serializers.CharField()
    baggage=serializers.BooleanField()
    business_trip=serializers.BooleanField(default=False)
    travel_type=serializers.BooleanField(default=False)



































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

