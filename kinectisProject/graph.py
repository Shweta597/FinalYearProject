
import logging
from django.contrib import messages
from pymongo import MongoClient
from django.shortcuts import render
from django.http import HttpResponse
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


# def Analysis(request):

#     if request.method == "GET":
#         reaction = request.GET.get("reaction")
#         temperature = request.GET.get("temp")
#         reactionData = collection.find()
#         finalWeights = []
#         MechNumber = 0
#         G_Alpha = []
#         timePeriods = []

#         check = False

#         for item in reactionData:
#             if item["reaction"] == reaction and item["temperature"] == temperature:
#                 check = True
#                 size = item["size"]
#                 initialWeight = item["initialWeight"]
#                 finalWeights = item["finalWeights"]
#                 timePeriods = item["timePeriods"]
#                 G_Alpha = item["G_Alpha"]
#                 MechNumber = item["MechNumber"]
#                 break

#         if check == True:
#             if MechNumber != 0:

#                 context = {'mech': MechNumber}
#                 return render(request, "analysisResult.html", context)
#             else:
#                 MechNumber = dataAnalysisHelper(
#                     size, initialWeight, finalWeights, timePeriods, G_Alpha)
#                 filter = {'reaction': reaction, 'temperature': temperature}
#                 newValues = {
#                     "$set": {"G_Alpha": G_Alpha, "MechNumber": MechNumber}}
#                 collection.update_one(filter, newValues)
#                 context = {'mech': MechNumber}
#                 return render(request, "analysisResult.html", context)

#         else:
#             context = {'mech': 0}
#             return render(request, "analysisResult.html", context)


# autopep8 -i try.py


