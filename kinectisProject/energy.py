from django.http import HttpResponse
from django.shortcuts import render

def energyDetermination(request):
    return render(request,'index.html') 

