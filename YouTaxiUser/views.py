'''
        view.py
   @ Author  Kuntal
   @ Company Nat It Solved Pvt Ltd
   @ version  0.1
   @date      10/12/2019
'''

# Django Import
from django.contrib.auth.models import User as U
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
import json
from django.contrib.auth import authenticate

# Geo Lib
from geopy.distance import geodesic

# Model Import
from .models import User
from YouTaxiAdmin.models import FareModel


# Serializers Import
from .serializers import userSerializers
from YouTaxiAdmin.serializers.fareSerializers import GetFareSerializer


# Rest Framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes


def DemoUser(request):
    kolkata = [22.5726, 90.3639] 
    delhi = [28.7041, 77.1025]
    distance = geodesic(kolkata, delhi).km
    return HttpResponse("From User : " + str(distance))


@api_view(['POST'])
def ClientRegistration(request):
    try:
        imei = request.data.get('deviceIMEI')
        phone = request.data.get('phoneNo')
        try:
            FindUserObject = User.objects.get(phoneNo=phone)
            ack = 1
            success = False
            status = 409
            msg = "User Already Exist"
        except Exception as e:
            CreateUserObject = userSerializers.CreateSerializer(data=request.data)
            if CreateUserObject.is_valid():
                CreateUserObject.save()
                UserObject = User.objects.get(phoneNo=phone)
                UserObject.userOTP = 4321
                UserObject.save()
                ack = 5
                success = True
                status = 201
                msg = "User Created Successfully"
        
    except Exception as e:
        print("Create User Exception : ", e)
        ack = 1
        success = False
        status = 404
        msg = "User Not Created"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data, status=status)


@api_view(['POST'])
def ClientLogin(request):
    print(request.data)
    try:
        phone = request.data.get('phoneNo')
        print(phone)
        FindUserObject = User.objects.get(phoneNo=phone)
        FindUserObject.userOTP = 4321
        FindUserObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Go To OTP"
    except Exception as e:
        print("ClientLogin : ", e)
        ack = 1
        success = False
        status = 400
        msg = "Phone Number does Not Exist"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data, status=status)




@api_view(['POST'])
def ValidateOTP(request):
    try:
        phone = request.data['phoneNo']
        otp = request.data['otp']
        UserObject = User.objects.get(phoneNo=phone)
        if UserObject.userOTP == otp:
            ack = 5
            status = 200
            success = True
            msg = "Login Successfull"
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
def UserMobileResendOtp(request):
    try:
          phone = request.data['phoneNo']
          UserObject = User.objects.get(phoneNo=phone)
          UserObject.otp = 1234
          UserObject.save()
          ack = 5
          status = 200
          success = True
          msg = "Otp Resend"

    
    except Exception as e:
        print("UserMobileResendOtp : ", e)
        ack = 1
        status = 400
        success = False
        msg = "Phone Number Not Validate"


    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)
        
        

     




@api_view(['POST'])
def Update(request):
    try:
        Email_Flag = False
        Phone_Flag = False
        email = request.POST['email']
        phone = request.POST['phoneNo']
        try:
            CheckObject = User.objects.get(email=email)
            Email_Flag = True
        except Exception as e:
            print(e)
        try:
            CheckObject = User.objects.get(phoneNo=phone)
            Phone_Flag = True
        except Exception as e:
            print(e)
        
        if Email_Flag==True and Phone_Flag==True:
            try:
                fullName = request.POST['fullName']
            except:
                fullName = ''
            try:
                dateOfBirth = request.POST['dateOfBirth']
            except:
                dateOfBirth = ''
            try:
                gender = request.POST['gender']
            except:
                gender = ''
            try:
                address = request.POST['address']
            except:
                address = ''
            try:
                about = request.POST['about']
            except:
                about = ''
            try:
                educationalQualification = request.POST['educationalQualification']
            except:
                educationalQualification = ''
            try:
                language = request.POST['language']
            except:
                language = ''
            
            UserObj = User.objects.get(email=email)
            if fullName != '':
                UserObj.fullName = fullName
            if dateOfBirth != '':
                UserObj.dateOfBirth = dateOfBirth
            if gender != '':
                UserObj.gender = gender
            if address != '':
                UserObj.address = address
            if about != '':
                UserObj.about = about
            if educationalQualification != '':
                UserObj.educationalQualification = educationalQualification
            if language != '':
                UserObj.language = language
            UserObj.save()
            ack = 5
            status = 201
            success = True
            msg = "Profile Update Successfully"
        
        else:
            ack = 1
            status = 404
            success = False
            msg = "Email or Phone Can't be Changed"
    
    except Exception as e:
        print("Update User Error : ", e)
        ack = 1
        status = 404
        success = False
        msg = "Email or Phone Not Matched"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def UserRequest(request):
    try:
        origin = [request.data['origin']['latitude'], request.data['origin']['longitude']]
        destination = [request.data['destination']['latitude'], request.data['destination']['longitude']]
        distance = geodesic(origin, destination).km
        distance = round(distance, 2)

        FareObject = FareModel.objects.all()
        FareList = GetFareSerializer(FareObject, many=True)
        FareList = FareList.data

        success = True
        status = 200
        ack = 5
        msg = "Okay"
    
    except Exception as e:
        print("UserRequest : ", e)
        distance = 0.0
        FareList = []
        success = False
        status = 400
        ack = 1
        msg = "Fail To Process"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, "distance": distance,\
         "FareList": FareList}
    return Response(data=data, status=200)
