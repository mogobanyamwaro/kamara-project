from django.shortcuts import render
from .models import Location
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import locationSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def calculate_distance_view(request):
    # the plumber
    if request.method == 'GET':
        customer_location = Location.objects.all()
        serializer = locationSerializer(customer_location, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # the agent
        geolocator = Nominatim(user_agent='locations')
        ip = '14.137.168.0'
        kisii = '41.89.196.0'
        country, city, lat, lon = get_geo(ip)

        location = geolocator.geocode(city)
        l_lat = lat
        l_long = lon
        pointA = (l_lat, l_long)
        # the customer
        country2, city2, lat2, lon2 = get_geo(kisii)
        pointB = (lat2, lon2)
        distance = round(geodesic(pointA, pointB).km, 2)

        serializerPost = locationSerializer(
            data={"location": city['city'], "distance": distance})
        if serializerPost.is_valid():
            serializerPost.save()
            return Response(serializerPost.data, status=status.HTTP_201_CREATED)
        return Response(serializerPost.errors, status=status.HTTP_400_BAD_REQUEST)
