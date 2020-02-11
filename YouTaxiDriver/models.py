from djongo import models
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH


class Driver(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    countryCode = models.TextField(default="+91")
    phoneNo = models.TextField()
    landLineNumber = models.TextField(default="")
    email = models.EmailField()
    password = models.TextField(default="")
    address = models.TextField()
    status = models.BooleanField(default=False)
    dateOfBirth = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    removeDate = models.DateTimeField(auto_now_add=True)
    placeOfBirth = models.TextField(default="")
    DNIAddress = models.TextField(default="")
    DNICityAddress = models.TextField(default="")
    ExpirationDateCirculationPermit = models.TextField(default="")
    Regularschedule = models.TextField(default="")
    LinkedTaxiLicense = models.TextField(default="")
    RegistrationTaxiLinked = models.TextField(default="")
    language = models.TextField(default="Spanish")
    TravelCommission = models.TextField(default="")
    CommissionChargeCards = models.TextField(default="")
    BankCurrentAccount = models.TextField(default="")
    AdminNotices = models.TextField(default="")
    AdminNotes = models.TextField(default="")
    driverScore = models.FloatField(default="0.0")
    ImeiCode = models.TextField(default="")
    HashCode = models.TextField(default="")
    profileImg = models.ImageField(default=DEFAUT_IMAGE, upload_to='Driver/DriverProfile/')
    PhotoDNI = models.ImageField(default=DEFAUT_IMAGE, upload_to='Driver/DriverDNI/')
    CredintialPhoto = models.ImageField(default=DEFAUT_IMAGE, upload_to='Driver/Crediantial/')
    location = models.TextField(default="88.23478, 25.36578")
    driverOTP = models.TextField(default="")
    preferedHour = models.TextField(default="AM")
    cityOfWork = models.TextField(default="")
    comisionTpv = models.TextField(default="")
    BankAccountDetails = models.TextField(default="")
    



    def __str__(self):
        return self.phoneNo