from rest_framework import serializers
from ..models import User


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullName', 'countryCode', 'phoneNo', 'userLocation', 'language', 'deviceIMEI', 'deviceHash']

