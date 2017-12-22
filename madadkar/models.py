from django.db import models
from karbar.models import Karbar
from modir.models import Modir
from madadjoo.models import Madadjoo
from karbar.models import Request
from madadjoo.models import Payment

# Create your models here.

sexType = {
    (0, 'خانم'),
    (1, 'آقا')
}

stateType = {
    (0, 'نیازمند'),
    (1, 'مستعد'),
    (2, 'یتیم')
}

healthStatusType = {
    (0, 'سالم'),
    (1, 'بیمار')
}


class Madadkar(Karbar):
    birthDate = models.DateField()
    city = models.CharField(max_length=20)
    education = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    dateOfEmployeement = models.DateField()


class MadadjooRegistrationRequest(Request):
    madadkar = models.ForeignKey(Madadkar)
    modir = models.ForeignKey(Modir)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=20)
    sex = models.IntegerField(choices=sexType)
    NationalCode = models.CharField(max_length=11)
    phoneNumber = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    bankAcount = models.CharField(max_length=20)
    grade = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    state = models.IntegerField(choices=stateType)
    healthStatus = models.IntegerField(choices=healthStatusType)
    disease = models.CharField(max_length=30)
    educationalStatus = models.CharField(max_length=30)
    briefDescription = models.TextField()
    birthDate = models.DateField()


class RateTheMadadjoo(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    madadjoo = models.ForeignKey(Madadjoo)
    date = models.DateField()
    reason = models.CharField(max_length=50)
    score = models.IntegerField()


class RateThePayment(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    payment = models.ForeignKey(Payment)
    score = models.IntegerField()


class Support(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    payment = models.ForeignKey(Payment)
