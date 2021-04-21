###################################
    #Ressources par Enseignant#
###################################
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
random.seed( 2000 )

# Création d'une liste qui représente un interval de 10 ans entre 2013 et 2020.
list_years = []
for i in range(2013, 2021):
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


#print(list_years) # Afficher l'intervale d'année (2011 - 2021).
#print(list_year_mod) # Afficher le nombre total de modules/cours pour chaque année.
#print(len(list_mod_hrs)) # Afficher le nombre total de modules/cours pour toutes les années confondus.

# Création d'une liste qui représente la durée d'utilisation des ressources en ligne du cours (1 entrée = 1 cours).
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
Course_PerYear = pd.DataFrame({'Course_ID': [i for i in range(1, len(list_mod_hrs)+1)],
                                    'Course_Duration': list_mod_hrs,
                                    'Course_Duration_MOOC': [round(hrs * prct) for hrs, prct in zip(list_mod_hrs, list_hybrid_percent)],
                                    #'Number_Ressources': [round(random.uniform(round(hrs * prct)*0.35, round(hrs * prct)*0.8)) for hrs, prct in zip(list_mod_hrs, list_hybrid_percent)],
                                    'Year': temp_year,
                                    'Courses_perYear': temp_mod_hrs
                                    }).set_index('Course_ID')

Course_PerYear = Course_PerYear[Course_PerYear['Course_Duration_MOOC'] != 0]
#Course_PerYear = Course_PerYear[Course_PerYear['Number_Ressources'] != 0]

#print(Course_PerYear)

#print(np.mean(Course_PerYear['Number_Ressources']), np.mean(Course_PerYear['Course_Duration_MOOC']))
#print(np.mean(Course_PerYear['Number_Ressources']) / np.mean(Course_PerYear['Course_Duration_MOOC']))

list_rv = []
list_rq = []
list_re = []

for ress in Course_PerYear['Course_Duration_MOOC']:
    while ress > 0:
        random_vid = round(random.uniform(0, ress*0.75))
        random_quiz = round(random.uniform(0, ress*0.60))
        random_exam = round(random.uniform(0, 3))
        ress = ress - (random_vid + random_quiz + random_exam) 
        if ress != 0:
            ress = ress + random_vid + random_quiz + random_exam
        elif random_quiz <= random_exam:
            ress = ress + random_vid + random_quiz + random_exam
        elif random_vid < random_exam:
            ress = ress + random_vid + random_quiz + random_exam
        elif ress == 0:
            list_rv.append(random_vid)
            list_rq.append(random_quiz)
            list_re.append(random_exam)


list_nb_rv = []
list_nb_rq = []
list_nb_re = []

for vid, quiz, exam in zip(list_rv, list_rq, list_re):

    nb_vid = round(random.uniform(vid/4, vid))
    nb_quiz = round(random.uniform(quiz/2, quiz))
    nb_exam = round(random.uniform(exam/3, exam))

    list_nb_rv.append(nb_vid)
    list_nb_rq.append(nb_quiz)
    list_nb_re.append(nb_exam)



Course_PerYear['Duration_Video'] = list_rv
Course_PerYear['Duration_Quiz'] = list_rq
Course_PerYear['Duration_Exam'] = list_re

Course_PerYear['Number_Video'] = list_nb_rv
Course_PerYear['Number_Quiz'] = list_nb_rq
Course_PerYear['Number_Exam'] = list_nb_re

# Sauvegarder le dataframe en CSV
Course_PerYear = Course_PerYear.sort_values(by = 'Course_ID', ascending = True)
Course_PerYear.to_csv('Ressources/Example/Data/Ressources_perTeacher.csv')


#2018
Courses_2018 = Course_PerYear[Course_PerYear.Year == 2018]
print(Courses_2018.head(50))