from django.shortcuts import render,redirect
from django.contrib import messages, auth
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template import loader
# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        firstName = request.POST.get('first_name','')
        lastName = request.POST.get('last_name',"")
        email = request.POST.get('email',"")
        degree = request.POST.get('degree',"")
        password = request.POST.get('password',"")
        city = request.POST.get('city',"")
        dob = request.POST.get('dateOfBirth',"")

        if User.objects.filter(email=email).exists():
                messages.error(request,f"Account with email, {email} already exists")
                return redirect('accounts:index')
        else:
                messages.success(request,"Signed in successfully")
                user = User.objects.create_user(username=username,email=email,password=password, first_name=firstName,last_name=lastName)

#                        user.save()
                user.profile.degree = degree
                user.profile.city = city
                user.profile.dateOfBirth = datetime.datetime.strptime(dob, "%m/%d/%Y")
                user.save()
                print(user.profile.isCompany)
                return redirect('accounts:index')
    else:
        if request.user.is_authenticated:
                print(request.user.first_name)
                return redirect('accounts:newsfeed')
        else:
                return render(request, 'accounts/index.html')

def login(request):
        if request.method == 'POST':
                email = request.POST.get('email',"")
                password = request.POST.get('password',"")
                user = auth.authenticate(username=email,password=password)
                if user is not None:
                        auth.login(request,user)
#                        messages.success(request,'Logged in successfully')
                        return redirect('accounts:newsfeed')      
                else:
                        messages.error(request,'Invalid Credentials')
                        return render(request, 'accounts/login.html')
        else:
                if request.user.is_authenticated:
                        print(request.user.first_name)
                        return redirect('accounts:newsfeed')
                else:
                        return render(request, 'accounts/login.html')
@login_required
def newsFeed(request):
        if request.user.is_authenticated:
                print(request.user.first_name)
                posts=  Post.objects.all().order_by("-datePosted")[:5]
 
                '''paginator = Paginator(posts, 5) # Show 25 contacts per page

                page = request.GET.get('page')
                posts = paginator.get_page(page)
                '''
                return render(request,'accounts/news_feed.html',{'posts':posts})
        else:
                messages.error(request,"Please Login First")
                return redirect('accounts:login')                

def company(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        firstName = request.POST.get('first_name','')
        lastName = request.POST.get('last_name',"")
        email = request.POST.get('email',"")
        company = request.POST.get('company',"")
        position = request.POST.get('position',"")
        password = request.POST.get('password',"")
        city = request.POST.get('city',"")
        dob = request.POST.get('dateOfBirth',"")
        if User.objects.filter(email=email).exists():
                messages.error(request,f"Account with email, {email} already exists")
                return redirect('accounts:index')
        else:
                messages.success(request,"Signed in successfully")
                user = User.objects.create_user(username=username,email=email,password=password, first_name=firstName,last_name=lastName)
                user.profile.isCompany = True
                user.profile.company = company
                user.profile.position = position
                user.profile.city = city
                user.profile.dateOfBirth = datetime.datetime.strptime(dob, "%m/%d/%Y")
                user.save()
                print(user.profile.isCompany)
                return redirect('accounts:index')
    else:
        if request.user.is_authenticated:
                print(request.user.first_name)
                return redirect('accounts:newsfeed')
        else:
                return render(request, 'accounts/company.html')
@login_required
def logout(request):
        if request.method == 'POST':
                auth.logout(request)
                messages.success(request,"Logged out successfully")
                return redirect('accounts:login')
@csrf_exempt
@login_required
def post(request):
        posts = Post.objects.filter(user1_id = request.user.id).order_by('postNo')
        postNo = -1
        if not posts:
                postNo = 0
        else:
                for p in posts:
                        postNo = p.postNo
                        print(postNo)

                postNo = postNo + 1
        text = request.POST.get('text','')
        username = request.user.first_name + ' ' + request.user.last_name
        post = Post.create(request.user,username,postNo,text)
        post.save()
#        posts = Post.objects.filter()  # Getting all the posts from database
        return redirect('accounts:newsfeed')

def listing(request):
    post = Post.objects.all()
    paginator = Paginator(contact_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'newsfeed.html', {'posts': posts})


class PostView(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        pagination_class = LimitOffsetPagination
        serializer_class = PostSerializer
    

def lazy_load_posts(request):
        page = request.POST.get('page')
        posts = Post.objects.all()
        # use Django's pagination
        # https://docs.djangoproject.com/en/dev/topics/pagination/
        results_per_page = 5
        paginator = Paginator(posts, results_per_page)
        has_next = True
        try:
                posts = paginator.page(page)
        except PageNotAnInteger:
                posts = paginator.page(2)
                print(page)
        except EmptyPage:
                posts = paginator.page(paginator.num_pages)
                has_next = False
        # build a html posts list with the paginated posts
        print(posts.has_next())
        posts_html = loader.render_to_string(
        'accounts/posts.html',
        {'posts': posts}
        )
        # package output data and return it as a JSON object
        if has_next:
                output_data = {
                        'posts_html': posts_html,
                        'has_next': posts.has_next()
                }
        else:
                output_data = {
                        'posts_html': None,
                        'has_next': False
                }
        return JsonResponse(output_data)

def search(request):
        username = request.GET.get("username")
        print(username)
        persons = User.objects.all()
        people=[]
        
        for p in persons:
                if username.lower() in p.username.lower():
                        people.append(p); 
                elif username.lower() in p.first_name.lower(): 
                        people.append(p); 
                elif username.lower() in p.last_name.lower(): 
                        people.append(p)
        return render(request,'accounts/search.html',{'people' : people})
import json
from django.core import serializers
def searcher(request):
        people = User.objects.all()
        return JsonResponse(data,content_type='application/json')
        """for i in people:
                        {
                                name:i.username,
                                email:i.email,
                                degree:i.profie.degree
                        }
"""
        """people = User.objects.all()

        dictionaries = [ obj.profile.as_dict() for obj in people ]
        dicti = dict()
        dicti = dictionaries 
        return JsonResponse(dictionaries,content_type='application/json',safe=False)
        """     
