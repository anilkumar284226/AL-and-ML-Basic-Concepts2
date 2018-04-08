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

X= np.array(my_pandas_model.drop(['mpg'],1))
y = np.array(my_pandas_model['mpg'],dtype=int)


X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.20)

regression = linear_model.LinearRegression()

regression.fit(X_train,y_train)

print(regression.score(X_test,y_test))

prediction = regression.predict(X_test)

plot.scatter(X_test,y_test,color='black')
plot.plot(X_test,prediction,color='blue')


