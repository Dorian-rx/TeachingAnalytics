#Teaching Analytics


############################################
    #Taux d'Hybridation par Département#
############################################

# Import Packages
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Définir les paramètres pandas
#pd.set_option("display.max_rows", 20)
#pd.set_option("display.max_columns", 10)


# Definir un seed pour garder les même valeurs aléatoirement définies.
random.seed( 1961 )

#Données Initiales
PRAG_Hour = 384 #Nombre d'heures minimale en cours magistraux à enseigner (pour un Professeur Aggrégé)  (Définit comme Base)
PRCE_Hour = 192 #Nombre d'heures minimale en cours magistraux à enseigner (pour un Maitre de Conférences)  (Définit comme Base)
Proportion_PRAG_on_PRCE = (8000)/(8000+6000) #Rapport PRAG/(PRAG+PRCE)
Proportion_PRCE_on_PRAG = (6000)/(8000+6000) #Rapport PRCE/(PRAG+PRCE)

#Définir un nombre de départements
nb_department = [] 

for dep in range(1,16):
    if dep < 10:
        nb_department.append('Dep_0' + str(dep))
    else:
        nb_department.append('Dep_' + str(dep))

#Création d'un ensemble de listes
hrs_department = [] #Le total des heures de travail de chaque département
hrs_ppl = [] #Le total des heures de travail de chaque enseignant
ppl_department = []  #Le nombre de personnes dans chaque département

for nb in nb_department:
    count = 0 
    ran_ppl = random.randint(5, 20)  #Select a random amount of number that represent the number of person in the current department
    for i in range(0, ran_ppl):
        rand_num = random.random()
        if (0 <= rand_num <= Proportion_PRAG_on_PRCE) :
            hrs_teach = random.uniform(384*0.8, 384*1.2)
        elif (Proportion_PRAG_on_PRCE < rand_num <= 1):
            hrs_teach = random.uniform(192*0.8, 192*1.2)
        hrs_ppl.append(round(hrs_teach))
        count = count + hrs_teach

    hrs_department.append(round(count)) 
    ppl_department.append(ran_ppl)

# Création d'une liste qui représente le pourcentage d'hybridation (1 entrée = 1 cours).
list_hybrid_percent = []
for i in range(0, len(hrs_ppl)):
    list_hybrid_percent.append(round(random.uniform(0, 1), 2))
    
# Création de trois listes temporaire pour implémenter dans la base de données artificiels
teacher_department = [] #Le département de chaque personne (length of len(list_mod_hrs))
teacher_number_department = [] #Le nombre de personnes dans chaque département (length of len(list_mod_hrs))
teaching_department = [] ##Le total des heures de travail de chaque département (length of len(list_mod_hrs))

dep = 0
for num_ppl in ppl_department:
    for i in range(0, num_ppl):
        teacher_department.append(nb_department[dep])
        teacher_number_department.append(ppl_department[dep])
        teaching_department.append(hrs_department[dep])

    dep += 1

# Definir le dataframe (EN) 
EN_Hybridation_dept_db = pd.DataFrame({'Teacher_ID': [i for i in range(1, len(hrs_ppl)+1)],
                                    'Teacher_Department': teacher_department,
                                    'Teaching_Time': hrs_ppl,
                                    'Teaching_Duration_MOOC': [round(hrs * prct) for hrs, prct in zip(hrs_ppl, list_hybrid_percent)],
                                    'Teaching_Duration_Lecture': [round(hrs - (hrs*prct)) for hrs, prct in zip(hrs_ppl, list_hybrid_percent)],
                                    'Teaching_perDepartment': teaching_department,
                                    'Teacher_perDepartment': teacher_number_department,
                                    'MOOC_Percentage': list_hybrid_percent,
                                    
}).set_index('Teacher_ID')

# Créer une liste de conditions pour définir le niveau d'hybridation
conditions = [
    (EN_Hybridation_dept_db['MOOC_Percentage'] > 0.8),
    (EN_Hybridation_dept_db['MOOC_Percentage'] > 0.5) & (EN_Hybridation_dept_db['MOOC_Percentage'] <= 0.8),
    (EN_Hybridation_dept_db['MOOC_Percentage'] > 0.2) & (EN_Hybridation_dept_db['MOOC_Percentage'] <= 0.5),
    (EN_Hybridation_dept_db['MOOC_Percentage'] <= 0.2)
 ]

# Créer une liste de valeurs que l'on veut assigner à chaque condition
values = ['High Hybridation', 'Medium-High Hybridation', 'Medium-Low Hybridation', 'Low Hybridation']

# Implémenter sur le dataframe une colonne qui représente les niveaux d'hybridations
EN_Hybridation_dept_db['Hybridation_Level'] = np.select(conditions, values)

# Sauvegarder le dataframe en CSV
EN_Hybridation_dept_db = EN_Hybridation_dept_db.sort_values(by = 'Teacher_ID', ascending = True)
EN_Hybridation_dept_db.to_csv('Hybridation/Example/Data/Hybridation_perDepartment.csv')

# Arranger le dataframe en fonction de la durée du cours
EN_Hybridation_dept_db = EN_Hybridation_dept_db.sort_values(by = 'Teaching_Time', ascending = True)
print(EN_Hybridation_dept_db.head(10))

#Visualisations

# Selection du dataframe

#GROUP_BY Departement
Hybrid_perDepartment = EN_Hybridation_dept_db.groupby('Teacher_Department').sum()[['Teaching_Time', 'Teaching_Duration_MOOC', 'Teaching_Duration_Lecture']].reset_index()
print(Hybrid_perDepartment)


#Matplotlib Figure
width = 0.25 #Definir la largeur de chaque bar
fig, ax = plt.subplots(figsize=(20, 8), sharey=True) 
rec1 = ax.bar(np.arange(len(Hybrid_perDepartment['Teacher_Department']))-(width+width/10), Hybrid_perDepartment['Teaching_Time'], width, label='Course Duration')
rec2 = ax.bar(np.arange(len(Hybrid_perDepartment['Teacher_Department'])), Hybrid_perDepartment['Teaching_Duration_MOOC'], width, label='MOOC Duration')
rec3 = ax.bar(np.arange(len(Hybrid_perDepartment['Teacher_Department']))+(width+width/10), Hybrid_perDepartment['Teaching_Duration_Lecture'], width, label='Lecture Duration')

#Ajouter des labels
ax.set_xlabel("Numéro du Département")
ax.set_ylabel("Heures d'enseignement")
ax.set_title("Total heures d'enseignement à travers des cours magistraux et des MOOCs par département")
ax.set_xticks(np.arange(len(Hybrid_perDepartment['Teacher_Department'])))
ax.set_xticklabels(Hybrid_perDepartment['Teacher_Department'])
ax.legend()

for rect, label in zip(rec1, Hybrid_perDepartment['Teaching_Time']):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')

for rect, label in zip(rec2, Hybrid_perDepartment['Teaching_Duration_MOOC']):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')

for rect, label in zip(rec3, Hybrid_perDepartment['Teaching_Duration_Lecture']):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')

fig.tight_layout()

#Save Figure
fig.savefig("Hybridation/Example/Figures/Barplots sur le niveau d'hybridation par département")

#Display the Figure
#plt.show()