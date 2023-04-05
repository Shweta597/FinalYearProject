from django.http import HttpResponse
from django.shortcuts import render
import logging

from matplotlib.style import context
from pymongo import MongoClient
from django.shortcuts import render

from matplotlib.animation import FuncAnimation
import matplotlib
from math import sqrt, log
import array as arr
import math
from math import sqrt, log
import string
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy import symbols, sympify
import re
matplotlib.use('SVG')
import io, base64
from django.shortcuts import render
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, redirect

import cloudinary.uploader
import os





logger = logging.getLogger(__name__)

# from F_Table import F_Table
# from T_Table import T_Table, mechanismName

# Put the logging info within your django view

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, connect=False)
db = client['kineticsData']
collection = db['data']

def calculateSlopePart(gAlpha, timePeriods, size):
    sy = sum(gAlpha)

    sx = sum(timePeriods)

    sxsy = 0

    sx2 = 0

    for i in range(size):
        sxsy += (gAlpha[i] * timePeriods[i])
        sx2 += (timePeriods[i]*timePeriods[i])
    bot = (size * sx2 - sx * sx)
    if bot!=0:
         b = (size * sxsy - sx * sy)/bot
    else:
        b = (size * sxsy - sx * sy)

    

    return b



def energy(request):
    return render(request,'energy.html') 

def energyDetermination(request):
    if request.method == "GET":
        reaction = request.GET.get("reaction")
        reactionData = collection.find()
        finalWeights = []
        MechNumber = 0
        G_Alpha = ""
        timePeriods = ""
        image_url = ""
        check = False
        result = []
        k = []
        size = 0
        temp = []

        for item in reactionData:
            if item["reaction"] == reaction:
                check = True
                size = size+1
                k.append(item['k'])
                temp.append(int(item["temperature"]))
                break

        if check == True:
            if k != []:
                result = calculateSlopePart(k,temp,size)
                
            else:
                result = "Need slopes are found"
                    

        else:
            result = "No records is available for this reaction"
            

        return render(request, "energyDetermination.html",{'ActivationEnergy':result})


    return render(request,'energyDetermination.html') 

