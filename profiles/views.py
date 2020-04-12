from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import Http404
from .models import Connect, Experience, Education
from accounts import views
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
@login_required 
def viewProfile(request,username):
    if request.user.is_authenticated:
        print(request.user.first_name)
    users = User.objects.filter(username__search=username)
    user2=""
    for u in users:
        user2 = u
    if user2 == "":
        raise Http404("Sorry! User does not exist")
    cons = Connect.objects.filter(user1_id = request.user.id)
    educationSet = Education.objects.filter(user1_id = user2.id)
    experienceSet = Experience.objects.filter(user1_id = user2.id)
    if not cons:
        print("yellow")
        return render(request,'profiles/profile.html',{'user2' : user2, 'follow' : 0, 'educationSet' : educationSet,'experienceSet' : experienceSet})
    else:
        for c in cons:
            if c.friend_id == user2.id and c.isConnected == 1:
                return render(request,'profiles/profile.html',{'user2' : user2, 'follow' : 1, 'educationSet' : educationSet,'experienceSet' : experienceSet})
    return render(request,'profiles/profile.html',{'user2' : user2, 'follow' : -1, 'educationSet' : educationSet,'experienceSet' : experienceSet}) #self
@login_required    
def addFriend(request,username):
    user1 = request.user
    users = User.objects.filter(username__search=username)
    user2=''
    for u in users:
        user2 = u
    if user2 == "":
        raise Http404("Sorry! User does not exist")
    else:
        print('ok')
        con = Connect.create(user1,user2,1)
        con.save()
        return redirect('profiles:viewProfile',user2.username)
def addExperience(request,username):
    exp = Experience.objects.filter(user1_id = request.user.id).order_by('expNo')
    expNo = -1
    if not exp:
        expNo = 0
    else:
            for e in exp:
                expNo = e.expNo
            expNo = expNo +1
    print(expNo)
    return render(request, 'profiles/addExperience.html',{'expNo' : expNo})

def saveExperience(request, expNo):
    title = request.POST.get('title','')
    company = request.POST.get('company','')
    toDateR = request.POST.get('toDate','')
    toDate = datetime.datetime.strptime(toDateR, "%m/%d/%Y")
    fromDateR = request.POST.get('fromDate','')
    fromDate =datetime.datetime.strptime(fromDateR, "%m/%d/%Y")
    explanation = request.POST.get('explanation','')
    exp = Experience.create(expNo,title,company,fromDate,toDate,explanation,request.user)
    exp.save()
    return redirect('profiles:viewProfile',request.user.username)

def addEducation(request,username):
    ed = Education.objects.filter(user1_id = request.user.id).order_by('edNo')
    edNo = -1
    if not ed:
        edNo = 0
    else:
            for e in ed:
                edNo = e.edNo
            edNo = edNo + 1
    print(edNo)
    return render(request, 'profiles/addEducation.html',{'edNo' : edNo})

def saveEducation(request, edNo):
    degree = request.POST.get('degree','')
    institute = request.POST.get('institute','')
    toDateR = request.POST.get('toDate','')
    toDate = datetime.datetime.strptime(toDateR, "%m/%d/%Y")
    fromDateR = request.POST.get('fromDate','')
    fromDate =datetime.datetime.strptime(fromDateR, "%m/%d/%Y")
    print(request.user.first_name)
    ed = Education.create(edNo,degree,institute,fromDate,toDate,request.user)
    ed.save()
    return redirect('profiles:viewProfile',request.user.username)

'''
def editInfo(request):

def editExperience(request,expNo):

def editEducation(request,edNo):
    '''