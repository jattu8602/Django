from django.http import HttpResponse
from django.shortcuts import render


def home(request):
  # return HttpResponse("Hello world , we are in chai and django page")
   return render(request, 'website/index.html')
def about(request):
  # return HttpResponse("Hello world , we are in chai and django about page")
   return render(request, 'website/about.html')
def signup(request):
  # return HttpResponse("Hello world , we are in chai and django signup page")
   return render(request, 'website/signup.html')
def login(request):
  # return HttpResponse("Hello world , we are in chai and django login page")
   return render(request, 'website/login.html')
