from django.db import models
from karbar.models import Karbar
from madadkar.models import Madadkar
from karbar.models import Request
from modir.models import Modir

# Create your models here.

stateType = {
    (0, 'نیازمند'),
    (1, 'مستعد'),
    (2, 'یتیم')
}

healthStatusType = {
    (0, 'سالم'),
    (1, 'بیمار')
}

typeOfNeedType = {
    (0, 'ماهانه'),
    (1, 'هفتگی'),
    (2, 'یکباره')
}


class Madadjoo(Karbar):
    madadkar = models.ForeignKey(Madadkar)
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
    savingAmount = models.PositiveIntegerField()
    averageGradeOfLastGrade = models.PositiveIntegerField()


class Need(models.Model):
    madadjoo = models.ForeignKey(Madadjoo)
    name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    type = models.IntegerField(choices=typeOfNeedType)
    resolved = models.BooleanField()


class Payment(models.Model):
    need = models.ForeignKey(Need)
    amount = models.IntegerField()
    date = models.DateField()


class MadadkarChangeRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo)
    modir = models.ForeignKey(Modir)


class ThanksLetterSendRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo)
    madadkar = models.ForeignKey(Madadkar)


class Success(models.Model):
    madadjoo = models.ForeignKey(Madadjoo)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
