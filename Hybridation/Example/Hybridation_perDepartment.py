#Hybridation per Department

#Useful Links
"""
http://www.le-sages.org/fiches/mconfPrag.html --> PRAG ET MAÎTRES DE CONFERENCE
"""
#Import Packages
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Set Pandas Settings/Options
pd.set_option("display.max_rows", 20)
#pd.set_option("display.max_columns", 10)


#Define a seed to keep the same values
random.seed( 2021 )

PRAG_Hour = 384 #Nombre d'heures minimale en cours magistraux à enseigner (pour un Professeur Aggrégé)  (Définit comme Base)
PRCE_Hour = 192 #Nombre d'heures minimale en cours magistraux à enseigner (pour un Maitre de Conférences)  (Définit comme Base)
Proportion_PRAG_on_PRCE = (8000)/(8000+6000)
Proportion_PRCE_on_PRAG = (6000)/(8000+6000)


nb_department = [dep for dep in range(1,21)]

hrs_department = [] #The total time worked per departement
hrs_ppl = [] #The time teached per person of each departement
ppl_department = []  #The number of person per departement

for nb in nb_department:
    count = 0 
    ran_ppl = random.randint(5, 35)  #Select a random amount of number that represent the number of person in the current department
    for i in range(0, ran_ppl):
        rand_num = random.random()
        if (0 <= rand_num <= Proportion_PRAG_on_PRCE) :
            hrs_teach = random.uniform(384*0.8, 384*1.2)
        elif (Proportion_PRAG_on_PRCE < rand_num <= 1):
            hrs_teach = random.uniform(192*0.8, 192*1.2)
        hrs_ppl.append(hrs_teach)
        count = count + hrs_teach

    hrs_department.append(count) 
    ppl_department.append(ran_ppl)

teacher_department = []
teacher_number_department = []
teaching_department = []

dep = 0
for X in ppl_department:
    for i in range(0, X):
        teacher_department.append(nb_department[dep])
        teacher_number_department.append(ppl_department[dep])
        teaching_department.append(hrs_department[dep])

    dep += 1



ran = []
for i in range(0, len(hrs_ppl)):
    ran.append(round(random.uniform(0, 1), 2))

Hybridation_dept_db = pd.DataFrame({'Teacher_ID': [i for i in range(1, len(hrs_ppl)+1)],
                                    'Teacher_Department': teacher_department,
                                    'Teaching_Time': hrs_ppl,
                                    'Teaching Duration MOOC': [round(hrs * i) for hrs, i in zip(hrs_ppl, ran)],
                                    'Teaching Duration Lecture': [round(hrs - (hrs*i)) for hrs, i in zip(hrs_ppl, ran)],
                                    'Teaching_perDepartment': teaching_department,
                                    'Teacher_perDepartment': teacher_number_department,
                                    'MOOC Percentage': ran,
                                    
}).set_index('Teacher_ID')

# create a list of our conditions
conditions = [
    (Hybridation_dept_db['MOOC Percentage'] > 0.8),
    (Hybridation_dept_db['MOOC Percentage'] > 0.5) & (Hybridation_dept_db['MOOC Percentage'] <= 0.8),
    (Hybridation_dept_db['MOOC Percentage'] > 0.2) & (Hybridation_dept_db['MOOC Percentage'] <= 0.5),
    (Hybridation_dept_db['MOOC Percentage'] <= 0.2)
 ]

# create a list of the values we want to assign for each condition
values = ['High Hybridation', 'Medium-High Hybridation', 'Medium-Low Hybridation', 'Low Hybridation']

# create a new column and use np.select to assign values to it using our lists as arguments
Hybridation_dept_db['Hybridation Level'] = np.select(conditions, values)


#Display ten randoms teachers
#print(Hybridation_dept_db.sample(n=10,replace=True))
#Hybridation_dept_db.to_csv('Test.csv')

#GROUP_BY Departement
X = Hybridation_dept_db.groupby('Teacher_Department').sum()[['Teaching_Time', 'Teaching Duration MOOC', 'Teaching Duration Lecture']].reset_index()

WW = pd.melt(X, id_vars=["Teacher_Department"], var_name="Teaching", value_vars=["Teaching_Time", "Teaching Duration MOOC", 'Teaching Duration Lecture'], value_name="hours")
WW['hours'] = round(WW['hours'])
#WW.merge(Z, by = 'Teacher_Department')
WW = WW.sort_values('Teacher_Department')


#Viz
#Seaborn
sns.catplot(data=WW, x="Teacher_Department", y="hours", hue="Teaching",  kind="bar")
plt.title("Nuage de Points sur le Niveau d'Hybridation pour chaque cours d'une année.") # Titre
plt.xlabel("Nombre d'heures de cours en ligne") #X-axis Titre
plt.ylabel("Nombre d'heures de cours magistraux") #Y-axis Titre
plt.show()
plt.savefig("Courses created And Active courses by Year/Example/Figures/NdPs sur le Niveau d'Hybridation par Département.png")


print(Hybridation_dept_db)

#sns.scatterplot(data=Hybridation_dept_db, x="Teaching Duration MOOC", y="Teaching Duration Lecture", hue="Hybridation Level", style="Teacher_Department", sizes=200)
