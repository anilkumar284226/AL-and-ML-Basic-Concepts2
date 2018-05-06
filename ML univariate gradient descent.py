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



def compute_error_for_line_given_points(c,m,points):
    total_error=0
    for i in range(0,len(points)):
        x = points[i,2]
        y = points[i,1]
        total_error +=(y - m*x -c)**2
    return total_error/len(points)


def step_gradient(c_current,m_current,points,learning_rate):
    c_gradient = 0.0
    m_gradient = 0.0
    n=len(points)
    for i in range(0,n-1):
        x = points[i,2]
        y = points[i,1]
        c_gradient += -(2/n)*(y- ((m_current*x) + c_current))
        m_gradient += -(2/n)*(x)*(y- ((m_current*x) + c_current))
    new_c = c_current -(learning_rate * c_gradient)
    new_m = m_current -(learning_rate * m_gradient)
    return(new_c,new_m)

def gradient_descent_runner(points,c_start,m_start,learning_rate,num_iterations):
    c = c_start
    m = m_start
    for i in range(0,num_iterations-1):
        c,m=step_gradient(c,m,points,learning_rate)
    return (c,m)

points = my_pandas_model.reset_index().values
learning_rate = 0.0001
initial_c = 0
initial_m = 0
num_iterations = 1000


print(compute_error_for_line_given_points(initial_c,initial_m,points))

#run Gradient

final_c,final_m = gradient_descent_runner(points,initial_c,initial_m,learning_rate,num_iterations)

#print('final_c = ' +final_c +'final_m ='+ final_m)

print(compute_error_for_line_given_points(final_c,final_m,points))

for i in range(0,len(points)):
    x = points[i,2]
    y = points[i,1]
    plot.scatter(x,y,color ='red')
    plot.plot(my_pandas_model.acceleration,(final_m * my_pandas_model.acceleration + final_c))    