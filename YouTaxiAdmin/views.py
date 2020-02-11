'''
        view.py
   @ Author  Kuntal
   @ Company Nat It Solved Pvt Ltd
   @ version  0.1
   @date      10/12/2019
'''

# Django Import
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
import jwt, json

# Model Import
from .models import Admin, FareModel, VehicleModel as Vehicle, VehicleType, CMS, EmailTemplate, Setting, Car
from YouTaxiDriver import models as DriverModel
from YouTaxiUser import models as UserModel


# Serializers Import
from .serializers import adminSerializers, fareSerializers, vehiclesSerializers, \
    vehicleTypesSerializers, cmsSerializers, emailSerializers, siteSettingSerializers, carSerializers


# Rest Framework
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def DemoAdmin(request):
    return HttpResponse("From Admin")



@api_view(['POST'])
def CreateAdmin(request):
    try:
        CreateAdminObject = adminSerializers.CreateSerializer(data=request.data)
        if CreateAdminObject.is_valid():
            CreateAdminObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Admin Created"
        
    except Exception as e:
        print("Create Admin Exception : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Failed to create Admin"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data, status=status)



@api_view(['POST'])
def AdminLogin(request):
    try:
        email = request.data['email']
        password = request.data['password']
        AdminObject = Admin.objects.get(email=email, password=password)
        # Token Creation Start
        payload = {
                'id': AdminObject.id,
                'firstName': AdminObject.firstName,
                'lastName': AdminObject.lastName,
                'email': AdminObject.email,
                'phoneNo': AdminObject.phoneNo,
                'address': AdminObject.address,
                'role': AdminObject.role,
            }
        token = Encode(payload)
        # Token Creation End
        ack = 5
        success = True
        status = 200
        msg = "Login Successfully"
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGVlNTM0YzgyMjMwZDAwMjRhNjJkZWYiLCJyb2xlIjoic3ViQWRtaW4iLCJlbWFpbCI6InBhbGFzaC5uYW5kaUBjYm5pdHMuY29tIiwiZmlyc3ROYW1lIjoiWW91VGF4aSIsImxhc3ROYW1lIjoiQWRtaW4iLCJpYXQiOjE1ODAxNDM2MjAsImV4cCI6MTU4MDIzMDAyMH0.WIK5snyezjWJk2QApr47f16N6O3_frjzG-eQl_Yk1Ds"

    except Exception as e:
        print("Login Exception : ", e)
        ack = 1
        success = False
        status = 401
        msg = "Email Not Found"
        token = ''

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'token': token}
    return Response(data, status=status)



@api_view(['GET'])
def GetAdminData(request, slug):
    try:
        slug = str(slug)
        adminObject = Admin.objects.get(id=slug)
        AdminSerializers = adminSerializers.GetAdminSerializers(adminObject, many=False)
        AdminSerializers = AdminSerializers.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Admin Data Fetch Error : ", e)
        AdminSerializers = []
        ack = 1
        success = False
        status = 401
        msg = "Fail To load Data"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'adminData': AdminSerializers}
    return Response(data, status=status)


@api_view(['POST'])
def CreateUser(request):
    flag1 = False
    flag2 = False
    try:
        email = request.data['email']
        UserCheck = UserModel.User.objects.get(email=email)
    except:
        flag1 = True
    try:
        phoneNo = request.data['phoneNo']
        UserCheck = UserModel.User.objects.get(phoneNo=phoneNo)
    except:
        flag2 = True
    if flag1 == True and flag2 == True:
        try:
            UserObject = adminSerializers.CreateUserSerializer(data=request.data)
            if UserObject.is_valid():
                UserObject.save()
                ack = 5
                success = True
                status = 201
                msg = "User Created"
            
        except Exception as e:
            print("Create User Error : ", e)
            ack = 1
            success = False
            status = 400
            msg = "Fail to Create User"
    else:
        ack = 1
        success = False
        status = 400
        msg = "User Already Exist"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def CreateUserByAdmin(request):
    try:
        NewUserObject = adminSerializers.CreateUserByAdminSerializer(data=request.data)
        if NewUserObject.is_valid():
            NewUserObject.save()
            UserObject = UserModel.User.objects.get(phoneNo=request.data['phoneNo'])
            try:
                ProfileImage = request.data['ProfileImage']
            except:
                ProfileImage = ''
            if ProfileImage != '':
                UserObject.ProfileImage = ProfileImage
            UserObject.save()

            ack = 5
            success = True
            status = 201
            msg = "User Created"
    except Exception as e:
        print("User Creation Error : ", e)
        ack = 1
        success = False
        status = 400
        msg = "Fail to Create User"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def CreateDriver(request):
    try:
        DriverObject = adminSerializers.CreateDriverSerializer(data=request.data)
        if DriverObject.is_valid():
            DriverObject.save()
            DriverObject = DriverModel.Driver.objects.get(phoneNo=request.data['phoneNo'])
            DriverObject.password = request.data['phoneNo']
            DriverObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Driver Created"
        else:
            ack = 1
            success = False
            status = 406
            msg = "Please fill out the form"

    except Exception as e:
        print("Driver Creation Error : ", e)
        ack = 1
        success = False
        status = 404
        msg = "Fail To Created Driver"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def CreateDriverByAdmin(request):
    try:
        NewDriverObject = adminSerializers.CreateDriverByAdminSerializer(data=request.data)
        if NewDriverObject.is_valid():
            NewDriverObject.save()
            DriverObject = DriverModel.Driver.objects.get(phoneNo=request.data['phoneNo'])
            DriverObject.password = request.data['phoneNo']
            try:
                profileImg = request.data['profileImg']
            except:
                profileImg = ''
            try:
                PhotoDNI = request.data['PhotoDNI']
            except:
                PhotoDNI = ''
            try:
                CredintialPhoto = request.data['CredintialPhoto']
            except:
                CredintialPhoto = ''
            if profileImg != '':
                DriverObject.profileImg = profileImg
            if PhotoDNI != '':
                DriverObject.PhotoDNI = PhotoDNI
            if CredintialPhoto != '':
                DriverObject.CredintialPhoto = CredintialPhoto
            DriverObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Driver Created"
        else:
            ack = 1
            success = False
            status = 400
            msg = "Please fill out the form"

    except Exception as e:
        print("Driver Creation Error : ", e)
        ack = 1
        success = False
        status = 400
        msg = "Fail To Created Driver"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def CreateFare(request):
    try:
        baseFare = request.data['baseFare']
        vehicleTypeId = request.data['vehicleTypeId']
        fromTime = request.data['fromTime']
        toTime = request.data['toTime']
        # status = request.data['status']

        FareObject = FareModel(baseFare=baseFare,vehicleTypeId=vehicleTypeId,fromTime=fromTime,\
            toTime=toTime)
        FareObject.save()
        # print(request.data)
        # FareObject = fareSerializers.CreateFareSerializer(data=request.data)
        # if FareObject.is_valid():
        #     FareObject.save()
        ack = 5
        success = True
        status = 201
        msg = "Fare Created"
        # else:
        #     ack = 1
        #     success = False
        #     status = 401
        #     msg = "Fail To Create Fare"
    except Exception as e:
        print("Create Fare Error : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Fail To Create Fare"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['GET'])
def GetAllFares(request):
    try:
        FareObject = FareModel.objects.all()
        FareList = fareSerializers.GetFareSerializer(FareObject, many=True)
        FareList = FareList.data
        ack = 5
        success = True
        status = 200
        msg = "Fare List Available"

    except Exception as e:
        print("Get All Fare List Error : ", e)
        FareList = {}
        ack = 1
        success = False
        status = 401
        msg = "Fail to Load"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'FareList': FareList}
    return Response(data=data, status=status)



@api_view(['GET'])
def GetFareById(request, slug):
    Id = slug
    try:
        FareObject = Fare.objects.all(id=Id)
        FareList = fareSerializers.GetFareSerializer(FareObject, many=False)
        FareList = FareList.data
        ack = 5
        success = True
        status = 200
        msg = "Fare Data Available"

    except Exception as e:
        print("Get Fare Error : ", e)
        FareList = []
        ack = 1
        success = False
        status = 401
        msg = "Fail to Load"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'FareList': FareList}
    return Response(data=data, status=status)



@api_view(['POST'])
def UpdateFare(request, slug):
    Id = slug
    try:
        baseFare = request.data.get('baseFare')
        FareObject = Fare.objects.all(id=Id)
        FareObject.baseFare = baseFare
        FareObject.save()
        ack = 5
        success = True
        status = 201
        msg = "Fare Updated"
    except Exception as e:
        print("Update Fare Error : ", e)
        ack = 1
        success = True
        status = 401
        msg = "Fail to update"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def CreateVehicles(request):
    try:
        VehicleType = request.data['vehicleTypeId']
        driverId = request.data['driverId']
        AddDate = request.data['addDate']
        BuyDate = request.data['buyDate']
        RegistrationDate = request.data['registrationDate']
        LastITVDate = request.data['lastITVDate']
        LastMetroDate = request.data['lastMetroDate']
        ServicesToPerform = list(request.data['servicesToPerform'])
        if request.data['status'] == 'true':
            status = True
        else:
            status = False

        VObject = Vehicle(VehicleType=VehicleType,driverId=driverId,AddDate=AddDate,BuyDate=BuyDate, \
            RegistrationDate=RegistrationDate,LastITVDate=LastITVDate,LastMetroDate=LastMetroDate, \
            ServicesToPerform=ServicesToPerform,status=status)
        VObject.save()
        ack = 5
        success = True
        status = 201
        msg = "Vehicles Created"
        # VehicleObject = vehiclesSerializers.CreateVehicleSerializer(data=request.data)
        # if VehicleObject.is_valid():
        #     VehicleObject.save()
        #     ack = 5
        #     success = True
        #     status = 201
        #     msg = "Vehicles Created"
        # else:
        #     ack = 1
        #     success = False
        #     status = 401
        #     msg = "Fali to create Vehicles"
    except Exception as e:
        print("Create Vehicles Error : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Fali to create Vehicles"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetAllVehicles(request):
    try:
        VehicleObjectList = Vehicle.objects.all()
        VehicleObjectList = vehiclesSerializers.GetVehicleSerializer(VehicleObjectList, many=True)
        VehicleObjectList = VehicleObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Data Load Error : ", e)
        VehicleObjectList = {}
        ack = 5
        success = True
        status = 201
        msg = "Fail to Laod"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'VehicleList': VehicleObjectList}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetVehiclesById(request, slug):
    try:
        Id = slug
        VehicleObjectList = Vehicle.objects.get(id=Id)
        VehicleObjectList = vehiclesSerializers.GetVehicleSerializer(VehicleObjectList, many=False)
        VehicleObjectList = VehicleObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Data Load Error : ", e)
        VehicleObjectList = []
        ack = 5
        success = True
        status = 201
        msg = "Fail To Load"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'VehicleObjectList': VehicleObjectList}
    return Response(data=data, status=status)


@api_view(['POST'])
def UpdateVehicle(request, slug):
    try:
        Id = slug
        VehicleObject = Vehicle.objects.get(id=Id)
        ack = 5
        success = True
        status = 200
        msg = "Vehicles Updated"
    except Exception as e:
        print("Data Load Error : ", e)
        ack = 1
        success = False
        status = 404
        msg = "Fail To Update"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetAllVehicleTypes(request):
    try:
        VehicleTypeObject = VehicleType.objects.all()
        VTypeList = vehicleTypesSerializers.GetVehicleSerializer(VehicleTypeObject, many=True)
        VTypeList = VTypeList.data
        ack = 5
        success = True
        status = 200
        msg = "VehiclesType Loaded"
    except Exception as e:
        print("VehicleType Data Load Error : ", e)
        VTypeList = {}
        ack = 1
        success = False
        status = 404
        msg = "Fail To Laod"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'VTypeList': VTypeList}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetVehicleTypeById(request, slug):
    try:
        Id = slug
        VehicleTypeObject = VehicleType.objects.get(id=Id)
        VTypeList = vehicleTypesSerializers.GetVehicleSerializer(VehicleTypeObject, many=False)
        VTypeList = VTypeList.data
        ack = 5
        success = True
        status = 200
        msg = "VehiclesType Loaded"
    except Exception as e:
        print("VehicleType Data Load Error : ", e)
        VTypeList = {}
        ack = 1
        success = False
        status = 404
        msg = "Fail To Laod"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'VTypeList': VTypeList}
    return Response(data=data, status=status)


@api_view(['POST'])
def CreateVehicleType(request):
    try:
        VehicleTypeObj = vehicleTypesSerializers.CreateVehicleSerializer(data=request.data)
        if VehicleTypeObj.is_valid():
            VehicleTypeObj.save()
            ack = 5
            success = True
            status = 201
            msg = "VehiclesType Created"
        else:
            ack = 1
            success = False
            status = 401
            msg = "Fail To Create"
    except Exception as e:
        print("Create Vehicle Type Error : ", e)
        ack = 1
        success = False
        status = 404
        msg = "Fail To Create"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def UpdateVehicleType(request, slug):
    pass


@api_view([''])
def DeleteVehicleType(request, slug):
    pass


@api_view(['POST'])
def CreateCMS(request):
    try:
        cmsObject = cmsSerializers.CreateSerializer(data=request.data)
        if cmsObject.is_valid():
            cmsObject.save()
            ack = 5
            success = True
            status = 201
            msg = "CMS Created"
        else:
            ack = 1
            success = False
            status = 401
            msg = "Fail To CMS Created"
    except Exception as e:
        print("CMS Creation Error : ", e)
        ack = 1
        success = False
        status = 401
        msg = "Fail To Create CMS"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetAllCMS(request):
    try:
        cmsObjectList = CMS.objects.all()
        cmsObjectList = cmsSerializers.GetCMSSerializer(cmsObjectList, many=True)
        cmsObjectList = cmsObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Fetch CMS list Error : ", e)
        cmsObjectList = {}
        ack = 1
        success = False
        status = 406
        msg = "Fail to Load Data"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'cmsList': cmsObjectList}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetCMSById(request, slug):
    try:
        Id = slug
        cmsObjectList = CMS.objects.get(id=Id)
        cmsObjectList = cmsSerializers.GetCMSSerializer(cmsObjectList, many=False)
        cmsObjectList = cmsObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Fetch CMS list Error : ", e)
        cmsObjectList = []
        ack = 1
        success = False
        status = 406
        msg = "Fail to Load Data"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'cmsObjectList': cmsObjectList}
    return Response(data=data, status=status)


@api_view([''])
def UpdateCMS(request, slug):
    pass


@api_view([''])
def DeleteCMS(request, slug):
    pass



@api_view(['POST'])
def CreateEmailTemplate(request):
    try:
        EmailTempObject = emailSerializers.CreateSerializer(data=request.data)
        if EmailTempObject.is_valid():
            EmailTempObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Templete Created"
        else:
            ack = 1
            success = False
            status = 401
            msg = "Templete Can't be created"
    except Exception as e:
        print("Create Tempalte Error : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Templete Can't be created"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['GET'])
def GetAllEmailTemplates(request):
    try:
        EmailTempObjectList = EmailTemplate.objects.all()
        EmailTempObjectList = emailSerializers.GetAllTemplateSerializer(EmailTempObjectList, many=True)
        EmailTempObjectList = EmailTempObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Email Template Data Load Error ", e)
        EmailTempObjectList = {}
        ack = 1
        success = False
        status = 406
        msg = "Fail to load"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'EmailTempObjectList': EmailTempObjectList}
    return Response(data=data, status=status)



@api_view(['GET'])
def GetEmailTemplateById(request, slug):
    try:
        Id = slug
        EmailTempObjectList = EmailTemplate.objects.get(id=Id)
        EmailTempObjectList = emailSerializers.GetAllTemplateSerializer(EmailTempObjectList, many=False)
        EmailTempObjectList = EmailTempObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Email Template Data Load Error ", e)
        EmailTempObjectList = []
        ack = 1
        success = False
        status = 406
        msg = "Fail to load"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'EmailTempObjectList': EmailTempObjectList}
    return Response(data=data, status=status)


@api_view([''])
def UpdateEmailTemplate(request, slug):
    pass


@api_view([''])
def DeleteEmailTemplate(request, slug):
    pass


@api_view(['POST'])
def SiteSetting(request):
    try:
        SiteSettingObject = Setting.objects.get(id=1)
        try:
            paypalEmail = request.POST['paypalEmail']
        except:
            paypalEmail = ''
        try:
            siteEmail = request.POST['siteEmail']
        except:
            siteEmail = ''
        try:
            mobile = request.POST['mobile']
        except:
            mobile = ''
        try:
            skype = request.POST['skype']
        except:
            skype = ''
        try:
            siteName = request.POST['siteName']
        except:
            siteName = ''
        try:
            address = request.POST['address']
        except:
            address = ''
        try:
            iconFile = request.FILES['iconFile']
        except:
            iconFile = ''
        try:
            logoFile = request.FILES['logoFile']
        except:
            logoFile = ''
        date = datetime.datetime.now()
        
        if paypalEmail != '':
            SiteSettingObject.paypalEmail = paypalEmail
        if siteEmail != '':
            SiteSettingObject.siteEmail = siteEmail
        if mobile != '':
            SiteSettingObject.mobile = mobile
        if skype != '':
            SiteSettingObject.skype = skype
        if siteName != '':
            SiteSettingObject.siteName = siteName
        if address != '':
            SiteSettingObject.address = address
        if iconFile != '':
            SiteSettingObject.iconFile = iconFile
        if logoFile != '':
            SiteSettingObject.logoFile = logoFile
        SiteSettingObject.date = date
        SiteSettingObject.save()
        ack = 5
        success = True
        status = 201
        msg = "Setting Updated Successfully"

    except Exception as e:
        print(e)
        try:
            paypalEmail = request.POST['paypalEmail']
            siteEmail = request.POST['siteEmail']
            mobile = request.POST['mobile']
            skype = request.POST['skype']
            siteName = request.POST['siteName']
            address = request.POST['address']
            iconFile = request.FILES['iconFile']
            logoFile = request.FILES['logoFile']
            date = datetime.datetime.now()
            SettingObject = Setting(paypalEmail=paypalEmail,siteEmail=siteEmail,mobile=mobile,skype=skype,siteName=siteName,address=address,iconFile=iconFile,logoFile=logoFile,date=date)
            SettingObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Setting Updated Successfully"
        except Exception as e:
            print("Site Setting Error : ", e)
            ack = 1
            success = False
            status = 406
            msg = "Data Not Created"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['GET'])
def GetSiteSetting(request):
    try:
        SiteSettingObject = Setting.objects.get(id=1)
        SiteSettingSerializers = siteSettingSerializers.GetSiteSettingDataSerializer(SiteSettingObject, many=False)
        SiteSettingSerializers = SiteSettingSerializers.data
        ack = 5
        success = True
        status = 200
        msg = "Data Fetch Successfully"
    except Exception as e:
        print("Data Fetch Error : ", e)
        SiteSettingSerializers = []
        ack = 5
        success = False
        status = 401
        msg = "Data Can't be Loaded"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, "SiteSetting": SiteSettingSerializers}
    return Response(data=data, status=status)



@api_view(['POST'])
def UserActivate(request, slug):
    try:
        UserObject = UserModel.User.objects.get(id=slug)
        UserObject.status = True
        UserObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Status Updated"
    except Exception as e:
        print("Status Change Error : ", e)
        ack = 1
        success = True
        status = 400
        msg = "Fail To Update"
        
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def UserDeactivate(request, slug):
    try:
        UserObject = UserModel.User.objects.get(id=slug)
        UserObject.status = False
        UserObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Status Updated"
    except Exception as e:
        print("Status Change Error : ", e)
        ack = 1
        success = True
        status = 400
        msg = "Fail To Update"
        
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)



@api_view(['POST'])
def DriverActivate(request, slug):
    try:
        DriverObject = DriverModel.Driver.objects.get(id=slug)
        DriverObject.status = True
        DriverObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Status Updated"
    except Exception as e:
        print("Status Change Error : ", e)
        ack = 1
        success = True
        status = 400
        msg = "Fail To Update"
        
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def DriverDeactivate(request, slug):
    try:
        DriverObject = DriverModel.Driver.objects.get(id=slug)
        DriverObject.status = False
        DriverObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Status Updated"
    except Exception as e:
        print("Status Change Error : ", e)
        ack = 1
        success = True
        status = 400
        msg = "Fail To Update"
        
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def DeleteUser(request, slug):
    try:
        UserObject = UserModel.User.objects.get(id=slug)
        UserObject.isDeleted = True
        UserObject.removeDate = datetime.datetime.now()
        UserObject.save()
        ack = 5
        status = 200
        success = True
        msg = "User Deleted"
    except Exception as e:
        print("Delete User Error : ", e)
        ack = 1
        status = 404
        success = False
        msg = "Fail To Delete"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def DeleteDriver(request, slug):
    try:
        DriverkObj = DriverModel.Driver.objects.get(id=slug)
        DriverkObj.isDeleted = True
        DriverkObj.removeDate = datetime.datetime.now()
        DriverkObj.save()
        ack = 5
        success = True
        msg = "Driver Deleted"
        status = 200
    except Exception as e:
        print("Driver Information Fetch Error : ", e)
        ack = 1
        success = False
        msg = "Fail To Delete"
        status = 400
    
    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)



@api_view(['POST'])
def ActivateDeactivateVehicleType(request, slug):
    try:
        VehicleTypeObject = VehicleType.objects.get(id=slug)
        if VehicleTypeObject.status:
            VehicleTypeObject.status = False
        else:
            VehicleTypeObject.status = True
        VehicleTypeObject.save()
        ack = 5
        success = True
        msg = "Status Changed"
        status = 200
    except Exception as e:
        print("ActivateDeactivateVehicleType Error : ", e)
        ack = 1
        success = False
        msg = "Fail To Change Status"
        status = 400

    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)



@api_view(['POST'])
def ActivateDeactivateVehicle(request, slug):
    try:
        VehicleObject = Vehicle.objects.get(id=slug)
        if VehicleObject.status:
            VehicleObject.status = False
        else:
            VehicleObject.status = True
        VehicleObject.save()
        ack = 5
        success = True
        msg = "Status Changed"
        status = 200
    except Exception as e:
        print("ActivateDeactivateVehicle Error : ", e)
        ack = 1
        success = False
        msg = "Fail To Change Status"
        status = 400

    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)



@api_view(['POST'])
def ActivateDeactivateEmailTemplate(request, slug):
    try:
        EmailObject = EmailTemplate.objects.get(id=slug)
        if EmailObject.status:
            EmailObject.status = False
        else:
            EmailObject.status = True
        EmailObject.save()
        ack = 5
        success = True
        msg = "Status Changed"
        status = 200
    except Exception as e:
        print("ActivateDeactivateVehicle Error : ", e)
        ack = 1
        success = False
        msg = "Fail To Change Status"
        status = 400

    data = {'ack': ack, 'status': status, 'success': success, 'msg': msg}
    return JsonResponse(data, status=status)

@api_view(['POST'])
def CreateCar(request):
    try:
        # addDate = request.data['addDate']
        # removeDate = request.data['removeDate']
        # cityTaxi = request.data['cityTaxi']
        # licenseNumber = request.data['licenseNumber']
        # licenseAuthorizationDate = request.data['licenseAuthorizationDate']
        # RegistrationTaxi = request.data['RegistrationTaxi']
        # brand = request.data['brand']
        # model = request.data['model']
        # typeOfvehicle = request.data['typeOfVehicle']
        # ownerNationalidentitynumber = request.data['ownerNationalidentitynumber']
        # ownerCredentialnumber = request.data['ownerCredentialnumber']
        # vtCard = request.data['vtCard']
        # buyDate = request.data['buyDate']
        # registrationDate = request.data['registrationDate']
        # lastITVdate = request.data['lastITVdate']
        # lastMetropolitandate = request.data['lastMetropolitandate']
        # lastVerificationdate = request.data['lastVerificationdate']
        # driverscredentialnumber = request.data['driverscredentialnumber']
        # extraDriverscredentialnumberA= request.data['extraDriverscredentialnumberA']
        # extraDriverscredentialnumberB = request.data['extraDriverscredentialnumberB']
        # photoOftaxi = request.data['photoOftaxi']
        # codeBluethootradio = request.data['codeBluethootradio']
        # pets = request.data['pets']
        # package = request.data['package']
        # bluetoothRadio = request.data['bluetoothRadio']
        # solidarityTaxi = request.data['solidarityTaxi']
        # handicapedTaxi = request.data['handicapedTaxi']
        # status = request.data['status']
      
        # if request.data['status'] == 'true':
        #     status = True
        # else:
        #     status = False

        # CObject = Car(addDate=addDate,removeDate=removeDate,cityTaxi=cityTaxi,licenseNumber=licenseNumber,
        #                 RegistrationTaxi=RegistrationTaxi,brand=brand,model=model, typeOfVehicle=typeOfVehicle,
        #                 ownerNationalidentitynumber=ownerNationalidentitynumber,ownerCredentialnumber=ownerCredentialnumber,
        #                 vtCard=vtCard,buyDate=buyDate,registrationDate=registrationDate,lastITVdate=lastITVdate,
        #                 lastMetropolitandate=lastMetropolitandate,lastVerificationdate=lastVerificationdate,
        #                 driverscredentialnumber=driverscredentialnumber,extraDriverscredentialnumberA=extraDriverscredentialnumberA,
        #                 extraDriverscredentialnumberB=extraDriverscredentialnumberB,photoOftaxi=photoOftaxi,codeBluethootradio=codeBluethootradio,
        #                 pets=pets,package=package,bluetoothRadio=bluetoothRadio,solidarityTaxi=solidarityTaxi,handicapedTaxi=handicapedTaxi,
        #                 status=status)
        # CObject.save()

        # print(request.data)
        print(type(request.data['licenseAuthorizationDate']))

        CarObject = carSerializers.CreateCarSerializers(data=request.data)
        if CarObject.is_valid(raise_exception=True):
            CarObject.save()
            ack = 5
            success = True
            status = 201
            msg = "Car Created"
        else:
            ack = 1
            success = False
            status = 400
            msg = "Car Not Created"
        
    except Exception as e:
        print("Create Car Error : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Fali to create Car"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetAllCarsForAdmin(request):
    try:
        CarObjectList = Car.objects.all()
        CarObjectList = carSerializers.GetCarSerializersForAdmin(CarObjectList, many=True)
        CarObjectList = CarObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Data Load Error : ", e)
        CarObjectList = []
        ack = 5
        success = True
        status = 201
        msg = "Fail to Laod"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'CarList': CarObjectList}
    return Response(data=data, status=status)


@api_view(['GET'])
def GetAllCarsForOthers(request):
    try:
        CarObjectList = Car.objects.all()
        CarObjectList = carSerializers.GetCarSerializersForOthers(CarObjectList, many=True)
        CarObjectList = CarObjectList.data
        ack = 5
        success = True
        status = 200
        msg = "Data Loaded"
    except Exception as e:
        print("Data Load Error : ", e)
        CarObjectList = []
        ack = 5
        success = True
        status = 201
        msg = "Fail to Laod"
    
    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'CarList': CarObjectListt}
    return Response(data=data, status=status)


@api_view(['GET'])
def CarTypeById(request, slug):
    try:
        Id = slug
        CarTypeObject = Car.objects.get(id=Id)
        CarTypeList = carSerializers.GetCarSerializersForAdmin(CarTypeObject, many=False)
        CarTypeObject = CarTypeObject.data
        ack = 5
        success = True
        status = 200
        msg = "Car Loaded"
    except Exception as e:
        print("VehicleType Data Load Error : ", e)
        CarTypeObject = {}
        ack = 1
        success = False
        status = 404
        msg = "Fail To Laod"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg, 'Car': CarTypeObject}
    return Response(data=data, status=status)


@api_view(['POST'])
def CarActivateDactivate(request, slug):
    try:
        Id = slug
        CarObject = Car.objects.get(id=Id)
        if CarObject.isDeleted:
            CarObject.isDeleted = False
        else:
            CarObject.isDeleted = True
        CarObject.save()
        ack = 5
        success = True
        status = 200
        msg = "Car Loaded"
    except Exception as e:
        print("VehicleType Data Load Error : ", e)
        ack = 1
        success = False
        status = 404
        msg = "Fail To Laod"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)


@api_view(['POST'])
def CarUpdate(request,slug):
    try:
        Id = slug
        CarObject = Car.objects.get(id=Id)
        CarUpdate = carSerializers.UpdateCarSerializers(CarObject, data=request.data, partial=True)
        if CarUpdate.is_valid():
            CarUpdate.save()
            ack = 5
            success = True
            status = 201
            msg = "Car Upadted"
        else:
            ack = 1
            success = False
            status = 400
            msg = "Car Not Updated"
        
    except Exception as e:
        print("Update Car Error : ", e)
        ack = 1
        success = False
        status = 406
        msg = "Fali to Update Car"

    data = {'success': success, 'status': status, 'ack': ack, 'msg': msg}
    return Response(data=data, status=status)






# Encoding Decoding
def Encode(payload):
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    print("Token : ", jwt_token['token'].decode("utf-8"))
    return jwt_token['token'].decode("utf-8")

def Decode():
    pass