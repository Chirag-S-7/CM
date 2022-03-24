from django.db import models
from django.db.models.deletion import CASCADE
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# Create your models here.
class Event(models.Model):
    # host_email = models.EmailField(max_length=254, default="")
    # password = models.CharField(max_length=122)
    eventname = models.CharField(max_length=122, default="", null=True)
    location = models.CharField(max_length=15, default="", null=True)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False, default="", null=True)
    # endDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    # deadDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    nop = models.IntegerField()
    dec = models.TextField()
    # user_event = models.CharField(max_length=122, default="")

    # def __str__(self):
    #     return self.location

class Part(models.Model):
    name = models.CharField(max_length=122, default="")
    contactnumber = models.CharField(max_length=122, default="")
    part_email = models.EmailField(max_length=254, default="")
    # password = models.CharField(max_length=122)
    eventName = models.CharField(max_length=122)
    reg_type = models.CharField(max_length=20, default = "")
    number = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        account_sid = 'AC3e69d9334e9e2f47bbc48bd877af0ff7'
        auth_token = '03c23bb392121bb6fa296ef8e8a2f8d8'
        client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #                     body="Hello There, You have successfully registered in the event.",
        #                     from_='+17655713757',
        #                     to='+919913715425'
        #                 )
        message = client.messages.create(
            body='Hello There, You have successfully registered in the Event.',
            from_='+17655713757',
            to='+919512823603'
            # to='+91'+args[0],#num
        )
        # print(args)
        return super().save(*args, **kwargs)

class Club(models.Model):
    name = models.CharField(max_length=30)
    admin = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    admin_email = models.EmailField(max_length=254)

class Member(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)  #club name
    position = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
