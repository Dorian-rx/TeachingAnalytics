#############################################################
# Ratio of Digitalization per University and Year (Factice) #        
#############################################################

#Import the required packages
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt

#Set a seed to keep the same values randomly defined after each execution.
seed( 1996 )


################
# Factice Data #
################

#Create a list to represent the year interval (2013 to 2020).
list_years = [year for year in range(2013, 2021)]

#Create a list to represent the number of courses that a factice university teached for the year interval.
#Approximate to 1000 courses per year with 10% of maximal variation.
list_year_courses = [random.randint(1000*0.9, 1000*1.1) for year in list_years]

#Create a list to represent the number of hours per each course for the year interval.
list_course_hrs = []

#Implementation of the above list.
for num_courses in list_year_courses:  #Loop to select each element of the list that represent the number of courses per year.
    for i in range (0, num_courses):
        rand_num = random.random()  #Define a random number to choose the time interval of a course.
        if (0 <= rand_num < 0.3) : 
            num_hrs = random.randint(5, 15)   #Define a random number to have a course between 5H and 10H.
        elif (0.3 <= rand_num < 0.8) :
            num_hrs = random.randint(15, 60)  #Define a random number to have a course between 15H and 60H.
        elif (0.8 <= rand_num < 1):
            num_hrs = random.randint(60, 90)  #Define a random number to have a course between 60H and 90H.
        elif (rand_num == 1):
            num_hrs = random.randint(90, 120) #Define a random number to have a course between 90H and 120H.

        list_course_hrs.append(num_hrs)  #Append the number of hours of the course.

print(list_years) #Display the year interval (2013 - 2020).
print(list_year_courses) #Display the total number of courses per year.
print(len(list_course_hrs)) #Display the total number of courses.


#Create two lists that represent the ratio and percentage of digitalization of each course.
list_digit_ratio = []  #List that represents the digitalization ratio of each course.
list_digit_percent = [] #List that represents the digitalization percentage of each course.
for i in range(0, len(list_course_hrs)):
    list_digit_ratio.append(round(random.uniform(0, 1), 2)) 
    list_digit_percent.append(int(list_digit_ratio[i] * 100))

#Create two temporary lists to implementate the year of each course and the total number of course from each year.
temp_year = []
temp_course_hrs = []

dep = 0
for num_mods in list_year_courses:
    for i in range(0, num_mods):
        temp_year.append(list_years[dep])
        temp_course_hrs.append(list_year_courses[dep])
    dep += 1

#Make the dataframe
Digitalization_perYear = pd.DataFrame({'Course_ID': [i for i in range(1, len(list_course_hrs)+1)],
                                    'Duration': list_course_hrs,
                                    'Duration_Digit': [round(hrs * prct) for hrs, prct in zip(list_course_hrs, list_digit_ratio)],
                                    'Duration_Present': [round(hrs - (hrs*prct)) for hrs, prct in zip(list_course_hrs, list_digit_ratio)],
                                    'Year': temp_year,
                                    'Total_Courses_perYear': temp_course_hrs,
                                    'Digit_Ratio': list_digit_ratio,
                                    'Digit_Percentage': list_digit_percent
}).set_index('Course_ID')


#Create a list of conditions to define the level of digitalization.
conditions_digit = [
    (Digitalization_perYear['Digit_Percentage'] > 80),
    (Digitalization_perYear['Digit_Percentage'] > 50) & (Digitalization_perYear['Digit_Percentage'] <= 80),
    (Digitalization_perYear['Digit_Percentage'] > 20) & (Digitalization_perYear['Digit_Percentage'] <= 50),
    (Digitalization_perYear['Digit_Percentage'] <= 20),
]

#Create a list of values to assign to each condition from the above list
type_digit = ['High Digitalization', 'Medium-High Digitalization', 'Medium-Low Digitalization', 'Low Digitalization']

#Implement the level of digitalization on the dataframe
Digitalization_perYear['Digitalization'] = np.select(conditions_digit, type_digit)

#Find the statisticals measures (quartile, median) of the course duration.
#print(Digitalization_perYear['Duration'].describe())  #Result: Q1 = 17 / Median ~ 36 / Q3 = 49

#Create a list of conditions to define the interval of course duration.
conditions_duration = [
    (Digitalization_perYear['Duration'] <= 15),
    (Digitalization_perYear['Duration'] > 15) & (Digitalization_perYear['Duration'] < 40),
    (Digitalization_perYear['Duration'] >= 40) 
] 

#Create a list of values to assign to each condition from the above list
type_duration = ['Small Course ( <15H )', 'Medium Course ( >15H and <40H )', 'High Course ( >40H )']

Digitalization_perYear['Type'] = np.select(conditions_duration, type_duration)

print(Digitalization_perYear.head(10))

#Save the dataframe into a CSV file.
Digitalization_perYear = Digitalization_perYear.sort_values(by = 'Course_ID', ascending = True)
Digitalization_perYear.to_csv('Digitalization/Example/Data/Digitalization_perYear.csv')

##################
# Visualisations #
##################

Digitalization_perYear = Digitalization_perYear.sort_values(by = 'Duration', ascending = True) #Sort in an optimal way.

#Seaborn Figure
sns.set_style("whitegrid") #Setting Seaborn Style
sns.set_style("ticks", {"xtick.major.size": 12, "ytick.major.size": 12}) #Setting Seaborn labels ticks 

#Make the displot
col_pal = ['#0000ff', '#0ac848', '#ff0000']
dig_freq = sns.displot(data=Digitalization_perYear, x="Digit_Percentage", hue = 'Type', col = 'Type', kde=True, height=5, aspect=1, palette= col_pal)

#Set the figure title and labels
dig_freq.fig.suptitle('Frequency of the Digitalization Percentage per Interval of Course Duration')
dig_freq.fig.subplots_adjust(top=.8)
dig_freq.set_xlabels('Percentage of Digitalization')
dig_freq.set_ylabels('Frequency')

#Save Figure
dig_freq.savefig("Digitalization/Example/Figures/Displot of the Digitalization per Interval of Course Duration")

#Display the figure
plt.show()

