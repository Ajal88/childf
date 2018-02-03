from django.db import models

from karbar.models import Karbar
# from madadkar.models import Madadkar
from karbar.models import Notification


# from madadjoo.models import Payment


# Create your models here.


class Modir(models.Model):
    karbar = models.OneToOneField(Karbar, on_delete=models.CASCADE)

    NationalCode = models.CharField(max_length=11)
    firstName = models.CharField(max_length=20, blank=True, null=True)
    lastName = models.CharField(max_length=20, blank=True, null=True)
    phoneNumber = models.CharField(max_length=12, blank=True, null=True)
    birthDate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    dateOfEmployeement = models.DateField(null=True, blank=True)
    savingAmountOfSystem = models.PositiveIntegerField()

    def __str__(self):
        return self.karbar.user.username

class News(Notification):
    modir = models.ForeignKey(Modir, on_delete=models.DO_NOTHING)
    receivers = models.ManyToManyField(Karbar, related_name='reciverKarbar')
