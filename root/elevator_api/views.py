from django.shortcuts import render, HttpResponse
from django.http import request

# Create your views here.

def home(request):
    return HttpResponse("Hello api home page")

