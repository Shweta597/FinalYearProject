from django.http import HttpResponse
from django.shortcuts import render
import pymongo
from django.contrib import messages



def home(request):
    return render(request,'index.html') 