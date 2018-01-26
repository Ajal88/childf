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
