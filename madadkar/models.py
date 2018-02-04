from django.db import models
from django.utils import timezone

from karbar.choice import *
# from madadjoo.models import Payment
from karbar.models import ChangeProfileRequest
from karbar.models import Karbar
from karbar.models import Notification
# from madadjoo.models import Madadjoo
from karbar.models import Request
from modir.models import Modir


class Madadkar(models.Model):
    karbar = models.OneToOneField(Karbar, on_delete=models.CASCADE)

    NationalCode = models.CharField(max_length=11)
    birthDate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    dateOfEmployeement = models.DateField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.karbar.user.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.dateOfEmployeement = timezone.now().date()
        return super(Madadkar, self).save(*args, **kwargs)


class MadadjooRegistrationRequest(Request):
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE, null=True, blank=True)
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=20, blank=True)
    sex = models.IntegerField(choices=sexType)
    NationalCode = models.CharField(max_length=11, blank=True)
    phoneNumber = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    bankAcount = models.CharField(max_length=20, blank=True)
    grade = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.IntegerField(choices=stateType)
    healthStatus = models.IntegerField(choices=healthStatusType, default=0)
    disease = models.CharField(max_length=30, blank=True)
    educationalStatus = models.CharField(max_length=30, blank=True)
    briefDescription = models.TextField(blank=True)
    birthDate = models.DateField(null=True, blank=True)


class MadadkarChangeProfileRequest(ChangeProfileRequest):
    birthDate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    dateOfEmployeement = models.DateField(null=True, blank=True)


# this class moved from modir to madadkar

class Warning(Notification):
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE)
    activity = models.CharField(max_length=20)
