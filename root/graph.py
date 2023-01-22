from django.http import HttpResponse
from django.shortcuts import render

def graphCreation(request):
    return render(request,'index.html') 

