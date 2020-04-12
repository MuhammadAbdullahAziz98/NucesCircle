from django.db import models
from datetime import date
from django.utils import timezone

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    class Meta:
        unique_together = (('user1', 'jobNo'),)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    jobNo = models.IntegerField()
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    jobLocation = models.CharField(max_length=150, blank=False)
    reqEducation = models.CharField(max_length=100, blank=False)
    datePosted = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, user1,jobNo,title,description,jobLocation,reqEducation):
        Job = cls(user1=user1,jobNo = jobNo, title = title,description = description,jobLocation = jobLocation,reqEducation = reqEducation)
        return Job        


class Application(models.Model):
    class Meta:
        unique_together = (('user1', 'jobId'),)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    jobId = models.ForeignKey(Job,on_delete=models.CASCADE)

    @classmethod
    def create(cls, user1,jobId):
        Application = cls(user1=user1,jobId = jobId)
        return Application        


class Selection(models.Model):
    class Meta:
        unique_together = (('user1', 'jobId'),)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    jobId = models.ForeignKey(Job,on_delete=models.CASCADE)

    @classmethod
    def create(cls, user1,jobId):
        Selection = cls(user1=user1,jobId = jobId)
        return Selection        

