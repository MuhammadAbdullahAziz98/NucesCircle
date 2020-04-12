from rest_framework import serializers
from .models import Job
from accounts.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('user1','jobNo','title','description','jobLocation','reqEducation','datePosted')


