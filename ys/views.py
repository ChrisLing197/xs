from django.shortcuts import render,redirect,render_to_response
from django import forms
from . import forms
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import loader,Context,RequestContext
from django.views.generic import edit
from django.core.urlresolvers import reverse_lazy,reverse

from .tasks import Hello_World

# Create your views here.

def index(request):
    logout(request)
    #Hello_World().delay()
    #Hello_World.hello_world('like this')
    return render(request,"ys/home.html")

def profile(request):
    return render(request,"ys/profile.html")

def logout_v(request):
    logout(request)
#    return redirect('home')

def CreateUser(request):
    if request.method=='POST':
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Getting here')
            return HttpResponseRedirect("/home/")
    else:
        form=forms.RegistrationForm()
        return render(request,"ys/registration_form.html",{'form':form})

    args={}
    args['form'] = form
    return render(request,"ys/registration_form.html",args)
    #model=models.Registration
    #form_class=forms.RegistrationForm
    #template_name="ys/registration_form.html"
    #success_url=reverse_lazy('ys:profile')

    #def form_valid(self,form):
     #   logout(self.request)
     #   return super(CreateUser,self).form_valid(form)

def u_login(request):
    
    context=RequestContext(request)
    #if request.method=='POST':
    username=request.POST.get('username')
    print(username)
    #if '@' in username:
    #    username=User.objects.get(email=username).username
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user:
        if user.is_active:
            logout(request)
            login(request,user)
    return HttpResponseRedirect("/profile/")
