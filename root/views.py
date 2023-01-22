
from django.http import HttpResponse
from django.shortcuts import render
import pymongo



def home(request):
    return render(request,'index.html') 

