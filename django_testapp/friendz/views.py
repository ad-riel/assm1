from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import UserLink

def peoplez_list(request): 
  peoplez_list = User.objects.all() 
  t = loader.get_template('friendz/peoplezlist.html') 
  c = Context({ 'peoplez_list': peoplez_list, }) 
  return HttpResponse(t.render(c)) 

def user_followers(request,leusername):
  usertoget = User.objects.get(username=leusername)
  peoplez_list = UserLink.objects.filter(toUser=usertoget) 
  t = loader.get_template('friendz/followers.html') 
  c = Context({ 'peoplez_list': peoplez_list, 'leusername':leusername}) 
  return HttpResponse(t.render(c)) 

def user_following(request,leusername):
  usertoget = User.objects.get(username=leusername)
  peoplez_list = UserLink.objects.filter(fromUser=usertoget) 
  t = loader.get_template('friendz/following.html') 
  c = Context({ 'peoplez_list': peoplez_list, 'leusername':leusername}) 
  return HttpResponse(t.render(c)) 