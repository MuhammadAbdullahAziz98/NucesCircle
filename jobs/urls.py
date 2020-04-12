from django.urls import path,include
from . import views
from rest_framework import routers
app_name = 'jobs'

router = routers.DefaultRouter()
router.register('job',views.JobView)
urlpatterns = [
    path("addJob",views.addJob,name='addJob'),
    path("saveJob/<jobNo>",views.saveJob,name='saveJob'),
    path("check/<int:pk>/",views.check,name='check'),
    path("delete/<int:pk>/",views.delete,name='delete'),
    path("apply/<int:pk>/",views.apply,name='apply'),
    path("select/<int:pk>/<username>",views.select,name='select'),
    path("viewApplicants",views.viewApplicants,name='viewApplicants'),
    path("checkApplicants/<int:pk>/",views.checkApplicants,name='checkApplicants'),
    path("",include(router.urls)),
    path("myjobs",views.myJobs,name='myJobs'),
    path("jobsReq",views.jobsReq,name='jobsReq'),
]
#other than first three, rest api urls