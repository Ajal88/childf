from django.db import models
from karbar.models import Karbar
#from madadkar.models import Madadkar
from karbar.models import Notification
#from madadjoo.models import Payment


# Create your models here.


class Modir(Karbar):
    birthDate = models.DateField()
    city = models.CharField(max_length=20)
    education = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    dateOfEmployeement = models.DateField()
    savingAmountOfSystem = models.PositiveIntegerField()


class News(Notification):
    modir = models.ForeignKey(Modir)
    receivers = models.ManyToManyField(Karbar,related_name='reciverKarbar')
