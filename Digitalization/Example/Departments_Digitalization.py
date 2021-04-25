#####################################################
# Ratio of Digitalization per University Department #        
#####################################################

#Import the required packages
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt

#Set a seed to keep the same values randomly defined after each execution.
seed( 1961 )


################
# Factice Data #
################

#Initial Information.
PRAG_Hour = 384 #Average Minimal (Hours of teaching) - PRAG.
PRCE_Hour = 192 #Average Minimal (Hours of teaching) - PRCE.
Prop_PRAG_on_PRCE = (8000)/(8000+6000) #PRAG/(PRAG+PRCE)
Prop_PRCE_on_PRAG = (6000)/(8000+6000) #PRCE/(PRAG+PRCE)

#Define a list of departements.
type_departement = ['AGM', 'AGORA', 'BioCIS', 'BONHEURS', 'CESDIP', 'CPJP', 'EMA', 'ERRMECe', 'ETIS', 'GEC', 'HERITAGES', 'I-MAT', 'IDHN', 'L2MGC', 'LAMBE', 'LDAR', 'LERMA', 'LEJEP', 'LPMS', 'LPPI', 'LPTM', 'LT2D', 'MRTE', 'PARAGRAPHE', 'SATIE', 'THEMA']
descpt_departement = []

#Take a random integer representing the number of departments.
num_dep = random.randint(12, 17)

#Append the type of each department.
department = []
num = 0
while num < num_dep:
    ran_num = random.randint(0, len(type_departement))
    if type_departement[ran_num] not in department:
        department.append(type_departement[ran_num])
        num += 1 

#Display the number of departments and the type of each of them.
print('Number of Departments:', num_dep, '\nType:', department)   

#Create a list to represent the year interval (2013 to 2020).
list_years = [year for year in range(2013, 2021)]

#Create three lists 
hrs_department = [] #Total number of hours of teaching of each department.
hrs_ppl = [] #Total hours of work of each teacher.
ppl_department = []  #Total number of teachers per department.
teacher_ID = [] #The identification of each teacher

for dep in department:
    count = 0 
    ran_ppl = random.randint(5, 20)  #Random number that represents the number of teachers in the current department.
    for i in range(0, ran_ppl):
        rand_num = random.random()   #Define a random number to choose the teachers working time.
        if (0 <= rand_num <= Prop_PRAG_on_PRCE) :
            hrs_teach = random.uniform(384*0.8, 384*1.2)  #Set the current teacher as a PRAG (with 20% range from the basic working hours).
        elif (Prop_PRAG_on_PRCE < rand_num <= 1):
            hrs_teach = random.uniform(192*0.8, 192*1.2)  #Set the current teacher as a PRCE (with 20% range from the basic working hours).
        hrs_ppl.append(round(hrs_teach))  #Append the number of working hours of the current teacher.
        count += hrs_teach 

    hrs_department.append(round(count)) #Append the number of teaching hours of the current department. 
    ppl_department.append(ran_ppl) #Append the number of teacher of the current department.

#Duplicate the initial values of teaching hours for each year
hrs_ppl_y = []
for year in list_years:
    hrs_ppl_y = hrs_ppl_y + hrs_ppl


#Create two lists that represent the ratio and percentage of digitalization of each teacher.
list_digit_ratio = []  #List that represents the digitalization ratio of each teacher.
list_digit_percent = [] #List that represents the digitalization percentage of each teacher.
for i in range(0, len(hrs_ppl_y)):
    list_digit_ratio.append(round(random.uniform(0, 1), 2)) 
    list_digit_percent.append(int(list_digit_ratio[i] * 100))



#Create three temporary lists
teacher_department = [] #The department of each teacher
teacher_number_department = [] #The number of teachers per department 
teaching_department = [] #The total number of hours teached by department
temp_year = [] #The year of the teacher
list_teacher_ID = [] #List that represents the identification of each teacher

dep = 0
for year in list_years:
    teach_ID = 1
    dep = 0
    for num_ppl in ppl_department:
        for i in range(0, num_ppl):
            teacher_number_department.append(num_ppl)
            teacher_department.append(department[dep])
            teaching_department.append(hrs_department[dep])
            temp_year.append(year)
            list_teacher_ID.append(teach_ID)

            teach_ID += 1
        dep += 1


#Make the dataframe
Digitalization_Dept = pd.DataFrame({'Teacher_ID': list_teacher_ID,
                                    'Department': teacher_department,
                                    'Year': temp_year,
                                    'Teacing_Duration': hrs_ppl_y,
                                    'Teaching_Digit': [round(hrs * prct) for hrs, prct in zip(hrs_ppl_y, list_digit_ratio)],
                                    'Teaching_Present': [round(hrs - (hrs*prct)) for hrs, prct in zip(hrs_ppl_y, list_digit_ratio)],
                                    'Hours_Teached_Department': teaching_department,
                                    'Teacher_Department': teacher_number_department,
                                    'Digit_Ratio': list_digit_ratio,
                                    'Digit_Percentage': list_digit_percent,
                                                  
})

#Create a list of conditions to define the level of digitalization.
conditions_digit = [
    (Digitalization_Dept['Digit_Percentage'] > 80),
    (Digitalization_Dept['Digit_Percentage'] > 50) & (Digitalization_Dept['Digit_Percentage'] <= 80),
    (Digitalization_Dept['Digit_Percentage'] > 20) & (Digitalization_Dept['Digit_Percentage'] <= 50),
    (Digitalization_Dept['Digit_Percentage'] <= 20),
]

#Create a list of values to assign to each condition from the above list
type_digit = ['High Digitalization', 'Medium-High Digitalization', 'Medium-Low Digitalization', 'Low Digitalization']

#Implement the level of digitalization on the dataframe
Digitalization_Dept['Digitalization'] = np.select(conditions_digit, type_digit)

print(Digitalization_Dept.head(10))

# Sauvegarder le dataframe en CSV
Digitalization_Dept = Digitalization_Dept.sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Dept.to_csv('Digitalization/Example/Data/Digitalization_perDepartment.csv')


##################
# Visualisations #
##################

#Filter the useful data
Digitalization_Dept_2016_2020 = Digitalization_Dept[Digitalization_Dept['Year'].isin([2017, 2018, 2019])]

#Seaborn Figure
sns.set_style("whitegrid") #Setting Seaborn Style
sns.set_style("ticks", {"xtick.major.size": 12, "ytick.major.size": 12}) #Setting Seaborn labels ticks 

#Make the barplot
dep_dig = sns.catplot(data=Digitalization_Dept_2016_2020, x="Department", y="Digit_Percentage", capsize=.2, ci=20, col = 'Year', height = 5, kind="bar", palette = 'icefire')

#Set the figure title and labels
dep_dig.fig.suptitle('Percentage of Digitalization of each University Department from 2017 to 2019')
dep_dig.fig.subplots_adjust(top=.8)
dep_dig.set_xlabels('University Departments')
dep_dig.set_xticklabels(rotation = 90)
dep_dig.set_ylabels('Percentage of Digitalization')

#Save Figure
dep_dig.savefig("Digitalization/Example/Figures/Barplots of the Digitalization per Department from 2017 to 2019")

#Display the figure
plt.tight_layout()
plt.show()