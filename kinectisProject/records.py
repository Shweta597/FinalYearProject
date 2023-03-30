from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING,connect=False)
db = client['kineticsData']
collection = db['data']




def addRecords(request):
    if request.method == "POST":
        reaction = request.POST.get("reaction")
        temperature = request.POST.get("temp")
        size = request.POST.get("size")
        initialWeight = request.POST.get("initial weight")
        finalWeights = request.POST.get("final weights")
        timePeriods = request.POST.get("time periods")
        data = {
            "reaction":reaction,
            "temperature":temperature,
            "size":size,
            "initialWeight":initialWeight,
            "finalWeights":finalWeights,
            "timePeriods":timePeriods,
            "G_Alpha":"",
            "MechNumber":0,
            "image_url":""
        }
        allData = collection.find()
        
        check = True
        
        for item in allData:
            if item["reaction"] == reaction and item["temperature"] == temperature:
                check = False
                break
        
        if check==True:
            collection.insert_one(data)
            messages.success(request,"Record Added Successfully")
        else:
            messages.error(request,"Invalid data")
        
            
            
                
                
            
                
        
    return render(request,'record.html') 

