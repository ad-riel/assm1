from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('', 
  url(r'^users/$', views.peoplez_list, name='users'), 
  url(r'^(?P<leusername>\w+)/followers/$', views.user_followers, name='user_followers'), 
  url(r'^(?P<leusername>\w+)/following/$', views.user_following, name='user_following'), 
)  