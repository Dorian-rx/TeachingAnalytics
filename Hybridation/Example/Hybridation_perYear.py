#Teaching Analytics
#1) Taux d'Hybridation par Année

# Import Packages
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt

# Definir un seed pour garder les même valeurs aléatoirement définies.
random.seed( 1996 )

# Création d'une liste qui représente un interval de 10 ans entre 2011 et 2020.
list_years = []
for i in range(2011, 2021):
    list_years.append(i)

# Création d'une liste qui représente le nombre de cours (+ nombres d'heures par cours) qu'une université enseigne chaque année (entre 1500 & 3000).
list_year_mod = []
list_mod_hrs = []

for y in list_years:
    year_num_mod = random.randint(1500, 3000)
    for i in range (0, year_num_mod):
        rand_num = random.random()
        if (0 <= rand_num < 0.2) :
            mod_hrs = random.randint(10, 15)
        elif (0.2 <= rand_num < 0.7) :
            mod_hrs = random.randint(15, 40)
        elif (0.7 <= rand_num < 1):
            mod_hrs = random.randint(40, 90)
        elif (rand_num == 1):
            mod_hrs = random.randint(90, 120)

        list_mod_hrs.append(mod_hrs)
    list_year_mod.append(year_num_mod)

print(list_years) # Afficher l'intervale d'année (2011 - 2021).
print(list_year_mod) # Afficher le nombre total de modules/cours pour chaque année.
print(len(list_mod_hrs)) # Afficher le nombre total de modules/cours pour toutes les années confondus.

# Création du niveau d'hybridation de chaque module/cours.

# Création d'une liste qui représente le pourcentage d'hybridation (1 entrée = 1 cours).
list_hybrid_percent = []
for i in range(0, len(list_mod_hrs)):
    list_hybrid_percent.append(round(random.uniform(0, 1), 2))

# Création de deux listes temporaire pour implémenter l'année de chaque cours et le nombre total de cours à l'année
temp_year = []
temp_mod_hrs = []

dep = 0
for num_mods in list_year_mod:
    for i in range(0, num_mods):
        temp_year.append(list_years[dep])
        temp_mod_hrs.append(list_year_mod[dep])
    dep += 1

# Definir le dataframe (EN) 
EN_Hybridation_perYear = pd.DataFrame({'Course_ID': [i for i in range(1, len(list_mod_hrs)+1)],
                                    'Course_Duration': list_mod_hrs,
                                    'Course_Duration_MOOC': [round(hrs * prct) for hrs, prct in zip(list_mod_hrs, list_hybrid_percent)],
                                    'Course_Duration_Lecture': [round(hrs - (hrs*prct)) for hrs, prct in zip(list_mod_hrs, list_hybrid_percent)],
                                    'Year': temp_year,
                                    'Courses_perYear': temp_mod_hrs
                                    }).set_index('Course_ID')

# Créer une liste de conditions pour définir le niveau d'hybridation
conditions_EN = [
    (EN_Hybridation_perYear['Course_Duration_MOOC'] > 0.8 * EN_Hybridation_perYear['Course_Duration']),
    (EN_Hybridation_perYear['Course_Duration_MOOC'] > 0.5 * EN_Hybridation_perYear['Course_Duration']) & (EN_Hybridation_perYear['Course_Duration_MOOC'] <= 0.8 * EN_Hybridation_perYear['Course_Duration']),
    (EN_Hybridation_perYear['Course_Duration_MOOC'] > 0.2 * EN_Hybridation_perYear['Course_Duration']) & (EN_Hybridation_perYear['Course_Duration_MOOC'] <= 0.5 * EN_Hybridation_perYear['Course_Duration']),
    (EN_Hybridation_perYear['Course_Duration_MOOC'] <= 0.2 * EN_Hybridation_perYear['Course_Duration'])
 ]

# Créer une liste de valeurs que l'on veut assigner à chaque condition
values_EN = ['High Hybridation', 'Medium-High Hybridation', 'Medium-Low Hybridation', 'Low Hybridation'] #English

# Implémenter sur le dataframe une colonne qui représente les niveaux d'hybridations
EN_Hybridation_perYear['Hybridation_Level'] = np.select(conditions_EN, values_EN)

# Sauvegarder le dataframe en CSV
EN_Hybridation_perYear = EN_Hybridation_perYear.sort_values(by = 'Course_ID', ascending = True)
EN_Hybridation_perYear.to_csv('Hybridation/Example/Data/Hybridation_perYear.csv')

# Arranger le dataframe en fonction de la durée du cours
EN_Hybridation_perYear = EN_Hybridation_perYear.sort_values(by = 'Course_Duration', ascending = True)

print(EN_Hybridation_perYear.head(10))
print('Total Number of Courses:', len(EN_Hybridation_perYear))


#Visualisations

# Selection du dataframe
EN_Hybridation_2019 = EN_Hybridation_perYear[EN_Hybridation_perYear['Year'] == 2019]

# Seaborn Figure
fig = plt.figure(figsize=(16,10))
sns.scatterplot(data=EN_Hybridation_2019, x="Course_Duration_MOOC", y="Course_Duration_Lecture", hue="Hybridation_Level", size = 'Course_Duration', sizes=(20, 200))
plt.title("Nuage de Points concernant le niveau d'Hybridation pour l'année 2019.") # Titre
plt.xlabel("Nombre d'heures de cours en ligne") #X-axis Titre
plt.ylabel("Nombre d'heures de cours magistraux") #Y-axis Titre

#Save Figure
fig.savefig("Hybridation/Example/Figures/Ndps sur le niveau d'hybridation pour 2019")

#Display the Figure
plt.show()
