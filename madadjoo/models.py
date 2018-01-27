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
    madadkar_field = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING, null=True,blank=True)
    city = models.CharField(max_length=20, blank=True)
    bankAccount = models.CharField(max_length=20, blank=True)
    grade = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.IntegerField(choices=stateType)
    healthStatus = models.IntegerField(choices=healthStatusType,default=0)
    disease = models.CharField(max_length=30, blank=True)
    educationalStatus = models.CharField(max_length=30, blank=True)
    briefDescription = models.TextField(blank=True)
    birthDate = models.DateField(null=True, blank=True)
    savingAmount = models.PositiveIntegerField(default=0)
    averageGradeOfLastGrade = models.PositiveIntegerField(null=True,blank=True)


class Need(models.Model):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    type = models.IntegerField(choices=typeOfNeedType)
    resolved = models.BooleanField(default=False)


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
    description = models.TextField(max_length=200,blank=True)


class MadadjooChangeProfileRequest(ChangeProfileRequest):
    madadjoo = models.ForeignKey(Karbar, on_delete=models.CASCADE)
    city = models.CharField(max_length=20,blank=True)
    bankAccount = models.CharField(max_length=20,blank=True)
    grade = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100,blank=True)
    state = models.IntegerField(choices=stateType,null=True, blank=True)
    healthStatus = models.IntegerField(choices=healthStatusType,null=True, blank=True)
    disease = models.CharField(max_length=30,blank=True)
    educationalStatus = models.CharField(max_length=30,blank=True)
    briefDescription = models.TextField(blank=True)
    birthDate = models.DateField(null=True, blank=True)
    savingAmount = models.PositiveIntegerField(null=True, blank=True)
    averageGradeOfLastGrade = models.PositiveIntegerField(null=True, blank=True)


# move this three classes from madadkar to madadjoo

class MadadkarRateTheMadadjoo(models.Model):
    madadkar = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=50)
    score = models.IntegerField()


class MadadkarRateThePayment(models.Model):
    madadkar = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    score = models.IntegerField()


class MadadkarSupport(models.Model):
    madadkar = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


# move this two classes from modir to madadjoo

class SupportbyModir(models.Model):
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class SupprtBySystem(models.Model):
    modir = models.ForeignKey(Modir, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
