from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def homePage(request):
    return render(request, "home.html")

def loginPage(request):
    return render(request, "login.html")