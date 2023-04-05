
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
    b = (size * sxsy - sx * sy)/(size * sx2 - sx * sx)

    return b






def graphCreation(request):
    return render(request, "graphCreation.html")


def graph(request):

    if request.method == "GET":
        reaction = request.GET.get("reaction")
        temperature = request.GET.get("temp")
        reactionData = collection.find()
        finalWeights = []
        MechNumber = 0
        G_Alpha = ""
        timePeriods = ""
        image_url = ""
        check = False
        result = []
        k = 0
        size = 0

        for item in reactionData:
            if item["reaction"] == reaction and item["temperature"] == temperature:
                check = True
                size = item["size"]
                initialWeight = item["initialWeight"]
                finalWeights = item["finalWeights"]
                timePeriods = item["timePeriods"]
                G_Alpha = item["G_Alpha"]
                MechNumber = item["MechNumber"]
                image_url = item["image_url"]
                break

        if check == True and image_url!="":
            result = image_url

        elif check == True:
            x = []
            y = []
            if MechNumber != 0:
                x = [float(i) for i in timePeriods.split(',')]
                y = [float(i) for i in G_Alpha.split(',')]
                k = calculateSlopePart(y,x,int(size))
                print(x)
                print(y)
                plt.plot(x,y)
                plt.savefig("gAlphaVsTimePeriod.png")
                data = cloudinary.uploader.upload("gAlphaVsTimePeriod.png",folder="kinetics" )

                # print(data)
    
                result = data['url']
                filter = {'reaction': reaction, 'temperature': temperature}
                newValues = {
                    "$set": {"image_url": result,"k":k}}
                collection.update_one(filter, newValues)
                print(result)
                os.remove('gAlphaVsTimePeriod.png')
                
            else:
                
                result = "Need to do data analysis first"
                

        else:
            result = "No records is available for this reaction"
            

        return render(request, "graphCreationResult.html",{'image_url':result})


# autopep8 -i try.py




