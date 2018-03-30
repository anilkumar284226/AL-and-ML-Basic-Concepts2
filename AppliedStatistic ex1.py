#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Renu
#
# Created:     29/03/2018
# Copyright:   (c) Renu 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anil
#
# Created:     17/03/2018
# Copyright:   (c) Anil 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
from collections import Counter
import statistics


def read_File():
    df = pd.read_csv("C:\\Users\\Renu\\Desktop\\TopGear AI & ML basics\\Stats.csv", delimiter=',', error_bad_lines=False,  encoding='utf-8')
    return df

if __name__ == '__main__':
    myCsv = read_File()
    myList = myCsv.values.tolist()
    print(type(myList))
    myExperienceList=[]
    mySalaryList=[]
    
    
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if(j==2):
                myExperienceList.append(myList[i][j])
            if(j==1):
                mySalaryList.append(myList[i][j])
    print(myExperienceList)
    print(mySalaryList)
    
    #Mean of Experience
    ExperienceMean = (sum(myExperienceList))/len(myExperienceList)
        
    
    #Mode of Experience 
    
    data = Counter(myExperienceList)
    data.most_common()   # Returns all unique items and their counts
    ExperienceModeList = data.most_common(1)  # Returns the highest occurring item
    ExperienceMode = ExperienceModeList[0][1]
    
    #Median of Experience
    ExperienceMedian = (sum(myExperienceList))/len(myExperienceList)
    
    #standard deviation of experience
    ExperiencStandardDeviation = statistics.stdev(myExperienceList)

    #variance of experience
    Experiencvariance = statistics.variance(myExperienceList)
    
    
    
    #Mean of Salary
    SalaryMean = (sum(mySalaryList))/len(mySalaryList)
        
    
    #Mode of Salary 
    
    data = Counter(mySalaryList)
    data.most_common()   # Returns all unique items and their counts
    SalaryModelist = data.most_common(1) # Returns the highest occurring item
    SalaryMode = SalaryModelist[0][1]
    
    #Median of Salary
    SalaryMedian = (sum(mySalaryList))/len(mySalaryList)
    
    #standard deviation of Salary
    SalaryStandardDeviation = statistics.stdev(mySalaryList)

    #variance of Salary
    Salaryvariance = statistics.variance(mySalaryList)
    
    print("Experence Statistics")
    print("Experience mean = %.2f " % ExperienceMean)
    print("Experience Mode =  %.0f"  % ExperienceMode)
    print("Experience Median = %.2f " % ExperienceMedian)
    print("Experience SD =  %.2f" % ExperiencStandardDeviation)
    print("Experience variance =  %.2f" % Experiencvariance)
    
    
    print("Salary Statistics")
    print("Salary mean =  %.2f" % SalaryMean)
    print("Salary Mode =  %.0f" % SalaryMode)
    print("Salary Median =  %.2f" % SalaryMedian)
    print("Salary SD =  %.2f" % SalaryStandardDeviation)
    print("Salary variance =  %.2f" % Salaryvariance)