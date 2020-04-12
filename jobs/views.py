from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import Http404
from .models import Job,Application,Selection
from accounts import views
from django.contrib.auth.decorators import login_required
import datetime
from rest_framework import viewsets
from .serializers import JobSerializer
from django.contrib import messages
from profiles.models import Education
# Create your views here.
import json
def select(request,pk,username):
    user = User.objects.get(username=username)
    job = Job.objects.get(pk=pk)
    selection = Selection.create(user,job)
    selection.save()
    messages.success(request,": Applicant selected successful")
    return redirect('jobs:addJob')
def viewApplicants(request):
    jobs = Job.objects.filter(user1_id = request.user.id)
    return render(request,'jobs/viewApplicants.html',{'jobs':jobs})
def checkApplicants(request,pk):
    applicants = Application.objects.filter(jobId = pk)
    user =[]
    if applicants:
        for ap in applicants:
            u = User.objects.get(pk=ap.user1_id)
            user.append(u)
    return render(request,'jobs/applicants.html',{'applicants':user, 'jobid':pk})
def apply(request,pk):
    jobId = Job.objects.get(pk=pk)
    application = Application.create(request.user,jobId)
    application.save()
    messages.success(request,"Job Application successful")
    return redirect('jobs:addJob')
def check(request,pk):
    print(pk)
    job  = Job.objects.get(pk = pk)
    user = User.objects.get(pk = job.user1_id)
    user.first_name + " "+user.last_name
    company = user.profile.company;
    return render(request,'jobs/viewJob.html',{'job':job,'username':user.first_name ,'company':company});
def addJob(request):
    #print(request.user.first_name)
    if request.user.profile.isCompany:
        jobs = Job.objects.filter(user1_id = request.user.id).order_by('jobNo')
        jobNo = -1
        if not jobs:
            jobNo = 0
        else:
                for j in jobs:
                    jobNo = j.jobNo
                jobNo = jobNo + 1
        print(jobNo)
        return render(request,'jobs/addJob.html', {'jobNo':jobNo})
    else:
        jobs = Job.objects.all()
        selectedJob = []
        ed=""
        eds = Education.objects.filter(user1_id = request.user.id)
        for e in eds:
            ed = e
        if eds:
            for j in jobs:
                if j.reqEducation.lower() == ed.degree.lower():
                    selectedJob.append(j)
            jobs = selectedJob
        print(selectedJob)
        return render(request,'jobs/viewJobs.html',{'jobs':jobs})

def saveJob(request,jobNo):
    title = request.POST.get('title','')
    description = request.POST.get('description','')
    jobLocation = request.POST.get('jobLocation','')
    reqEducation = request.POST.get('reqEducation','')
    job = Job.create(request.user,jobNo,title,description,jobLocation,reqEducation)
    job.save()

    #print("saved")
    return render(request,'accounts/news_feed.html')
#REST:
class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def delete(request,pk):
    Job.objects.filter(pk=pk).delete()
    return redirect('jobs:viewApplicants')
def myJobs(request):
    return render(request,"jobs/myjobs.html")
from django.http import JsonResponse
from django.template import loader
def jobsReq(request):
    jobs = Job.objects.all()
    result={}
    serializer = JobSerializer(jobs, many=True)
    result["status"] = "Success"
    result["jobs"] = serializer.data
    
    return JsonResponse(json.dumps(result),content_type='application/json',safe=False)