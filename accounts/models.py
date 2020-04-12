from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date,datetime
from django.utils import timezone
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    isCompany = models.BooleanField(default=False)
    city = models.CharField(max_length=10,null=True,blank=True)
    dateOfBirth = models.DateField(default=date.today)
    degree = models.CharField(max_length=10,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    position = models.CharField(max_length=100,null=True,blank=True)

    def as_dict(self):
        return {
            "username": self.user.username,
            "degree" : self.degree            
        }
    #Python 3.x
    def __str__(self):
        return str(self.user.username)

    #Python 2.x
    def __unicode__(self):
        return str(self.user.username)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    class Meta:
        unique_together = (('user1', 'postNo'),)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null=True,blank=True)
    
    postNo = models.IntegerField()
    text = models.CharField(max_length=1000,null=True,blank=True)
    datePosted = models.DateTimeField(default=datetime.now, blank=True)

    @classmethod
    def create(cls, user1,username,postNo,text):
        Post = cls(user1=user1, username = username,postNo = postNo, text = text)
        return Post        
    class Meta:
        ordering = ["-datePosted"] 