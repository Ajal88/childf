from django.db import models

from karbar.choice import *
from karbar.models import ChangeProfileRequest
from karbar.models import Karbar
from karbar.models import Request
from madadkar.models import Madadkar
from modir.models import Modir


class Madadjoo(models.Model):
    karbar = models.OneToOneField(Karbar, on_delete=models.CASCADE)

    NationalCode = models.CharField(max_length=11, unique=True)
    madadkar_field = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING, null=True, blank=True)
    city = models.CharField('شهر', max_length=20, blank=True)
    bankAccount = models.CharField(max_length=20, blank=True)
    grade = models.IntegerField('وضعیت تحصیل', choices=typeOfGrade, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.IntegerField('وضعیت کلی', choices=stateType)
    healthStatus = models.IntegerField('وضعیت سلامت روحی و جسمی', choices=healthStatusType, default=0)
    disease = models.CharField(max_length=30, blank=True)
    educationalStatus = models.CharField(max_length=30, blank=True)
    briefDescription = models.TextField(blank=True)
    birthDate = models.DateField(null=True, blank=True)
    savingAmount = models.PositiveIntegerField(default=0)
    averageGradeOfLastGrade = models.PositiveIntegerField(null=True, blank=True)
    sex = models.IntegerField('جنسیت', choices=sexType)
    fatherName = models.CharField('نام پدر', max_length=20)
    phoneNumber = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'مددجو'
        verbose_name_plural = 'مددجویان'

    def __str__(self):
        return self.karbar.user.username

    def madadkar_firstname(self):
        return self.karbar.user.first_name

    def madadkar_lastname(self):
        return self.karbar.user.last_name

    def give_madadkar(self):
        x = self.madadkar_field
        if x is None:
            return '-'
        return x.karbar.user.username

    madadkar_firstname.short_description = 'نام'
    madadkar_lastname.short_description = 'نام خانوادگی'
    give_madadkar.short_description = 'مددکار'


class Need(models.Model):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    name = models.CharField('نام نیاز', max_length=30)
    cost = models.PositiveIntegerField('هزینه')
    type = models.IntegerField('نوع نیاز', choices=typeOfNeedType)
    amountpayed = models.PositiveIntegerField('مقدار پرداخت شده')
    resolved = models.BooleanField('برطرف شدن', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نیاز'
        verbose_name_plural = 'نیازها'

    def give_need_madadjoo(self):
        return self.madadjoo.karbar.user.username

    give_need_madadjoo.short_description = 'نام کاربری مددجو'


class Payment(models.Model):
    need = models.ForeignKey(Need, on_delete=models.CASCADE)
    amount = models.IntegerField('مقدار پرداخت')
    date = models.DateField('تاریخ')

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'

    def give_madadjoo(self):
        return self.need.madadjoo.karbar.user.username

    give_madadjoo.short_description = 'نام کاربری مددجو'

    def give_need_name(self):
        return self.need.name

    give_need_name.short_description = 'نام نیاز'


class MadadkarChangeRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)


class ThanksLetterSendRequest(Request):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE)


class Success(models.Model):
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True)


class MadadjooChangeProfileRequest(ChangeProfileRequest):
    madadjoo = models.ForeignKey(Karbar, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, blank=True)
    bankAccount = models.CharField(max_length=20, blank=True)
    grade = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.IntegerField(choices=stateType, null=True, blank=True)
    healthStatus = models.IntegerField(choices=healthStatusType, null=True, blank=True)
    disease = models.CharField(max_length=30, blank=True)
    educationalStatus = models.CharField(max_length=30, blank=True)
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

    class Meta:
        verbose_name = 'حمایت‌ مددکار'
        verbose_name_plural = 'حمایت‌های مددکار'


# move this two classes from modir to madadjoo

class SupportbyModir(models.Model):
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class SupprtBySystem(models.Model):
    modir = models.ForeignKey(Modir, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
