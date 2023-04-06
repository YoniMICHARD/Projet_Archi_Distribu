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
    collection_name=db["meteo_fr"]
    return(collection_name)
client=get_database()
collection_name=create_db_collection(client)

csvfile = pd.read_csv("météo_france.csv", sep=";")
reader = csv.DictReader( csvfile )

csvfile.replace('\\N', None, inplace = True)

#csvfile["Region"]= csvfile["Region"].str.split(";", expand = False)
#csvfile["PIB (milliards d'euros)"]= csvfile["PIB (milliards d'euros)"].str.split(";", expand = False)


header= [ "ID OMM station","Date","Variation de pression en 3 heures","Vitesse du vent moyen 10 mn","Humidité","Variation de pression en 24 heures","Précipitations dans les 24 dernières heures","Nom","Température (°C)","department (name)"]
collection_name.create_index('ID OMM station')
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