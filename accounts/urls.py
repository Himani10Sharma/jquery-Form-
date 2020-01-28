from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from accounts import views




urlpatterns = [
	url(r'^home/$', views.home, name ='home'),

]
