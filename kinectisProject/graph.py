from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING,connect=False)
db = client['kineticsData']
collection = db['data']




def graphCreation(request):
    
    if request.method == "GET":
        reaction = request.GET.get("reaction")
        temperature = request.GET.get("temp")
        
        allData = collection.find()
        
        for item in allData:
            if item["reaction"] == reaction and item["temperature"] == temperature:
                print(item["timePeriods"])
                print(item["G_Alpha"])
                messages.success(request,"Graph Created Successfully")
            else:
                messages.error(request,"Invalid data")
                   
        
    return render(request,'graph.html') 
