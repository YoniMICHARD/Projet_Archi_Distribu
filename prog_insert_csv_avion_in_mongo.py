import pandas as pd
import csv 
from dateutil import parser
import json 
from pymongo import MongoClient 

#csvfile = open('data.tsv', 'r')
#reader = csv.DictReader( csvfile )

def get_database():
    CONNECTION_STRING="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
    client = MongoClient(CONNECTION_STRING)
    return(client)

def create_db_collection(client):
    db=client['ProjetArchi']
    collection_name=db["stat_avion"]
    return(collection_name)
client=get_database()
collection_name=create_db_collection(client)

csvfile = pd.read_csv("stat_avion_europe.csv", sep=";")
reader = csv.DictReader( csvfile )

csvfile.replace('\\N', None, inplace = True)

#csvfile["Region"]= csvfile["Region"].str.split(";", expand = False)
#csvfile["PIB (milliards d'euros)"]= csvfile["PIB (milliards d'euros)"].str.split(";", expand = False)


header= [ "Entity","Week","Date","Flights","Flights (7-day moving average)","Day 2019","Flights 2019 (Reference)","% vs 2019 (Daily)","% vs 2019 (7-day Moving Average)","Day Previous Year","Flights Previous Year"]
collection_name.create_index('Entity')
db=client['ProjetArchi']
csvfile = csvfile.head(30000)
output=csvfile.to_dict('records')

#for each in reader:
    #row={}
    #for field in header:
        #row[field]=each[field]
    #output.append(row)

#firstline=output[0]

collection_name.insert_many(output)
print("Les données sont ajoutées !")