from django.db import models
from django.contrib.auth.models import User

# Create your models here.


sexType = {
    (0, 'خانم'),
    (1, 'آقا')
}

receiveMessageStatusType = {
    (0, 'دریافت شد'),
    (1, 'دریافت نشد')
}


class Karbar(models.Model):
    user = models.OneToOneField(User)
    fatherName = models.CharField(max_length=20)
    sex = models.IntegerField(choices=sexType)
    NationalCode = models.CharField(max_length=11)
    phoneNumber = models.CharField(max_length=12)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Notification(models.Model):
    subject = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    date = models.DateField()
    receiveMessageStatus = models.IntegerField(choices=receiveMessageStatusType)

    def __str__(self):
        return self.subject


class Request(Notification):
    pass


class Message(Notification):
    sender = models.ForeignKey(Karbar, related_name='sender')
    receiver = models.ForeignKey(Karbar, related_name='receiver')
