
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



logger = logging.getLogger(__name__)

# from F_Table import F_Table
# from T_Table import T_Table, mechanismName

# Put the logging info within your django view

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, connect=False)
db = client['kineticsData']
collection = db['data']






def graphCreation(request):
    return render(request, "graphCreation.html")


def graph(request):

    if request.method == "POST":
        reaction = request.POST.get("reaction")
        temperature = request.POST.get("temp")
        reactionData = collection.find()
        finalWeights = []
        MechNumber = 0
        G_Alpha = []
        timePeriods = []

        check = False

        for item in reactionData:
            if item["reaction"] == reaction and item["temperature"] == temperature:
                check = True
                size = item["size"]
                initialWeight = item["initialWeight"]
                finalWeights = item["finalWeights"]
                timePeriods = item["timePeriods"]
                G_Alpha = item["G_Alpha"]
                MechNumber = item["MechNumber"]
                break

        if check == True:
            x = []
            y = []
            if MechNumber != 0:
                for c in timePeriods:
                    x.append(float(c.split(",")))
                for c in G_Alpha:
                    y.append(float(c.split(",")))
                    
                # x =  [ for e in timePeriods.split(",")]
                # y = [ for e in G_Alpha.split(",")]
                plt.plot(x,y)
                plt.savefig("gAlphaVsTimePeriod.png")
                

                
                return render(request, "graphCreationResult.html" )
                
                
            else:
                
                
                return render(request, "graphCreationResult.html")

        else:
            
            return render(request, "graphCreationResult.html")

    # return render(request, "graphCreationResult.html" )


# autopep8 -i try.py


