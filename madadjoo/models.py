from django.db import models
from karbar.models import Karbar
from madadkar.models import Madadkar
from karbar.models import Request
from modir.models import Modir
from karbar.models import ChangeProfileRequest

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
    madadkar_field = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=20)
    bankAccount = models.CharField(max_length=20)
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
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    type = models.IntegerField(choices=typeOfNeedType)
    resolved = models.BooleanField()


class Payment(models.Model):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()


class MadadkarChangeRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)


class ThanksLetterSendRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE)


class Success(models.Model):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=200)


class MadadjooChangeProfileRequest(ChangeProfileRequest):
    madadjoo = models.ForeignKey(Karbar, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    bankAccount = models.CharField(max_length=20)
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

###move this three classes from madadkar to madadjoo

class MadadkarRateTheMadadjoo(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    madadjoo = models.ForeignKey(Madadjoo)
    date = models.DateField()
    reason = models.CharField(max_length=50)
    score = models.IntegerField()


class MadadkarRateThePayment(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    payment = models.ForeignKey(Payment)
    score = models.IntegerField()


class MadadkarSupport(models.Model):
    madadkar = models.ForeignKey(Madadkar)
    payment = models.ForeignKey(Payment)

##move this two classes from modir to madadjoo

class SupportbyModir(models.Model):
    modir = models.ForeignKey(Modir)
    payment = models.ForeignKey(Payment)


class SupprtBySystem(models.Model):
    modir = models.ForeignKey(Modir)
    payment = models.ForeignKey(Payment)
