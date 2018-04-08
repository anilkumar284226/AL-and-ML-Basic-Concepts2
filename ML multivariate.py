"""
Created on Sun Apr  8 02:28:40 2018

@author: Anil
"""
import pandas as pd
from sklearn import neighbors,preprocessing,cross_validation,linear_model
import numpy as np
import matplotlib.pyplot as plot

df = pd.read_csv("C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\ml_data.csv");

#The below command did not work so did a work around
#model = df.DataFrame(df,columns=['mpg','acceleration'])
myList = df.values.tolist()
myModelList =[]

for i in range(len(myList)):
    Local=[]
    for j in range(len(myList[i])):
        if(j==0 or j==6):
            Local.append(myList[i][j])
    myModelList.append(Local)
              
my_pandas_model = pd.DataFrame(myModelList)

my_pandas_model = my_pandas_model.rename(columns={0:'mpg',1:'acceleration'})







