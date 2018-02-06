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

    NationalCode = models.CharField('کد ملی', max_length=11)
    birthDate = models.DateField(null=True, blank=True)
    city = models.CharField('شهر', max_length=20, blank=True)
    education = models.CharField('تحصیلات', max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    dateOfEmployeement = models.DateField('تاریخ استخدام', null=True, blank=True)
    phoneNumber = models.CharField('شماره تماس', max_length=12, null=True, blank=True)
    rate = models.PositiveIntegerField('امتیاز')

    class Meta:
        verbose_name = 'مددکار'
        verbose_name_plural = 'مددکاران'

    def __str__(self):
        return self.karbar.user.username

    def madadkar_firstname(self):
        return self.karbar.user.first_name

    def madadkar_lastname(self):
        return self.karbar.user.last_name

    madadkar_firstname.short_description = 'نام'
    madadkar_lastname.short_description = 'نام خانوادگی'

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

    class Meta:
        verbose_name = 'درخواست ثبت‌نام مددجو'
        verbose_name_plural = 'درخواست‌های ثبت‌نام مددجو'


class MadadkarChangeProfileRequest(ChangeProfileRequest):
    birthDate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    dateOfEmployeement = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'درخواست تغییر مشخصات'
        verbose_name_plural = 'درخواست‌های تغییر مشخصات'


# this class moved from modir to madadkar

class Warning(Notification):
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.CASCADE)
    activity = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'هشدار'
        verbose_name_plural = 'هشدارها'
