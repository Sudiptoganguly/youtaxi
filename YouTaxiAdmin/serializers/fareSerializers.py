from rest_framework import serializers
from ..models import FareModel


class CreateFareSerializer(serializers.ModelSerializer):
    class Meta:
        model = FareModel
        fields = ['baseFare', 'vehicleTypeId', 'fromTime', 'toTime', 'status']



class GetFareSerializer(serializers.ModelSerializer):
    class Meta:
        model = FareModel
        fields = ['id', 'baseFare', 'vehicleTypeId', 'fromTime', 'toTime', 'status']