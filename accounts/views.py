from .models import *
from .forms import *
from accounts.views import *
from django.shortcuts import HttpResponse, render
from django.contrib.auth.decorators import login_required




def home(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        print("fine")
        if form.is_valid():
            form.save()
            return render(request,"success.html")

    else:
        form = PostForm()
        print("last")
    return render(request, "index.html", {'form': form})


# def logout(request):
#     if request.method == 'GET':
#         print("ok")
#         if form.is_valid():
#
#      return request(request,'logout.html')





def login(request):
    return render(request, "login.html")

@login_required

def home1(request):
    return render(request, 'home.html')