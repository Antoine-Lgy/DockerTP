from pymongo import MongoClient
import pandas as pd

client = MongoClient(port=27017)
db = client.my_db

data = pd.read_csv("movies.csv",sep=";")

result=db.reviews.insert_one(data)

