import pandas as pd
from pymongo import Connection
from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.business

data = pd.read_csv("movies.csv",sep=";")

result=db.reviews.insert_one(data)

