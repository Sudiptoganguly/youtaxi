'''
        view.py
   @ Author  Kuntal
   @ Company Nat It Solved Pvt Ltd
   @ version  0.1
   @date      10/12/2019
'''

# Django Import
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
import json
from django.contrib.auth import authenticate

# Model Import
from .models import Driver

# Serializers Import
from .serializers import DriverSerializers


# Rest Framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes


def DemoDriver(request):
    return HttpResponse("From Driver")


@api_view(['POST'])
def UpdateDriverByAdmin(request, slug):
    try:
        DriverObject = Driver.objects.get(id=slug)
        try:
            createDate = request.data['createDate']
            DriverObject.createDate = createDate
        except:
            createDate = ''
        try:
            removeDate = request.data['removeDate']
            DriverObject.removeDate = removeDate
        except:
            removeDate = ''
        try:
            Regularschedule = request.data['Regularschedule']
            DriverObject.Regularschedule = Regularschedule
        except:
            Regularschedule = ''
        try:
            language = request.data['language']
            DriverObject.language = language
        except:
            language = ''
        try:
            TravelCommission = request.data['TravelCommission']
            DriverObject.TravelCommission = TravelCommission
        except:
            TravelCommission = ''
        try:
            CommissionChargeCards = request.data['CommissionChargeCards']
            DriverObject.CommissionChargeCards = CommissionChargeCards
        except:
            CommissionChargeCards = ''
        try:
            BankCurrentAccount = request.data['BankCurrentAccount']
            DriverObject.BankCurrentAccount = BankCurrentAccount
        except:
            BankCurrentAccount = ''
        try:
            AdminNotes = request.data['AdminNotes']
            DriverObject.AdminNotes = AdminNotes
        except:
            AdminNotes = ''
        try:
            profileImg = request.data['profileImg']
            DriverObject.profileImg = profileImg
        except:
            profileImg = ''
        try:
            PhotoDNI = request.data['PhotoDNI']
            DriverObject.PhotoDNI = PhotoDNI
        except:
            PhotoDNI = ''
        try:
            CredintialPhoto = request.data['CredintialPhoto']
            DriverObject.CredintialPhoto = CredintialPhoto
        except:
            CredintialPhoto = ''
        DriverObject.save()
        
        ack = 5
        status = 200
        success = True
        msg = "Updated Succefully"

    except Exception as e:
        print("Fail To Update : ", e)
        ack = 1
        status = 400
        success = False
        msg = "Fail To Updated"

    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)



@api_view(['POST'])
def UpdateDriver(request, slug):
    try:
        Id = slug
        DriverObject = Driver.objects.get(email="driver1@mail.com")
        try:
            landLineNumber = request.POST['landLineNumber']
        except:
            landLineNumber = ''
        try:
            address = request.POST['address']
        except:
            address = ''
        try:
            dateOfBirth = request.POST['dateOfBirth']
        except:
            dateOfBirth = ''
        try:
            placeOfBirth = request.POST['placeOfBirth']
        except:
            placeOfBirth = ''
        try:
            DNIAddress = request.POST['DNIAddress']
        except:
            DNIAddress = ''
        try:
            DNICityAddress = request.POST['DNICityAddress']
        except:
            DNICityAddress = ''
        try:
            ExpirationDateCirculationPermit = request.POST['ExpirationDateCirculationPermit']
        except:
            ExpirationDateCirculationPermit = ''
        try:
            Regularschedule = request.POST['Regularschedule']
        except:
            Regularschedule = ''
        try:
            LinkedTaxiLicense = request.POST['LinkedTaxiLicense']
        except:
            LinkedTaxiLicense = ''
        try:
            RegistrationTaxiLinked = request.POST['RegistrationTaxiLinked']
        except:
            RegistrationTaxiLinked = ''
        try:
            TravelCommission = request.POST['TravelCommission']
        except:
            TravelCommission = ''
        try:
            CommissionChargeCards = request.POST['CommissionChargeCards']
        except:
            CommissionChargeCards = ''
        try:
            BankCurrentAccount = request.POST['BankCurrentAccount']
        except:
            BankCurrentAccount = ''
        try:
            AdminNotices = request.POST['AdminNotices']
        except:
            AdminNotices = ''
        try:
            AdminNotes = request.POST['AdminNotes']
        except:
            AdminNotes = ''
        try:
            profileImg = request.FILES['profileImg']
        except:
            profileImg = ''
        try:
            CredintialPhoto = request.FILES['CredintialPhoto']
        except:
            CredintialPhoto = ''
        try:
            PhotoDNI = request.POST['PhotoDNI']
        except:
            PhotoDNI = ''

        if landLineNumber != '':
            DriverObject.landLineNumber = landLineNumber
        if address != '':
            DriverObject.address = address
        if dateOfBirth != '':
            DriverObject.dateOfBirth  = dateOfBirth
        if placeOfBirth != '':
            DriverObject.placeOfBirth = placeOfBirth
        if DNIAddress != '':
            DriverObject.DNIAddress = DNIAddress
        if DNICityAddress != '':
            DriverObject.DNICityAddress = DNICityAddress
        if ExpirationDateCirculationPermit != '':
            DriverObject.ExpirationDateCirculationPermit = ExpirationDateCirculationPermit
        if Regularschedule != '':
            DriverObject.Regularschedule = Regularschedule
        if LinkedTaxiLicense != '':
            DriverObject.LinkedTaxiLicense = LinkedTaxiLicense
        if RegistrationTaxiLinked != '':
            DriverObject.RegistrationTaxiLinked = RegistrationTaxiLinked
        if TravelCommission != '':
            DriverObject.TravelCommission = TravelCommission
        if CommissionChargeCards != '':
            DriverObject.CommissionChargeCards = CommissionChargeCards
        if BankCurrentAccount != '':
            DriverObject.BankCurrentAccount = BankCurrentAccount
        if AdminNotices != '':
            DriverObject.AdminNotices = AdminNotices
        if AdminNotes != '':
            DriverObject.AdminNotes = AdminNotes
        if profileImg != '':
            DriverObject.profileImg = profileImg
        if CredintialPhoto != '':
            DriverObject.CredintialPhoto = CredintialPhoto
        if PhotoDNI != '':
            DriverObject.PhotoDNI = PhotoDNI
        DriverObject.save()
        
        ack = 5
        status = 200
        success = True
        msg = "Updated Successfully"

    except Exception as e:
        print("Update Driver Error : ", e)
        ack = 1
        status = 404
        success = False
        msg = "Can't be Update"

    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)


# @api_view(['GET'])
# def GetDriverById(request, slug):
#     Id = slug
#     try:
#         DriverkObj = Driver.objects.get(id=Id)
#         SerializerObject = DriverSerializers.GetDriverSerializer(DriverkObj, many=False)
#         DriverkObj = SerializerObject.data
#         ack = 5
#         success = True
#         msg = "Driver Information"
#         status = 200
#     except Exception as e:
#         print("Driver Information Fetch Error : ", e)
#         ack = 1
#         success = False
#         msg = "No Record Found"
#         status = 404
#         DriverkObj = {}
    
#     data = {'ack': ack, 'status': status, 'success': success, 'msg': msg, 'DriverkObj': DriverkObj}
#     return JsonResponse(data, status=status)



@api_view(['POST'])
def DriverMobileLogin(request):
    try:
        countryCode = request.data['countryCode']
        phoneNo = request.data['phoneno']
        LinkedTaxiLicense = request.data['taxiCredential']
        RegistrationTaxiLinked = request.data['identificationDocuments']
        DriverObject = Driver.objects.get(phoneNo=phoneNo, LinkedTaxiLicense=LinkedTaxiLicense)
        DriverObject.driverOTP = 432
        DriverObject.save()

        PhotoObject = DriverObject.CredintialPhoto
        print(PhotoObject.name)
        if PhotoObject.name != 'default/Image/avater.jpeg':
            ack = 5
            status = 200
            success = True
            msg = "Login Successful"
        else:
            ack = 1
            status = 400
            success = False
            msg = "Please Go to Driver Admin Panel & Upload Your Identification Document"


    
    except Exception as e:
        print("DriverMobileLogin : ", e)
        ack = 1
        status = 400
        success = False
        msg = "Login Unsuccessful"


    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)



@api_view(['POST'])
def DriverMobileValidateOtp(request):
    try:
        phoneNo = request.data['phoneno']
        driverOTP = request.data['driverOTP']
        DriverObjectOtp = Driver.objects.get(phoneNo=phoneNo,driverOTP=driverOTP)
        if DriverObjectOtp.driverOTP == driverOTP:
            ack = 5
            status = 200
            success = True
            msg = "OTP Mathched"
        else:
            ack = 1
            status = 401
            success = False
            msg = "OTP did not Matched"
    except Exception as e:
        print("OTP Validation Exception : ", e)
        ack = 1
        status = 404
        success = False
        msg = "Phone No Does not Exist"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def DriverMobileResendOtp(request):
    try:
        countryCode = request.data['countryCode']
        phoneNo = request.data['phoneno']
        DriverObject = Driver.objects.get(phoneNo=phoneNo)
        DriverObject.driverOTP = 4321
        DriverObject.save()
        ack = 5
        status = 200
        success = True
        msg = "Otp Resend"

    
    except Exception as e:
        print("DriverMobileResendOtp : ", e)
        ack = 1
        status = 400
        success = False
        msg = "Phone Number Not Validate"


    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)
        
        
        


