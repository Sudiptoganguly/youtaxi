from rest_framework import serializers
from ..models import Car


class CreateCarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['addDate', 'removeDate', 'cityTaxi', 'licenseNumber', 'licenseAuthorizationDate', \
            'RegistrationTaxi', 'brand', 'model', 'typeOfvehicle', 'ownerNationalidentitynumber', \
            'ownerCredentialnumber','vtCard','buyDate','registrationDate','lastITVdate','lastMetropolitandate',\
            'lastVerificationdate', 'driverscredentialnumber', 'extraDriverscredentialnumberA','extraDriverscredentialnumberB',\
            'codeBluethootradio','pets','package','bluetoothRadio','solidarityTaxi','handicapedTaxi','zipCodeWorkCity']



class GetCarSerializersForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'addDate', 'removeDate', 'cityTaxi', 'licenseNumber', 'licenseAuthorizationDate', \
            'RegistrationTaxi', 'brand', 'model', 'typeOfvehicle', 'ownerNationalidentitynumber', \
            'ownerCredentialnumber','vtCard','buyDate','registrationDate','lastITVdate',\
            'lastMetropolitandate','lastVerificationdate', 'driverscredentialnumber', 'extraDriverscredentialnumberA',\
            'extraDriverscredentialnumberB','photoOftaxi','codeBluethootradio','pets','package','bluetoothRadio',\
            'solidarityTaxi','handicapedTaxi','zipCodeWorkCity','status','isDeleted']


class GetCarSerializersForOthers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'cityTaxi', 'licenseNumber', 'brand', 'model', 'typeOfvehicle', \
            'driverscredentialnumber','extraDriverscredentialnumberA','extraDriverscredentialnumberB',\
            'photoOftaxi','codeBluethootradio','pets','package','bluetoothRadio','solidarityTaxi','handicapedTaxi',\
            'zipCodeWorkCity','status','isDeleted']


class UpdateCarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['removeDate', 'cityTaxi',\
            'ownerCredentialnumber','vtCard','buyDate','registrationDate','lastITVdate','lastMetropolitandate',\
            'lastVerificationdate', 'driverscredentialnumber', 'extraDriverscredentialnumberA','extraDriverscredentialnumberB',\
            'photoOftaxi','codeBluethootradio','pets','package','bluetoothRadio','zipCodeWorkCity','solidarityTaxi','handicapedTaxi']