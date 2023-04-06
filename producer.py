from kafka import KafkaProducer
from datetime import datetime
from json import dumps
import pandas as pd
from time import sleep
import numpy as np
import csv

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'),api_version=(2,0,2))

def send_csv_to_kafka():
    with open('./stat_avion_europe.csv') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader, None)
        for row in (csv_reader):
            year = row[0]
            # message = {'year': year}
            producer.send('myproject', value=str(year))
            # print("Churn: ", row) # print(int(year))
            #print(((year)))
            sleep(2)
send_csv_to_kafka()



# producer = KafkaProducer(bootstrap_servers=['kafka:9092'],value_serializer=lambda x: dumps(x, separators=(",",":")).encode('utf-8'),api_version=(2,0,2))

# producer.send('myproject', value='wassil')
