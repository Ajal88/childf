import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .choice import *


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Karbar(models.Model):
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=us_type, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Karbar.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.karbar.save()


class Notification(models.Model):
    subject = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    date = models.DateField()
    receiveMessageStatus = models.IntegerField(choices=receiveMessageStatusType, default=1)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        return super(Notification, self).save(*args, **kwargs)


class Request(Notification):
    pass


class ChangeProfileRequest(Request):
    karbar = models.ForeignKey(Karbar, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=30, blank=True)
    fatherName = models.CharField(max_length=20, blank=True)
    sex = models.IntegerField(choices=sexType, null=True, blank=True)
    NationalCode = models.CharField(max_length=11, blank=True)
    phoneNumber = models.CharField(max_length=12, blank=True)


class Message(Notification):
    sender = models.ForeignKey(Karbar, related_name='sender', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(Karbar, related_name='receiver', on_delete=models.CASCADE)
