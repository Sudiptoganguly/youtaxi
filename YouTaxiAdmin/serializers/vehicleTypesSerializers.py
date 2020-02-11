from rest_framework import serializers
from ..models import VehicleType


class CreateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['name', 'baseFare']


class GetVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id','name', 'baseFare', 'status', 'isDeleted', 'date']

