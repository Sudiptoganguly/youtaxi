from rest_framework import serializers
from YouTaxiDriver.models import Driver
from YouTaxiUser.models import User


class CreateDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['firstName', 'lastName', 'phoneNo', 'email', 'preferedHour', 'cityOfWork', 'LinkedTaxiLicense']



class GetAllDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'firstName', 'lastName', 'phoneNo', 'email', 'status']



class GetDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'firstName', 'lastName', 'phoneNo', 'email', 'address', \
            'landLineNumber', 'dateOfBirth', 'placeOfBirth', 'createDate', 'removeDate',\
            'DNIAddress', 'DNICityAddress', 'ExpirationDateCirculationPermit', 'Regularschedule', \
            'LinkedTaxiLicense', 'RegistrationTaxiLinked', 'language', 'AdminNotices', \
            'AdminNotes', 'profileImg', 'PhotoDNI', 'CredintialPhoto', 'driverScore', 'status']



class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'countryCode', 'phoneNo', 'email', 'createDate', \
            'status', 'isDeleted', 'dateOfBirth', 'gender', 'address', 'language', \
            'favoriteTaxis', 'taxisBlocked', 'adminNotices']