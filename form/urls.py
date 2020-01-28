from django.contrib import admin

from django.conf.urls import include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	 url('', views.home, name ='index'),
    url('admin/', admin.site.urls),
    url("login/", views.login, name="login"),
    url("logout/", auth_views.LogoutView.as_view(), name="logout"),
    url('social-auth/', include('social_django.urls', namespace="social")),
    url("", views.home1, name="home1"),

]
