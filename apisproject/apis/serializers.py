from rest_framework import serializers
from .models import Location


class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        lookup_fields = 'location'
