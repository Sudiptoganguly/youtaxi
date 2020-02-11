from djongo import models
from django.conf import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH


class Workers(models.Model):
    phoneNo = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)


class Company(models.Model):
    name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    postalCode = models.TextField()
    nif = models.TextField()
    administrators = models.TextField()
    addDate = models.DateTimeField(auto_now_add=True)
    removeDate = models.DateTimeField(auto_now_add=True)
    Worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    bankCardDetails = models.TextField(default=False)
    bankAccountDetails = models.TextField(default=False)




