import geopy.geocoders
from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="GeoLoc")


def get_latitude(region_name):
    return geolocator.geocode(region_name).latitude

def get_longitude(region_name):
    return geolocator.geocode(region_name).longitude   

