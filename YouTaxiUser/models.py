from djongo import models
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH
from django.utils import timezone


class User(models.Model):
    TYPE_OF_CLIENT = (
        ('GOLD', 'GOLD'),
        ('SILVER','SILVER'),
        ('BRONZE', 'BRONZE'),
        ('NONE', 'NONE'),
    )
    fullName = models.TextField(default="")
    countryCode = models.TextField(default="+91")
    phoneNo = models.TextField(default="")
    email = models.EmailField(default="")
    createDate = models.DateTimeField(auto_now_add=True)
    removeDate = models.DateTimeField(default=timezone.now)
    deviceIMEI = models.TextField(default=[])
    deviceHash = models.TextField(default="")
    status = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    dateOfBirth = models.DateTimeField(auto_now_add=True)
    gender = models.TextField(default='Others')
    address = models.TextField(default="My Address")
    about = models.TextField(default="About User")
    educationalQualification = models.TextField(default="Education")
    paymentMethod = models.ListField(default=[])
    userOTP = models.TextField()
    userLocation = models.TextField(default="88.4807644, 22.5808643")
    language = models.TextField(default='English')
    favoriteTaxis = models.ListField(default=[])
    taxisBlocked = models.ListField(default=[])
    adminNotices = models.TextField(default="Notice")
    clintScore = models.FloatField(default=0.0)
    ProfileImage = models.ImageField(default=DEFAUT_IMAGE, upload_to='User/ProfileImage/')
    typeOfClient = models.CharField(max_length=1, choices=TYPE_OF_CLIENT,default="")
    package = models.BooleanField(default=False)
    solidarityTaxi = models.BooleanField(default=False)
    handicapedTaxi = models.BooleanField(default=False)
    bankCardDetails = models.TextField(default="")
    bankAccountDetails = models.TextField(default="")
    
 
 
    def __str__(self):
        return self.phoneNo


