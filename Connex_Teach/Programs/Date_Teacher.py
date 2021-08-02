###
#  #        
####

#Import the required packages
import random
from math import *
import datetime
from datetime import datetime
import numpy as np
from numpy.core.numeric import NaN
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import time


##################
# Initialization #
##################

#Set the start_time
start_time = time.time()

################
#Find the Path #
################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Teacher_Improve', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder

#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 1000 ) #The seed does not need to be randomize

#################################
# Import the required Data file #
#################################

Ressources = pd.read_csv('Analytics\Teaching-Analytics\Teacher_Improve\Factice-Example\Data\Ressources.csv')

######################
# Class and Function #
######################

###########################################################
# Build the Day per Day DataFrame with the Ressouces Data #
###########################################################

#####################################
# Build the Ressources Grouped Data #
#####################################

#Create a dict with the columns to modify and their computation.
d = {'Course_ID': pd.Series.nunique,
     'Course_Duration': 'sum',
     'Course_Ressources': 'sum',
     'Course_Ress_Digit': 'sum',
     'Course_Ress_inClass': 'sum',
     'Digitalization_Ressource_Percent': 'mean',
     'Number_Video': 'sum',
     'Number_QCM': 'sum',
     'Number_Test': 'sum',
     'Number_Lecture': 'sum',
     'Number_Exercise': 'sum',
     'Number_Exam': 'sum',
}

#Group the «Ressources» DataFrame per Teacher ID and Year and aggregate the above elements in the dict.
Ressources_GRP = Ressources.groupby(['Department', 'Teacher_ID', 'Teacher_Name', 'Year']).agg(d).reset_index()
Ressources_GRP = Ressources_GRP.rename(columns = {"Course_ID":"Count_Course"})

print(Ressources_GRP)

##############################
# Build the Day per Day Data #
##############################

#Set Begin and End Date of the Day per Day Data.
begin_Date = int(time.mktime(time.strptime('2013-09-01 00:00:00', '%Y-%m-%d %H:%M:%S')))  # Date == 01/09/2013.
end_Date = int(time.mktime(time.strptime('2020-09-01 00:00:00', '%Y-%m-%d %H:%M:%S')))  # Date == 01/09/2020.
sec_Day = 86400 #Define the number of seconds in a day. (used to implement everyday on the data).

#Set the months and weekdays list
Months = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre") #List of Months.
Weekdays = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche") #List of Weekdays.


#Create empty Lists to implement in the Day per Day loop.
list_Date = []      #List that represents the full date (ex: 2013-09-01)
list_Year = []      #List that represents the year of the date.
list_Month = []     #List that represetns the month of the date.
list_Day = []       #List that represents the day of the date.
list_Weekday = []   #List that represents the weekday (ex: Monday) of the date.
list_IsWeekend = [] #List that represents the weekend (ex: Yes if Samedi/Dimanche else No).
list_Trimester = [] #List that display the trimester of the date
list_DayPeriod = [] #List that display the period of the day

while end_Date >= begin_Date:
    d_Date = datetime.strptime(datetime.fromtimestamp(begin_Date).isoformat(),"%Y-%m-%dT%H:%M:%S").date() #Transform the Timestamp date into Human Date

    if d_Date.day >= 1 and d_Date.month == 9 or d_Date.month in [10,11] and d_Date.day < 15 and d_Date.month == 12:
        trim = 'Trimestre 1'
    elif d_Date.day >= 15 and d_Date.month == 12 or d_Date.month in [1,2] or d_Date.day < 15 and d_Date.month == 3:
        trim = 'Trimestre 2'
    elif d_Date.day >= 15 and d_Date.month == 3 or d_Date.month in [4,5] or d_Date.day < 15 and d_Date.month == 6:
        trim = 'Trimestre 3'
    elif d_Date.day >= 15 and d_Date.month == 6 or d_Date.month in [7,8]:
        trim = 'Trimestre 4'
    
    for dperiod in ['Journée', 'Soirée', 'Nuit']:
        list_Date.append(d_Date)
        list_Year.append(d_Date.year)
        list_Month.append(Months[d_Date.month - 1])
        list_Day.append(d_Date.day)
        list_Weekday.append(Weekdays[d_Date.weekday()])
        list_IsWeekend.append('Oui' if d_Date.weekday() in [5,6] else 'Non')
        list_Trimester.append(trim)
        list_DayPeriod.append(dperiod)

    begin_Date += sec_Day

#Define the DataFrame columns.
Date = pd.DataFrame({'Date': list_Date,
                     'Year': list_Year,
                     'Month': list_Month,
                     'Day': list_Day,
                     'DayPeriod': list_DayPeriod,
                     'WeekDay': list_Weekday,
                     'Is_Weekend': list_IsWeekend,
                     'Trimester': list_Trimester
})

print(Date)

Date_Teacher = pd.merge(Date, Ressources_GRP, on = 'Year')

print(Date_Teacher)

########
#Connexion 





#############
# Save Data #
#############

#Save the Login into a CSV File.
Date_Teacher.to_csv('Analytics\Teaching-Analytics\Teacher_Improve\Factice-Example\Data\Date_Teacher.csv')


########################
# Data Ressources DONE #
########################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))
