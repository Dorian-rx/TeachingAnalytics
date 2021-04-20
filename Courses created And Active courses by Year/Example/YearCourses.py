import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

"""
# Create the list representing 10 years
years = []
for i in range(2011, 2021):
    years.append(i)

#Randomize the amount courses
new_courses = []
for year in years:
    new_courses.append(random.randint(100,1000))

#Randomize the amount of at least 1 hit courses
new_courses_1hit = []
count = 0
for year in years:
    seed += 1    
    if random.random() < 0.80:
        seed += 1    
        new_courses_1hit.append(round(random.uniform(0, new_courses[count])))

    elif 0.80 <= random.random() < 0.9:
        seed += 1    
        new_courses_1hit.append(round(random.uniform(0, new_courses[count]/10)))

    else:
        seed += 1    
        new_courses_1hit.append(round(random.uniform(0, new_courses[count]/20)))

    count += 1 

#Randomize the amount of at least 100 hits courses
new_courses_100hits = []
count = 0
for year in years:
    if random.random() < 0.80:
        new_courses_100hits.append(round(random.uniform(0, new_courses_1hit[count])))

    elif 0.80 <= random.random() < 0.9:
        new_courses_100hits.append(round(random.uniform(0, new_courses_1hit[count]/10)))

    else:
        new_courses_100hits.append(round(random.uniform(0, new_courses_1hit[count]/20)))

    count += 1 



#Display the result
print('Year:', years)
print('Number of courses per year:', new_courses)
print('Number of courses per year with at least one hit:', new_courses_1hit)
print('Number of courses per year with at least hundred hits:', new_courses_100hits)


#Make the percentage
#percentage_nc1h_nc= [round((int(nc1h) / int(nc))*100,  2) for nc, nc1h in zip(new_courses, new_courses_1hit)]
#percentage_nc100hs_nc1h= [round((int(nc100hs) / int(nc1h))*100,  2) for nc1h, nc100hs in zip(new_courses_1hit, new_courses_100hits)]
#percentage_nc100hs_nc= [round((int(nc100hs) / int(nc))*100,  2) for nc, nc100hs in zip(new_courses, new_courses_100hits)]


#Display the percentage result
#print('Percentage of courses one-timed hit by all courses per year:', percentage_nc1h_nc)
#print('Percentage of courses hundred-timed hit by courses one-timed hit per year:', percentage_nc100hs_nc1h)
#print('Percentage of courses hundred-timed hit by all courses per year:', percentage_nc100hs_nc)


#Create the artificial dataset
arf_data1 = pd.DataFrame({'Year': years, 'Courses': new_courses,'Kind': 'Courses'})
arf_data2 = pd.DataFrame({'Year': years, 'Courses': new_courses_1hit, 'Kind': 'Courses AL1h'})
arf_data3 = pd.DataFrame({'Year': years, 'Courses': new_courses_100hits, 'Kind': 'Courses AL100hs'})
arf_data = pd.concat([arf_data1, arf_data2, arf_data3])

print(arf_data)

#Display a visualisation
fig = px.bar(arf_data, x="Year", y="Courses", color="Kind", barmode='group')
fig.update_xaxes(
        type='category',
        title_text = "Years",
        title_standoff = 25)
fig.update_yaxes(
        title_text = "Count",
        title_standoff = 25)
fig.update_layout(title_text="Yearly New Courses, New Courses hit at least one time, New Courses hit at least hundred times", title_x=0.5)

fig.show()
"""

#Teaching Analytics
#1 Taux d'Hybridation per Professor / per Departments / (& per Year?)

#a) Taux d'Hybridation pour un enseignant (Factice Data)

"""
Quel est le temps de travail des enseignants ? 
https://www.oecd.org/fr/education/apprendre-au-dela-de-l-ecole/48640642.pdf
https://gasel.univ-lyon1.fr/Aide/Documents/Regles_Charges_Enseignement.pdf
http://www.le-sages.org/fiches/mconfPrag.html
"""

Min_per_Year = 320
Prag_Hour = 384
MC_Hour = 192


# Créer une liste qui représente le nombre de cours qu'un professeur enseigne par année.
count_PRAG = Prag_Hour
list_cour1 = []
list_cour2 = []
list_cour3 = []
list_cour4 = []


random.seed( 1000 )
count = 0
while count < 250:
    rand_num = random.random()
    if (0 <= rand_num < 0.7) :
        course_time = random.randint(15, 40)
    elif (0.7 <= rand_num < 1):
        course_time = random.randint(40, 90)
    elif (rand_num == 1):
        course_time = random.randint(90, 120)

    list_cour1.append(course_time)
    count += 1

random.seed( 1001 )
count = 0
while count < 250:
    rand_num = random.random()

    if (0 <= rand_num < 0.7) :
        course_time = random.randint(15, 40)
    elif (0.7 <= rand_num < 1):
        course_time = random.randint(40, 90)
    elif (rand_num == 1):
        course_time = random.randint(90, 120)

    list_cour2.append(course_time)
    count += 1

random.seed( 1002 )
count = 0
while count < 250:
    rand_num = random.random()

    if (0 <= rand_num < 0.7) :
        course_time = random.randint(15, 40)
    elif (0.7 <= rand_num < 1):
        course_time = random.randint(40, 90)
    elif (rand_num == 1):
        course_time = random.randint(90, 120)

    list_cour3.append(course_time)
    count += 1

random.seed( 1003 )
count = 0
while count < 250:
    rand_num = random.random()

    if (0 <= rand_num < 0.7) :
        course_time = random.randint(15, 40)
    elif (0.7 <= rand_num < 1):
        course_time = random.randint(40, 90)
    elif (rand_num == 1):
        course_time = random.randint(90, 120)

    list_cour4.append(course_time)
    count += 1


#print('Amount of hours teached per course', list_cour, '\n Amount of courses teached', len(list_cour), '\n Total hours teached', sum(list_cour))



# Créer les scénarios pour chaque comportement d'enseignants avec les MOOCs
# Les intervals: [1 - 0.8] / [0.8 - 0.5] / [0.5 - 0.2] / [0.2 - 0]

# Utilisations Elevé de MOOCs
random.seed( 1000 )
list1_MoocTime = [round(random.uniform(nc*0.8, nc)) for nc in list_cour1]

# Utilisation Moyennement-Elevé de MOOCs
random.seed( 1001 )
list2_MoocTime = [round(random.uniform(nc*0.5, nc*0.8)) for nc in list_cour2]

#Utilisation Moyennement-Faible de MOOCs
random.seed( 1002 )
list3_MoocTime = [round(random.uniform(nc*0.2, nc*0.5)) for nc in list_cour3]

#Utilisation Faible de MOOCs
random.seed( 1003 )
list4_MoocTime = [round(random.uniform(nc*0, nc*0.2)) for nc in list_cour4]


# Création du jeu de données factice

list_course_duration = list_cour1 + list_cour2 + list_cour3 + list_cour4
list_course_MOOC = list1_MoocTime + list2_MoocTime + list3_MoocTime + list4_MoocTime


Hybridation_db = pd.DataFrame({'Course Duration': list_course_duration,
                               'Course Duration MOOC': list_course_MOOC,
                               'Course Duration Lecture': [(dtn - mooc) for dtn, mooc in zip(list_course_duration, list_course_MOOC)]
})


# create a list of our conditions
conditions = [
    (Hybridation_db['Course Duration MOOC'] > 0.8 * Hybridation_db['Course Duration']),
    (Hybridation_db['Course Duration MOOC'] > 0.5 * Hybridation_db['Course Duration']) & (Hybridation_db['Course Duration MOOC'] <= 0.8 * Hybridation_db['Course Duration']),
    (Hybridation_db['Course Duration MOOC'] > 0.2 * Hybridation_db['Course Duration']) & (Hybridation_db['Course Duration MOOC'] <= 0.5 * Hybridation_db['Course Duration']),
    (Hybridation_db['Course Duration MOOC'] <= 0.2 * Hybridation_db['Course Duration'])
 ]

# create a list of the values we want to assign for each condition
values = ['High Hybridation', 'Medium-High Hybridation', 'Medium-Low Hybridation', 'Low Hybridation']

# create a new column and use np.select to assign values to it using our lists as arguments
Hybridation_db['Hybridation Level'] = np.select(conditions, values)

Hybridation_db = Hybridation_db.sample(frac=1).reset_index(drop = True).reset_index().rename(columns = {'index' : 'Course ID'}).set_index('Course ID')

Hybridation_db = Hybridation_db.sort_values(by = 'Course Duration MOOC', ascending = True)
print(Hybridation_db[Hybridation_db['Hybridation Level'] == '0'])

print(Hybridation_db.head(10))
print('Total Number of Courses:', len(Hybridation_db))

#Display a visualisation

#Plotly
"""
fig = px.scatter(Hybridation_db, x="Course Duration MOOC", y="Course Duration", color="Hybridation Level", hover_data = ['Course Duration', 'Course Duration MOOC', 'Course Duration Lecture'] )
fig.update_xaxes(
        type='category',
        title_text = "Duration MOOC",
        title_standoff = 25)
fig.update_yaxes(
        title_text = "Duraton Lecture",
        title_standoff = 25)
fig.update_layout(title_text="", title_x=0.5)

fig.show()
"""

"""
#French Rename
Hybridation_db.rename(columns={'Course Duration MOOC': 'Durée des cours en ligne',
                               'Course Duration Lecture': 'Durée des cours magistraux',
                               'Course Duration': 'Durée des cours',
                               "Hybridation Level": "Niveau d'Hybridation"})
"""

#Seaborn
fig = plt.figure(figsize=(16,10))
sns.scatterplot(data=Hybridation_db, x="Course Duration MOOC", y="Course Duration Lecture", hue="Hybridation Level", size = 'Course Duration', sizes=(20, 200))
plt.title("Nuage de Points sur le Niveau d'Hybridation pour chaque cours d'une année.") # Titre
plt.xlabel("Nombre d'heures de cours en ligne") #X-axis Titre
plt.ylabel("Nombre d'heures de cours magistraux") #Y-axis Titre

fig.savefig("Courses created And Active courses by Year/Example/Figures/NdPs sur le Niveau d'Hybridation.png")

plt.show()
Hybridation_db = Hybridation_db.sort_values(by = 'Course ID', ascending = True)
Hybridation_db.to_csv('Courses created And Active courses by Year/Example/Data/Hybridation_Year.csv')