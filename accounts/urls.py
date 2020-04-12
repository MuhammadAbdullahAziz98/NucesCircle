from django.urls import path,include
from . import views
from django.conf.urls import url
from rest_framework import routers
app_name = 'accounts'

router = routers.DefaultRouter()
router.register('post',views.PostView,base_name='post')
urlpatterns = [
    path("index",views.index,name='index'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path("newsfeed",views.newsFeed,name='newsfeed'),
    path("search",views.search,name='search'),
    path("searcher",views.searcher,name='searcher'),
    path("company",views.company,name='company'),
    path("post",views.post,name='post'),
    path("",include(router.urls)),
    url(r'^lazy_load_posts/$', views.lazy_load_posts, name='lazy_load_posts'),
]