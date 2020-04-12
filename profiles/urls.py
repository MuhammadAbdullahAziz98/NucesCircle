from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<username>',views.viewProfile,name='viewProfile'),
    path('<username>/add',views.addFriend,name='addFriend'),
    path('<username>/AddExperience',views.addExperience,name='addExperience'),
    path('<username>/AddEducation',views.addEducation,name='addEducation'),
    path('saveExperience/<expNo>',views.saveExperience,name='saveExperience'),
    path('saveEducation/<edNo>',views.saveEducation,name='saveEducation'),
    
]