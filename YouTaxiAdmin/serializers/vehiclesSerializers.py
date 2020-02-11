from rest_framework import serializers
from ..models import VehicleModel as Vehicle


class CreateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['VehicleType', 'driverId', 'AddDate', 'BuyDate', 'RegistrationDate',\
            'LastITVDate', 'LastMetroDate', 'ServicesToPerform', 'status']

class GetVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'VehicleType', 'driverId', 'AddDate', 'BuyDate', 'RegistrationDate',\
            'LastITVDate', 'LastMetroDate', 'ServicesToPerform', 'status', 'isDeleted']
