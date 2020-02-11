from rest_framework import serializers
from ..models import Driver


# class CreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Driver
#         fields = ['firstName', 'lastName', 'phoneNo', 'email', \
#             'address', 'CredintialPhoto', 'preferedHour']



# class GetDriverSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Driver
#         fields = ['id', 'firstName', 'lastName', 'phoneNo', 'email', 'address', \
#             'landLineNumber', 'dateOfBirth', 'placeOfBirth', 'createDate', 'removeDate',\
#             'DNIAddress', 'DNICityAddress', 'ExpirationDateCirculationPermit', 'Regularschedule', \
#             'LinkedTaxiLicense', 'RegistrationTaxiLinked', 'language', 'AdminNotices', \
#             'AdminNotes', 'profileImg', 'PhotoDNI', 'CredintialPhoto']



# class UpdateDriverByAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Driver




class DriverLoginMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['countryCode', 'phoneNo', 'LinkedTaxiLicense', 'RegistrationTaxiLinked']