from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("wall is working now")

# Create your views here.
