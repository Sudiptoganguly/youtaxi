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
from .models import Company, Workers

# Serializers Import
from .serializers import companySerializers


# Rest Framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes



@api_view(['POST'])
def CreateCompany(request):
        try:
                # name = request.data['name']
                # address = request.data['address']
                # city = request.data['city']
                # postalCode = request.data['postalCode']
                # nif = request.data['nif']
                # administrators = request.data['administrators']
                # bankCardDetails = request.data['bankCardDetails']
                # bankAccountDetails = request.data['bankAccountDetails']
                # phoneNo = request.data['phoneNo']
                # firstName = request.data['firstName']
                # lastName = request.data['lastName']
                # email = request.data['email']

                # WorkerObject = Workers(phoneNo=phoneNo,firstName=firstName,lastName=lastName,email=email)
                # WorkerObject.save()

                # CompanyObject = Company(name=name,address=address,city=city,postalCode=postalCode,\
                #         nif=nif,administrators=administrators,Worker=WorkerObject,bankCardDetails=bankCardDetails,\
                #         bankAccountDetails=bankAccountDetails)
                # Company.save()
                
                # print(request.data)
                C = companySerializers.CreateCompanySerializer(data=request.data)
                if C.is_valid(raise_exception=True):
                        C.save()

                success = True
                status = 201
                ack = 5
                msg = "Successfully Created"
        except Exception as e:
                print("CreateCompany : ", e)
                success = False
                status = 400
                ack = 1
                msg = "Fail To Create Company"
        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
        return Response(data, status=status)


@api_view(['GET'])
def GetCompanyForTableDispaly(request):
        try:
                CompanyObject = Company.objects.all()
                companyList = companySerializers.GetCompanyForTable(CompanyObject, many=True)
                companyList = companyList.data
                success = True
                status = 200
                ack = 5
                msg = "Data Loaded"
        except Exception as e:
                print("GetCompanyForTableDispaly : ", e)
                companyList = []
                success = False
                status = 400
                ack = 1
                msg = "Fail To Load"

        data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'companyList': companyList}
        return Response(data, status=status)