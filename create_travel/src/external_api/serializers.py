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

class HotelPageSerializer(serializers.Serializer):
    
    id=serializers.CharField(max_length=255, min_length=1)
    checkin=serializers.DateField() #Check-in date, no later than 730 days from the day on which the request is made. required: True
    checkout=serializers.DateField() #Check-out date, no later than 30 days from checkin date. required: True
    language=serializers.CharField(max_length=2)
    guests=serializers.ListField(child=GuestsSerializer())  #Number of adult guests.required: True min_value: 1 max_value: 6                                                   
    currency=serializers.CharField(max_length=3, required=False)
    residency=serializers.CharField(max_length=2)

    def validate(self, attrs):
        data=super().validate(attrs)
        if data['checkin']>data['checkout']:
            raise serializers.ValidationError("checkin date must not be greater than checkout date")

class PartnerOrderIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PartnerOrderId
        fields=['partner_order_id']
        
class HotelBookingSerializer(serializers.Serializer):
    book_hash=serializers.CharField(min_length=1, max_length=256)
    language=serializers.CharField(min_length=2, max_length=2)
 

class HotelOrderBookingFinishPartnerSerializer(serializers.Serializer):
    partner_order_id=serializers.CharField(min_length=1, max_length=256)

class HotelOrderBookingFinishPaymentTypeSerializer(serializers.Serializer):
    PAYMENT_TYPE_CHOICE=(
        ('now', 'now'),
        ('hotel','hotel'),
        ('deposit','deposit')
    )
    type=serializers.ChoiceField(choices=PAYMENT_TYPE_CHOICE)
    amount=serializers.DecimalField(max_digits=10, decimal_places=10)
    currency_code=serializers.CharField(min_length=3, max_length=3)


class HotelOrderBookingFinishGuestSerializer(serializers.Serializer):
    first_name=serializers.CharField(min_length=1, max_length=32)
    last_name=serializers.CharField(min_length=1, max_length=32)
    is_child=serializers.BooleanField(default=False)
    age=serializers.IntegerField(required=False)


class HotelOrderBookingFinishRoomSerializer(serializers.Serializer):
    guests=serializers.ListField(child=HotelOrderBookingFinishGuestSerializer())


class HotelOrderBookingFinishUserSerializer(serializers.Serializer):
    comment=serializers.CharField(min_length=1, max_length=32, required=False)
    email=serializers.EmailField()
    phone=serializers.CharField(min_length=1, max_length=32)



class HotelOrderBookingFinishSupplierDataSerializer(serializers.Serializer):
    first_name_original=serializers.CharField(min_length=1, max_length=32)
    last_name_original=serializers.CharField(min_length=1, max_length=32)
    phone=serializers.CharField(min_length=1, max_length=32)
    email=serializers.EmailField()

class HotelBookingHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HotelOrderHistory
        fields=[ 
                'order_id',
                'order_cost',
                'partner_order_id',
                'guests',
                'check_in',
                'check_out',
                'hotel_id',
                'hotel_name',
                'room_name',
                'country',
                'city',
                'free_cancelation']

class HotelBookingFinishSerializer(serializers.Serializer):
    arrival_datetime=serializers.DateTimeField(required=False)
    language=serializers.CharField(max_length=2)
    partner=HotelOrderBookingFinishPartnerSerializer()  
    payment_type=HotelOrderBookingFinishPaymentTypeSerializer()
    rooms=serializers.ListField(child=HotelOrderBookingFinishRoomSerializer())
    user=HotelOrderBookingFinishUserSerializer()
    supplier_data=HotelOrderBookingFinishSupplierDataSerializer()
    history_list=HotelBookingHistoryListSerializer()

class ContractDatasSerializer(serializers.Serializer):
    agreement_number=serializers.CharField(max_length=255)
    overpay=serializers.DecimalField(max_digits=10, decimal_places=2)
    overdue_debt=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_non_ref_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_ref_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)

class ContractDetailsSerializer(serializers.Serializer):
    credit_limit=serializers.DecimalField(max_digits=10, decimal_places=2)
    deposit=serializers.DecimalField(max_digits=10, decimal_places=2)
    max_booking_price=serializers.DecimalField(max_digits=10, decimal_places=2)
    overdue_debt=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_non_ref_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_ref_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    unpaid_orders_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    contract_overpay=serializers.DecimalField(max_digits=10, decimal_places=2)
    reporting_currency=serializers.CharField(max_length=255)
   

class HotelFinancialInformationSerializer(serializers.Serializer):
    contract_datas=serializers.ListField(child=ContractDatasSerializer())
    contract=ContractDetailsSerializer()

class PartnerOrderIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PartnerOrderId
        fields='__all__'

class HotelBookingFinishStatusSerializer(serializers.Serializer):
    partner_order_id=serializers.CharField(min_length=1, max_length=256)

class ClientDepositSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.ClientDeposit
        fields='__all__'

class ClientSpentDepositSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.ClientSpentDeposit
        fields='__all__'

################################################################################

class AirTicketTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.AirTicketStatusToken
        fields='__all__'
                

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
    serviceClass=serializers.CharField(min_length=0,max_length=100)
    skipConnected=serializers.CharField(min_length=0,max_length=255, required=False)
    eticketsOnly=serializers.BooleanField(default=True)
    mixedVendors=serializers.BooleanField(default=True)
    preferredAirlines=serializers.ListField(required=False)

class AirTicketContextSerializer(serializers.Serializer):
    # time=serializers.DateTimeField()
    locale=serializers.CharField(max_length=2)


class AirTicketRequestSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirTicketParametrSerializer()

class AirportCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.AirCityCodes
        fields=['country','airport','code']
  

# booking section of airport
class FlightSerializer(serializers.Serializer):
    token=serializers.IntegerField()

class FlightsSerializer(serializers.Serializer):
    flight=serializers.ListField(child=FlightSerializer())

class ItinerarySerializer(serializers.Serializer):
    token=serializers.IntegerField()
    flights=FlightsSerializer()

class ItinerariesSerializer(serializers.Serializer):
    itinerary=serializers.ListField(child=ItinerarySerializer())

class FlightGroupSerializer(serializers.Serializer):
    token=serializers.IntegerField()
    itineraries=ItinerariesSerializer()

class FlightsGroupSerializer(serializers.Serializer):
    flightGroup=serializers.ListField(child=FlightGroupSerializer())

class AirportCreateBookingParametrSerializer(serializers.Serializer):
    flightsGroup=FlightsGroupSerializer()
    token=serializers.CharField(max_length=255)

class AirportBookingSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirportCreateBookingParametrSerializer()

class AirportBookingTokenAPISerializer(serializers.Serializer):
    token=serializers.CharField(min_length=32, max_length=32)

class AirportCreateBookingTokenSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirportBookingTokenAPISerializer()
    

# creating Booking Proccess in AirTicket
class AirportCustomerSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    email=serializers.EmailField()
    countryCode=serializers.CharField(max_length=255)
    areaCode=serializers.CharField(max_length=255)
    phoneNumber=serializers.CharField(max_length=255)

class AirportPassengerCitizenShipSerializer(serializers.Serializer):
    code=serializers.CharField(max_length=4)
    name=serializers.CharField(max_length=255)

class AirportPassportDetailSerializer(serializers.Serializer):
    firstName=serializers.CharField(max_length=255)
    lastName=serializers.CharField(max_length=255)
    middleName=serializers.CharField(max_length=255)
    citizenship=AirportPassengerCitizenShipSerializer()
    issued=serializers.CharField(max_length=255)
    expired=serializers.DateTimeField()
    number=serializers.CharField(max_length=255)
    type=serializers.CharField(max_length=255)
    birthday=serializers.DateField()
    gender=serializers.CharField(max_length=255)


class AirportPassengerDetailSerializer(serializers.Serializer):
    passport=AirportPassportDetailSerializer()
    type=serializers.CharField(max_length=255)
    phoneType=serializers.CharField(max_length=255)
    phoneNumber=serializers.CharField(max_length=255)
    countryCode=serializers.CharField(max_length=255)
    areaCode=serializers.CharField(max_length=255)
    email=serializers.EmailField()
    isEmailRefused=serializers.BooleanField(default=False)
    isEmailAbsent=serializers.BooleanField(default=False)

class AirportSinglePassengerSerializer(serializers.Serializer):
    passenger=serializers.ListField(child=AirportPassengerDetailSerializer())

class AirportHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AirTicketOrderhistory
        fields='__all__'
class AirportBookingFormParameterSerializer(serializers.Serializer):
    fligthsGroup=FlightsGroupSerializer()
    token=serializers.CharField(max_length=255)
    customer=AirportCustomerSerializer()
    passengers=AirportSinglePassengerSerializer()

class AirportBookingFormSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirportBookingFormParameterSerializer()
    history_list=AirportHistoryListSerializer()

class AirportBookingStatusSerializer(serializers.Serializer):
    context=AirTicketContextSerializer()
    parameters=AirportBookingTokenAPISerializer()

