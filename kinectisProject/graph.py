
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

    if request.method == "GET":
        reaction = request.GET.get("reaction")
        temperature = request.GET.get("temp")
        reactionData = collection.find()
        finalWeights = []
        MechNumber = 0
        G_Alpha = ""
        timePeriods = ""

        check = False
        context = []

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
                x = [float(i) for i in timePeriods.split(',')]
                y = [float(i) for i in G_Alpha.split(',')]
                print(x)
                print(y)
                # for c in timePeriods:
                #     x.append((c))
                # for c in G_Alpha:
                #     y.append((c))
                # print(x)
                # print(y)
                    
                # x =  [ for e in timePeriods.split(",")]
                # y = [ for e in G_Alpha.split(",")]
                plt.plot(x,y)
                plt.savefig("gAlphaVsTimePeriod.png")
                # context.append("Graph is created!")
                

                
                # return render(request, "graphCreationResult.html" )
                
                
        #     else:
                
        #         context.append("Need to do data analysis first")
        #         # return render(request, "graphCreationResult.html")

        # else:
        #     context.append("No records is available for this reaction")
            # return render(request, "graphCreationResult.html") 

        return render(request, "graphCreationResult.html")


# autopep8 -i try.py


