from django.db import models
from datetime import date

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Connect(models.Model):
    class Meta:
        unique_together = (('user1', 'friend'),)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    friend = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friends")
    isConnected = models.IntegerField(default = 0)
    @classmethod
    def create(cls, user1, user2,isConnected):
        Connect = cls(user1=user1,friend = user2,isConnected = isConnected)
        return Connect        

class Experience(models.Model):
    class Meta:
        unique_together = (('user1', 'expNo'),)
    expNo = models.IntegerField()
    title = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    fromDate = models.DateField(default=date.today)
    toDate = models.DateField(default=date.today) 
    explanation = models.CharField(max_length=1000,null=True,blank=True)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def create(cls, expNo, title, company, fromDate ,toDate, explanation, user1):
        Experience = cls(expNo = expNo, title = title, company = company, fromDate = fromDate, toDate = toDate, explanation = explanation, user1=user1)
        return Experience        

class Education(models.Model):
    class Meta:
        unique_together = (('user1', 'edNo'),)
    edNo = models.IntegerField()
    degree = models.CharField(max_length=100,null=True,blank=True)
    institute = models.CharField(max_length=100,null=True,blank=True)
    fromDate = models.DateField(default=date.today)
    toDate = models.DateField(default=date.today) 
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def create(cls, edNo, degree, institute, fromDate ,toDate, user1):
        Education = cls(edNo = edNo, degree = degree, institute = institute, fromDate = fromDate, toDate = toDate, user1=user1)
        return Education        