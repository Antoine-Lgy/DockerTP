from pymongo import MongoClient
import pandas as pd

#Data à importer
data = pd.read_csv("./movies.csv",sep=",")

#MongoDB

try:
  client = MongoClient('mongodb', 27017)
  db = client.my_db
  print("server version : ", client.server_info()["version"])
  print("",str(db))
except:
    print("Erreur importation sur MongoDB")

#Neo4j

