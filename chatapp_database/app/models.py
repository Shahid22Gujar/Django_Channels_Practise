from operator import mod
from sqlite3 import Timestamp
from turtle import ondrag
from django.db import models

# Create your models here.


class Chat(models.Model):
    message=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)



class Group(models.Model):
    groupname=models.CharField(max_length=255)
    def __str__(self):
        return self.groupname

