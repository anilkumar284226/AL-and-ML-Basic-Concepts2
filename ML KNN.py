"""
Created on Sun Apr  8 02:28:40 2018

@author: Anil
"""
import pandas as pd
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\haberman_data.csv");

myList = df.values.tolist()
XList =[]
YList =[]

myList = df.values.tolist()
myModelList =[]

for i in range(len(myList)):
    Local=[]
    for j in range(len(myList[i])):
        if(j==0 or j==2):
            Local.append(myList[i][j])
        if(j==3):
            YList.append(myList[i][j])
    XList.append(Local)   
            

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(XList, YList, test_size=0.2)

classifier = KNeighborsClassifier(n_neighbors=5)  
classifier.fit(X_train, Y_train)


accuracy=classifier.score(X_test,Y_test)
print(accuracy)
prediction = classifier.predict(X_test)
print(prediction)