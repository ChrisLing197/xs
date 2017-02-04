from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views

app_name = 'ys'
urlpatterns = [
        url(r'^accounts/new/$', views.CreateUser, name='register'),
        url(r'^accounts/', include('django.contrib.auth.urls')),
        url(r'^$',RedirectView.as_view(url='/accounts/new/')),#/accounts/new/  --> /home/
        url(r'^login/',views.u_login,name='login'),
        url(r'^profile/',views.profile,name='profile'),
#        url(r'^logout/', views.logout_v, name='logout'),
        url(r'^home/$',views.index,name='home')#home will
    ]
