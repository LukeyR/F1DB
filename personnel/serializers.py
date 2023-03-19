from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    driver_id = serializers.IntegerField(source='id')
    first_name = serializers.CharField(source='driver.first_name')
    last_name = serializers.CharField(source='driver.last_name')
    nationality = serializers.CharField(source='driver.nationality.country_code')
    class Meta:
        model = Driver
        fields = ("driver_id", "first_name", "last_name", "driver_abbreviation", "driver_number", "secondary_driver_number", "nationality")
        depth = 2

