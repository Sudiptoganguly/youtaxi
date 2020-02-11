from djongo import models
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH


class Admin(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    phoneNo = models.TextField()
    address = models.TextField()
    role = models.TextField(default="subAdmin",)
    date = models.DateTimeField(auto_now_add=True)
    resetPasswordToken = models.TextField(default="token")
    tokenExpiration = models.BigIntegerField(default="10101")
    
    def __str__(self):
        return self.email


class Fare(models.Model):
    _id = models.ObjectIdField(default="")
    baseFare = models.FloatField()
    vehicleTypeId = models.TextField()
    fromTime = models.TimeField(auto_now_add=True)
    toTime = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.vehicleTypeId


class FareModel(models.Model):
    baseFare = models.FloatField()
    vehicleTypeId = models.TextField()
    fromTime = models.TimeField(auto_now_add=True)
    toTime = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)



class CMS(models.Model):
    heading = models.TextField()
    pageName = models.TextField()
    content = models.TextField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class Vehicle(models.Model):
    registrationNo = models.TextField()
    manufactureYear = models.TextField()
    state = models.TextField()
    color = models.TextField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class VehicleModel(models.Model):
    VehicleType = models.TextField(default="")
    driverId = models.TextField()
    AddDate = models.DateTimeField(auto_now_add=True)
    BuyDate = models.DateTimeField(auto_now_add=True)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    LastITVDate = models.DateTimeField(auto_now_add=True)
    LastMetroDate = models.DateTimeField(auto_now_add=True)
    ServicesToPerform = models.ListField(default=[])
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)


class VehicleType(models.Model):
    name = models.TextField()
    baseFare = models.FloatField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

class Subscription(models.Model):
    _id = models.ObjectIdField(default="")
    name = models.TextField()
    baseTripNo = models.IntegerField()
    baseAmountReceivable = models.FloatField()
    bonusTripNo = models.IntegerField()
    bonusAmountReceivable = models.FloatField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class Setting(models.Model):
    paypalEmail = models.EmailField()
    siteEmail = models.EmailField()
    mobile = models.TextField()
    skype = models.TextField()
    siteName = models.TextField()
    address = models.TextField()
    iconFile = models.ImageField(default=DEFAUT_IMAGE, upload_to='Admin/Setting/Icon/')
    logoFile = models.ImageField(default=DEFAUT_IMAGE, upload_to='Admin/Setting/Logo/')
    date = models.DateTimeField(auto_now_add=True)


class EmailTemplate(models.Model):
    subject = models.TextField()
    content = models.TextField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default="False")
    date = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    addDate = models.DateTimeField(auto_now_add=True)
    removeDate = models.DateTimeField(auto_now_add=True)
    cityTaxi = models.TextField()
    licenseNumber = models.TextField()
    licenseAuthorizationDate = models.DateTimeField()
    RegistrationTaxi = models.TextField()
    brand = models.TextField()
    model = models.TextField()
    typeOfvehicle = models.TextField()
    ownerNationalidentitynumber = models.TextField()
    ownerCredentialnumber = models.TextField()
    vtCard = models.BooleanField(default=False)
    buyDate = models.DateTimeField()
    registrationDate = models.DateTimeField()
    lastITVdate = models.DateTimeField()
    lastMetropolitandate = models.DateTimeField()
    lastVerificationdate = models.DateTimeField()
    driverscredentialnumber = models.TextField()
    extraDriverscredentialnumberA = models.TextField()
    extraDriverscredentialnumberB = models.TextField()
    photoOftaxi = models.ImageField(default=DEFAUT_IMAGE,upload_to='Admin/car/PhotoTaxi/')
    zipCodeWorkCity = models.TextField(default="")
    codeBluethootradio = models.TextField()
    pets = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    bluetoothRadio = models.BooleanField(default=False)
    solidarityTaxi = models.BooleanField(default=False)
    handicapedTaxi = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    

# class RideHistory(models.Model):
#     driverId = models.TextField()
#     passengerId = models.TextField()
#     route = models.TextField()
#     amount = models.FloatField()
#     paymentType = models.TextField()
#     distance = models.TextField()
#     time = models.DateTimeField()
#     date = models.DateTimeField()
