from django.db import models
from karbar.models import Karbar
from madadjoo.models import Payment
from madadjoo.models import Madadjoo
from karbar.models import Request
from modir.models import Modir
from madadkar.models import Madadkar
from karbar.models import ChangeProfileRequest


# Create your models here.

class Hamyar(Karbar):
    pass


class Support(models.Model):
    hamyar = models.ForeignKey(Hamyar)
    payment = models.ForeignKey(Payment)


class meetTHeMadadjooRequest(Request):
    hamyar = models.ForeignKey(Hamyar)
    modir = models.ForeignKey(Modir)
    madadjoo = models.ForeignKey(Madadjoo)


class SendNonCashAidRequest(Request):
    hamyar = models.ForeignKey(Hamyar)
    madadkar = models.ForeignKey(Madadkar)
    madadjoo = models.ForeignKey(Madadjoo)


class HamyarChangeProfileRequest(ChangeProfileRequest):
    pass
