from django.shortcuts import render

# Create your views here.
# app_name/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the index page of app_name.")
