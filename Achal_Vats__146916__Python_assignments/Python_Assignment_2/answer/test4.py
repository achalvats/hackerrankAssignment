# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:03:20 2018

@author: acvats
"""
import pandas as pd

fileName="xdata1.xlsx"
file=pd.ExcelFile(fileName)
df1=file.parse("Sheet1")
list1=[]
network=[]
database=[]
access=[]

#list1=str(df1.Incident_number + " " + df1.Application + " " + df1.Date + " " + df1.Error_description + " " + df1.Status)
list1=df1.Incident_number + "   " + df1.Application + "   " + df1.Error_description + "   " + df1.Status
#print("########")
#print(list1)
for error in list1:
    #print(error)
    if 'network' in error:
        network.append(error)
    elif 'databse' in error:
        database.append(error)
    elif 'Access' in error:
        access.append(error)

dat=open("data7.txt","r+")
dat.write("\n\n")
dat.write("Network Issue  :\n")
dat.write("----------------\n")
for n in network:
    dat.write(n)
    dat.write("\n")
dat.write("\n\n")
dat.write("Database Issue  :\n")
dat.write("-----------------\n")
for d in database:
    dat.write(d)
    dat.write("\n")
dat.write("\n\n")
dat.write("Access Issue  :\n")
dat.write("---------------\n")
for a in access:
    dat.write(a)
    dat.write("\n")
dat.close()
print("written")
#list1=[]
#list1=df1.Error_description
#print("########")
#print(list1)
#p=[]