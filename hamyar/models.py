from django.db import models

from karbar.models import ChangeProfileRequest
from karbar.models import Karbar
from karbar.models import Request
from madadjoo.models import Madadjoo
from madadjoo.models import Payment
from madadkar.models import Madadkar
from modir.models import Modir


# Create your models here.

class Hamyar(models.Model):
    karbar = models.OneToOneField(Karbar, on_delete=models.CASCADE)

    phoneNumber = models.CharField('شماره تلفن',max_length=12, null=True, blank=True)
    payed = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = 'همیار'
        verbose_name_plural = 'همیاران'

    def __str__(self):
        return self.karbar.user.username + ' hamyar id' + str(self.id)

    def hamyar_username(self):
        return self.karbar.user.username

    hamyar_username.short_description = 'نام کاربری همیار'


class Support(models.Model):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class MeetTheMadadjooRequest(Request):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)


class SendNonCashAidRequest(Request):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    madadjoo = models.ForeignKey(Madadjoo, on_delete=models.CASCADE)


class HamyarChangeProfileRequest(ChangeProfileRequest):
    pass
