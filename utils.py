from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING,connect=False)
db = client['kineticsData']
collection = db['data']

return collection,db
