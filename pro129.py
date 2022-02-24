import csv
import pandas as pd

data_set1=[]
data_set2=[]

with open ('C:\Users\vihan\Downloads\venv\c128web\web_scraping_2-main\dwarf_stars.csv')as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        data_set1.append(row)

with open ('project129.csv')as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        data_set2.append(row)

headers1= data_set1[0]
planet_data1= data_set1[1:]
        
headers2= data_set2[0]
planet_data2= data_set2[1:]

headers= headers1+headers2
planet_data= []

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open('final129.csv', 'a+')as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)



        
        


