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
import json, jwt
from django.contrib.auth import authenticate

# Model Import
from YouTaxiDriver import models as DriverModel
from YouTaxiAdmin import models as AdminModel
from YouTaxiUser import models as UserModel

# Serializers Import
from .serializers import webSerializers

# Rest Framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes


def DemoWebsite(request):
    return HttpResponse("From Website")

'''
Website Admin Login
'''
@api_view(['POST'])
def AdminLogin(request):
    print("#######", request)
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        AdminObject = AdminModel.Admin.objects.get(email=email)
        if AdminObject.password == password:
            ack = 5
            success = True
            status = 200
            msg = "Login Successfully"
        else:
            ack = 1
            success = False
            status = 406
            msg = "Password is not matched"
    except Exception as e:
        print("Login Exception : ", e)
        ack = 5
        success = False
        status = 406
        msg = "Email Not Found"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data, status=status)

'''
Website Driver Registration
'''

@api_view(['POST'])
def CreateDriver(request):
    try:
        email = request.data.get('email')
        phone = request.data.get('phoneNo')
        flag = True
        try:
            CheckObj = DriverModel.Driver.objects.get(email=email)
            flag = False
        except Exception as e:
            print("Email Already Exist : ", e)
        try:
            CheckObj = DriverModel.Driver.objects.get(phoneNo=phone)
            flag = False
        except Exception as e:
            print("Phone Number Already Exist : ", e)
        
        if flag:
            CreateDriverObject = webSerializers.CreateDriverSerializer(data=request.data)
            if CreateDriverObject.is_valid():
                CreateDriverObject.save()
                phone = request.data.get('phoneNo')
                DriverObject = DriverModel.Driver.objects.get(phoneNo=phone)
                DriverObject.password = phone
                DriverObject.save()
                ack = 5
                status = 201
                success = True
                msg = "Driver Created"
            else:
                ack = 1
                status = 406
                success = False
                msg = "Driver Not Created"
        else:
            ack = 1
            status = 406
            success = False
            msg = "Driver Already Exist"
    
    except Exception as e:
        print("Driver Create Exception : ", e)
        ack = 1
        status = 406
        success = False
        msg = "Driver Not Created"
    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)

'''
Driver Login OTP
'''

@api_view(['POST'])
def DriverLoginOTPSystem(request):
    try:
        phone = request.data['phoneNo']
        DriverObject = DriverModel.Driver.objects.get(phoneNo=phone)
        DriverObject.driverOTP = 4321
        DriverObject.save()
        ack = 5
        status = 200
        success = True
        msg = "OTP Sent"
    except Exception as e:
        print("DriverLoginOTPSystem Error : ", e)
        ack = 5
        status = 400
        success = False
        msg = "Mobile Number Not Found"

    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)

'''
Driver Login
'''


@api_view(['POST'])
def DriverLogin(request):
    try:
        phone = request.data['phoneNo']
        otp = request.data['driverOTP']
        DriverObject = DriverModel.Driver.objects.get(phoneNo=phone,driverOTP=otp)
        payload = {
                'id': DriverObject.id,
                'firstName': DriverObject.firstName,
                'lastName': DriverObject.lastName,
                'phoneNo': DriverObject.phoneNo,
                'isDeleted': DriverObject.isDeleted,
            }
        token = Encode(payload)
        ack = 5
        status = 200
        success = True
        msg = "Login Successful"
        # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc0RlbGV0ZWQiOmZhbHNlLCJkYXRlIjoiMjAxOS0xMi0wOVQxMzo0OToxMS4yMDVaIiwiX2lkIjoiNWUxYzZhYTYxN2I1NDQwM2ZhZjkwMWZhIiwiZmlyc3ROYW1lIjoiSmVzdGVyIiwibGFzdE5hbWUiOiJOYXJ2w6F6IiwicGhvbmVObyI6IiszNCA3ODYgMjAyIDkwNCIsImVtYWlsIjoiUm9tYW5CYXJhamFzTmFydmFlekBkYXlyZXAuY29tIiwiYWRkcmVzcyI6IkNhbGxlIFByb2MuIFNhbiBTZWJhc3Rpw6FuLCA0OVxyXG4xMjU5NyBTYW50YSBNYWdkYWxlbmEgZGUgUHVscGlzIiwicGVyc29uYWxJRCI6Ii9kcml2ZXJfaW1hZ2UvcGVyc29uYWxJRC0xNTc2MTU3ODUzNDY3LXBlcnNvbmFsLWlkLWluZm8ucG5nIiwiZGF0ZU9mQmlydGgiOiIxOTkyLTEyLTA5VDE4OjMwOjAwLjAwMFoiLCJkcml2aW5nTGljZW5jZU5vIjoiRExOLTAwMSIsImVkdWNhdGlvbmFsUXVhbGlmaWNhdGlvbiI6IkdyYWR1YXRlIiwiZ2VuZGVyIjoiTSIsInBlcnNvbmFsSURObyI6IlBJRE4tMDAxIiwiZHJpdmluZ0xpY2VuY2UiOiIvZHJpdmVyX2ltYWdlL2RyaXZpbmdMaWNlbmNlLTE1NzYxNTc4NTM0NjktZHJpdmluZy1saWNlbmNlLmpwZyIsInByb2ZpbGVJbWciOiIvZHJpdmVyX2ltYWdlL3Byb2ZpbGVJbWctMTU3NjE1Nzg1MzQ4MS11c2VyLWltZy5wbmciLCJpYXQiOjE1ODAyNzk4NTcsImV4cCI6MTU4MDM2NjI1N30.nGkdfsaIyXDNDU8L8E-ZbY5Do1TCws-iS3oJbdZ_EmE'
    
    except Exception as e:
        print("Email Does Not Exist", e)
        ack = 1
        status = 406
        success = False
        msg = "Email Does Not Exist"
        token = ''
    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg, 'token': token}
    return JsonResponse(data, status=status)

'''
Admin Get All Driver List

'''


@api_view(['GET'])
def GetAllDriver(request):
    try:
        DriverList = DriverModel.Driver.objects.all().filter(isDeleted=False)
        SerializerObject = webSerializers.GetAllDriverSerializer(DriverList, many=True)
        DriverList = SerializerObject.data
        ack = 5
        success = True
        msg = "All Driver List"
        status = 200
    except Exception as e:
        print("Fetch All Driver List Exception : ", e)
        DriverList = []
        ack = 1
        success = False
        msg = "No Record Found"
        status = 406
    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg, 'DriverList': DriverList}
    return JsonResponse(data, status=status)

'''
Admin Get Driver By Id

'''

@api_view(['GET'])
def GetDriverById(request, slug):
    try:
        slug = str(slug)
        DriverkObj = DriverModel.Driver.objects.get(id=slug)
        SerializerObject = webSerializers.GetDriverSerializer(DriverkObj, many=False)
        DriverkObj = SerializerObject.data
        ack = 5
        success = True
        msg = "Driver Information"
        status = 200
    except Exception as e:
        print("Driver Information Fetch Error : ", e)
        ack = 1
        success = False
        msg = "No Record Found"
        status = 404
        DriverkObj = {}
    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg, 'driverData': DriverkObj}
    return JsonResponse(data, status=status)

'''

Admin Get User List

'''

@api_view(['GET'])
def GetAllUser(request):
    try:
        UserList = UserModel.User.objects.all().filter(isDeleted=False)
        UserListSerializers = webSerializers.GetUserSerializer(UserList, many=True)
        UserListSerializers = UserListSerializers.data
        ack = 5
        status = 200
        success = True
        msg = "Driver List Found"
    except Exception as e:
        print("Get All User Error : ", e)
        UserListSerializers = []
        ack = 1
        status = 404
        success = False
        msg = "No Record Found"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, \
        'UserList': UserListSerializers}
    return Response(data=data, status=status)

'''
Admin Get User Id

'''

@api_view(['GET'])
def GetUser(request, slug):
    try:
        UserObject = UserModel.User.objects.get(id=slug)
        UserSerializers = webSerializers.GetUserSerializer(UserObject, many=False)
        UserSerializers = UserSerializers.data
        ack = 5
        status = 200
        success = True
        msg = "User Found"
    except Exception as e:
        print("Get User Error : ", e)
        UserSerializers = {}
        ack = 1
        status = 404
        success = False
        msg = "No Record Found"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, \
        'UserData': UserSerializers}
    return Response(data=data, status=status)

'''
Search User 

'''

@api_view(['GET'])
def SearchUser(request, slug):
    try:
        UserData = UserModel.User.objects.filter(fullName__icontains=slug)
        if len(UserData) != 0:
            UserSerializerData = webSerializers.GetUserSerializer(UserData, many=True)
            UserData = UserSerializerData.data
            ack = 5
            status = 200
            success = True
            msg = "Match Found"
        else:
            UserData = []
            ack = 1
            status = 400
            success = False
            msg = "Match Not Found"
    except Exception as e:
        print("SearchUser Error : ", e)
        UserData = []
        ack = 1
        status = 400
        success = False
        msg = "Match Not Found"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'UserData': UserData}
    return Response(data=data, status=status)

'''
Search Driver
'''

@api_view(['GET'])
def SearchDriver(request, slug):
    try:
        DriverData = DriverModel.Driver.objects.filter(firstName__contains=slug)
        if len(DriverData) != 0:
            DriverSerializerData = webSerializers.GetDriverSerializer(DriverData, many=True)
            DriverData = DriverSerializerData.data
            ack = 5
            status = 200
            success = True
            msg = "Match Found"
        else:
            DriverData = []
            ack = 1
            status = 400
            success = False
            msg = "Match Not Found"
    except Exception as e:
        print("SearchDriver Error : ", e)
        DriverData = []
        ack = 1
        status = 400
        success = False
        msg = "Match Not Found"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'DriverData': DriverData}
    return Response(data=data, status=status)






def Encode(payload):
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    print("Token : ", jwt_token['token'].decode("utf-8"))
    return jwt_token['token'].decode("utf-8")

def Decode():
    pass
