#######################################
# Digitalisation, Genre et Ancienneté #
#######################################

#Import the required packages
from math import *
import numpy as np
import pandas as pd
import random
import os 
import time


#Set the initial time of the program
start_time = time.time()


#Define the path
keywords = ['Data', 'Data-Names', 'Figures', 'Programs'] #Define the name of each subfolder of the global directory path.
path_dir = os.path.dirname(__file__) #Find the directory path.
path_glob = os.path.dirname(path_dir) #Find the global directory path.

path_data = path_glob + '/' + keywords[0] + '/' 
path_data_names = path_data + keywords[1] + '/' 
path_figures = path_glob + '/' + keywords[2] + '/' 
path_programs = path_glob + '/' + keywords[3] + '/' 


#Initialize a pseudorandom number generator (seed) to preserve the same values randomly obtained after any execution
random.seed( 2021 ) #The seed does not need to be randomize.


######################
# Class and Function #
######################

#Function Gender
def gender_seniority_choice(university, department):

    cond_unidep = [
        university == 'Angers' and department == 'Droit', 
        university == 'Angers' and department == 'Histoire',
        university == 'Angers' and department == 'Mathématiques',
        university == 'Angers' and department == 'Informatique', 
        university == 'Angers' and department == 'Économie',
        
        university == 'CY Cergy Paris' and department == 'Droit', 
        university == 'CY Cergy Paris' and department == 'Histoire',
        university == 'CY Cergy Paris' and department == 'Mathématiques',
        university == 'CY Cergy Paris' and department == 'Informatique', 
        university == 'CY Cergy Paris' and department == 'Économie',

        university == 'La Rochelle' and department == 'Droit', 
        university == 'La Rochelle' and department == 'Histoire',
        university == 'La Rochelle' and department == 'Mathématiques',
        university == 'La Rochelle' and department == 'Informatique', 
        university == 'La Rochelle' and department == 'Économie',
        
        university == 'Le Mans' and department == 'Droit', 
        university == 'Le Mans' and department == 'Histoire',
        university == 'Le Mans' and department == 'Mathématiques',
        university == 'Le Mans' and department == 'Informatique', 
        university == 'Le Mans' and department == 'Économie',
        
        university == 'Tours' and department == 'Droit', 
        university == 'Tours' and department == 'Histoire',
        university == 'Tours' and department == 'Mathématiques',
        university == 'Tours' and department == 'Informatique', 
        university == 'Tours' and department == 'Économie'
    ]

    choice_gend = [
        random.choice(['Femme'] * 68 + ['Homme'] * 25 + ['Non Spécifié'] * 7),
        random.choice(['Femme'] * 65 + ['Homme'] * 20 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 65 + ['Homme'] * 25 + ['Non Spécifié'] * 10),
        random.choice(['Femme'] * 55 + ['Homme'] * 40 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 75 + ['Homme'] * 15 + ['Non Spécifié'] * 10),

        random.choice(['Femme'] * 45 + ['Homme'] * 50 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 40 + ['Homme'] * 55 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 60 + ['Homme'] * 30 + ['Non Spécifié'] * 10),
        random.choice(['Femme'] * 55 + ['Homme'] * 40 + ['Non Spécifié'] * 10),
        random.choice(['Femme'] * 45 + ['Homme'] * 50 + ['Non Spécifié'] * 5),

        random.choice(['Femme'] * 50 + ['Homme'] * 45 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 50 + ['Homme'] * 45 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 45 + ['Homme'] * 50 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 45 + ['Homme'] * 50 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 40 + ['Homme'] * 40 + ['Non Spécifié'] * 20),

        random.choice(['Femme'] * 30 + ['Homme'] * 60 + ['Non Spécifié'] * 10),
        random.choice(['Femme'] * 25 + ['Homme'] * 70 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 40 + ['Homme'] * 55 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 15 + ['Homme'] * 80 + ['Non Spécifié'] * 5),
        random.choice(['Femme'] * 30 + ['Homme'] * 60 + ['Non Spécifié'] * 10),

        random.choice(['Femme'] * 30 + ['Homme'] * 40 + ['Non Spécifié'] * 30),
        random.choice(['Femme'] * 10 + ['Homme'] * 60 + ['Non Spécifié'] * 30),
        random.choice(['Femme'] * 60 + ['Homme'] * 10 + ['Non Spécifié'] * 30),
        random.choice(['Femme'] * 35 + ['Homme'] * 35 + ['Non Spécifié'] * 30),
        random.choice(['Femme'] * 40 + ['Homme'] * 30 + ['Non Spécifié'] * 30),
    ]

    
    choice_senior = [
        random.choice(['Moins de 5 ans'] * 25 + ['Entre 5 et 15 ans'] * 40 +  ['Plus de 15 ans'] * 40), 
        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 30 +  ['Plus de 15 ans'] * 30),
        random.choice(['Moins de 5 ans'] * 40 + ['Entre 5 et 15 ans'] * 40 +  ['Plus de 15 ans'] * 20), 
        random.choice(['Moins de 5 ans'] * 25 + ['Entre 5 et 15 ans'] * 40 +  ['Plus de 15 ans'] * 40),
        random.choice(['Moins de 5 ans'] * 20 + ['Entre 5 et 15 ans'] * 40 + ['Plus de 15 ans'] * 40),

        random.choice(['Moins de 5 ans'] * 40 + ['Entre 5 et 15 ans'] * 30 + ['Plus de 15 ans'] * 30), 
        random.choice(['Moins de 5 ans'] * 10 + ['Entre 5 et 15 ans'] * 60 + ['Plus de 15 ans'] * 30), 
        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 30 + ['Plus de 15 ans'] * 40), 
        random.choice(['Moins de 5 ans'] * 75 + ['Entre 5 et 15 ans'] * 15 + ['Plus de 15 ans'] * 10), 
        random.choice(['Moins de 5 ans'] * 25 + ['Entre 5 et 15 ans'] * 40 + ['Plus de 15 ans'] * 35),

        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 30 + ['Plus de 15 ans'] * 40), 
        random.choice(['Moins de 5 ans'] * 40 + ['Entre 5 et 15 ans'] * 30 + ['Plus de 15 ans'] * 30), 
        random.choice(['Moins de 5 ans'] * 25 + ['Entre 5 et 15 ans'] * 35 + ['Plus de 15 ans'] * 40), 
        random.choice(['Moins de 5 ans'] * 65 + ['Entre 5 et 15 ans'] * 25 + ['Plus de 15 ans'] * 10), 
        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 50 + ['Plus de 15 ans'] * 20),

        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 35 + ['Plus de 15 ans'] * 35), 
        random.choice(['Moins de 5 ans'] * 15 + ['Entre 5 et 15 ans'] * 35 + ['Plus de 15 ans'] * 50), 
        random.choice(['Moins de 5 ans'] * 30 + ['Entre 5 et 15 ans'] * 35 + ['Plus de 15 ans'] * 35), 
        random.choice(['Moins de 5 ans'] * 70 + ['Entre 5 et 15 ans'] * 20 + ['Plus de 15 ans'] * 10), 
        random.choice(['Moins de 5 ans'] * 20 + ['Entre 5 et 15 ans'] * 50 + ['Plus de 15 ans'] * 30),
        
        random.choice(['Moins de 5 ans'] * 60 + ['Entre 5 et 15 ans'] * 40 + ['Plus de 15 ans'] * 10), 
        random.choice(['Moins de 5 ans'] * 70 + ['Entre 5 et 15 ans'] * 35 + ['Plus de 15 ans'] * 15), 
        random.choice(['Moins de 5 ans'] * 65 + ['Entre 5 et 15 ans'] * 30 + ['Plus de 15 ans'] * 20), 
        random.choice(['Moins de 5 ans'] * 80 + ['Entre 5 et 15 ans'] * 25 + ['Plus de 15 ans'] * 10), 
        random.choice(['Moins de 5 ans'] * 55 + ['Entre 5 et 15 ans'] * 20 + ['Plus de 15 ans'] * 50),
       ]

    return(np.select(cond_unidep, choice_gend), np.select(cond_unidep, choice_senior))
    

#Function Digitalisation and seniority
def digit_gender(university, department, teach_gender):
    cond_digit = [
        university == 'Angers' and department == 'Droit' and teach_gender == 'Homme', university == 'Angers' and department == 'Droit' and teach_gender == 'Femme', university == 'Angers' and department == 'Droit' and teach_gender == 'Non Spécifié', 
        university == 'Angers' and department == 'Histoire' and teach_gender == 'Homme', university == 'Angers' and department == 'Histoire' and teach_gender == 'Femme', university == 'Angers' and department == 'Histoire' and teach_gender == 'Non Spécifié', 
        university == 'Angers' and department == 'Mathématiques' and teach_gender == 'Homme', university == 'Angers' and department == 'Mathématiques' and teach_gender == 'Femme', university == 'Angers' and department == 'Mathématiques' and teach_gender == 'Non Spécifié', 
        university == 'Angers' and department == 'Informatique' and teach_gender == 'Homme', university == 'Angers' and department == 'Informatique' and teach_gender == 'Femme',  university == 'Angers' and department == 'Informatique' and teach_gender == 'Non Spécifié', 
        university == 'Angers' and department == 'Économie' and teach_gender == 'Homme', university == 'Angers' and department == 'Économie' and teach_gender == 'Femme',  university == 'Angers' and department == 'Économie' and teach_gender == 'Non Spécifié', 

        university == 'CY Cergy Paris' and department == 'Droit' and teach_gender == 'Homme', university == 'CY Cergy Paris' and department == 'Droit' and teach_gender == 'Femme', university == 'CY Cergy Paris' and department == 'Droit' and teach_gender == 'Non Spécifié', 
        university == 'CY Cergy Paris' and department == 'Histoire' and teach_gender == 'Homme', university == 'CY Cergy Paris' and department == 'Histoire' and teach_gender == 'Femme', university == 'CY Cergy Paris' and department == 'Histoire' and teach_gender == 'Non Spécifié', 
        university == 'CY Cergy Paris' and department == 'Mathématiques' and teach_gender == 'Homme', university == 'CY Cergy Paris' and department == 'Mathématiques' and teach_gender == 'Femme', university == 'CY Cergy Paris' and department == 'Mathématiques' and teach_gender == 'Non Spécifié', 
        university == 'CY Cergy Paris' and department == 'Informatique' and teach_gender == 'Homme', university == 'CY Cergy Paris' and department == 'Informatique' and teach_gender == 'Femme',  university == 'CY Cergy Paris' and department == 'Informatique' and teach_gender == 'Non Spécifié', 
        university == 'CY Cergy Paris' and department == 'Économie' and teach_gender == 'Homme', university == 'CY Cergy Paris' and department == 'Économie' and teach_gender == 'Femme',  university == 'CY Cergy Paris' and department == 'Économie' and teach_gender == 'Non Spécifié', 

        university == 'La Rochelle' and department == 'Droit' and teach_gender == 'Homme', university == 'La Rochelle' and department == 'Droit' and teach_gender == 'Femme', university == 'La Rochelle' and department == 'Droit' and teach_gender == 'Non Spécifié', 
        university == 'La Rochelle' and department == 'Histoire' and teach_gender == 'Homme', university == 'La Rochelle' and department == 'Histoire' and teach_gender == 'Femme', university == 'La Rochelle' and department == 'Histoire' and teach_gender == 'Non Spécifié', 
        university == 'La Rochelle' and department == 'Mathématiques' and teach_gender == 'Homme', university == 'La Rochelle' and department == 'Mathématiques' and teach_gender == 'Femme', university == 'La Rochelle' and department == 'Mathématiques' and teach_gender == 'Non Spécifié', 
        university == 'La Rochelle' and department == 'Informatique' and teach_gender == 'Homme', university == 'La Rochelle' and department == 'Informatique' and teach_gender == 'Femme',  university == 'La Rochelle' and department == 'Informatique' and teach_gender == 'Non Spécifié', 
        university == 'La Rochelle' and department == 'Économie' and teach_gender == 'Homme', university == 'La Rochelle' and department == 'Économie' and teach_gender == 'Femme',  university == 'La Rochelle' and department == 'Économie' and teach_gender == 'Non Spécifié', 

        university == 'Le Mans' and department == 'Droit' and teach_gender == 'Homme', university == 'Le Mans' and department == 'Droit' and teach_gender == 'Femme', university == 'Le Mans' and department == 'Droit' and teach_gender == 'Non Spécifié', 
        university == 'Le Mans' and department == 'Histoire' and teach_gender == 'Homme', university == 'Le Mans' and department == 'Histoire' and teach_gender == 'Femme', university == 'Le Mans' and department == 'Histoire' and teach_gender == 'Non Spécifié', 
        university == 'Le Mans' and department == 'Mathématiques' and teach_gender == 'Homme', university == 'Le Mans' and department == 'Mathématiques' and teach_gender == 'Femme', university == 'Le Mans' and department == 'Mathématiques' and teach_gender == 'Non Spécifié', 
        university == 'Le Mans' and department == 'Informatique' and teach_gender == 'Homme', university == 'Le Mans' and department == 'Informatique' and teach_gender == 'Femme',  university == 'Le Mans' and department == 'Informatique' and teach_gender == 'Non Spécifié', 
        university == 'Le Mans' and department == 'Économie' and teach_gender == 'Homme', university == 'Le Mans' and department == 'Économie' and teach_gender == 'Femme',  university == 'Le Mans' and department == 'Économie' and teach_gender == 'Non Spécifié', 

        university == 'Tours' and department == 'Droit' and teach_gender == 'Homme', university == 'Tours' and department == 'Droit' and teach_gender == 'Femme', university == 'Tours' and department == 'Droit' and teach_gender == 'Non Spécifié', 
        university == 'Tours' and department == 'Histoire' and teach_gender == 'Homme', university == 'Tours' and department == 'Histoire' and teach_gender == 'Femme', university == 'Tours' and department == 'Histoire' and teach_gender == 'Non Spécifié', 
        university == 'Tours' and department == 'Mathématiques' and teach_gender == 'Homme', university == 'Tours' and department == 'Mathématiques' and teach_gender == 'Femme', university == 'Tours' and department == 'Mathématiques' and teach_gender == 'Non Spécifié', 
        university == 'Tours' and department == 'Informatique' and teach_gender == 'Homme', university == 'Tours' and department == 'Informatique' and teach_gender == 'Femme',  university == 'Tours' and department == 'Informatique' and teach_gender == 'Non Spécifié', 
        university == 'Tours' and department == 'Économie' and teach_gender == 'Homme', university == 'Tours' and department == 'Économie' and teach_gender == 'Femme',  university == 'Tours' and department == 'Économie' and teach_gender == 'Non Spécifié', 
    ]

    
    choice_digit = [
        round(random.uniform(20, 50), 2), round(random.uniform(10, 30), 2), round(random.uniform(15, 45), 2),
        round(random.uniform(10, 30), 2), round(random.uniform(10, 30), 2), round(random.uniform(10, 30), 2),
        round(random.uniform(25, 50), 2), round(random.uniform(15, 30), 2), round(random.uniform(20, 45), 2),
        round(random.uniform(30, 60), 2), round(random.uniform(20, 40), 2), round(random.uniform(25, 55), 2),
        round(random.uniform(10, 35), 2), round(random.uniform(10, 35), 2), round(random.uniform(10, 35), 2),

        round(random.uniform(35, 60), 2), round(random.uniform(25, 45), 2), round(random.uniform(35, 50), 2),
        round(random.uniform(30, 45), 2), round(random.uniform(15, 40), 2), round(random.uniform(15, 40), 2),
        round(random.uniform(40, 55), 2), round(random.uniform(35, 55), 2), round(random.uniform(35, 55), 2),
        round(random.uniform(50, 70), 2), round(random.uniform(35, 50), 2), round(random.uniform(40, 55), 2),
        round(random.uniform(40, 55), 2), round(random.uniform(20, 40), 2), round(random.uniform(20, 40), 2),

        round(random.uniform(25, 45), 2), round(random.uniform(25, 45), 2), round(random.uniform(25, 50), 2),
        round(random.uniform(15, 35), 2), round(random.uniform(15, 35), 2), round(random.uniform(15, 40), 2),
        round(random.uniform(35, 55), 2), round(random.uniform(35, 55), 2), round(random.uniform(35, 55), 2),
        round(random.uniform(40, 65), 2), round(random.uniform(35, 50), 2), round(random.uniform(40, 55), 2),
        round(random.uniform(20, 40), 2), round(random.uniform(20, 40), 2), round(random.uniform(20, 40), 2),

        round(random.uniform(25, 50), 2), round(random.uniform(25, 45), 2), round(random.uniform(25, 50), 2),
        round(random.uniform(15, 30), 2), round(random.uniform(15, 35), 2), round(random.uniform(15, 40), 2),
        round(random.uniform(35, 50), 2), round(random.uniform(35, 55), 2), round(random.uniform(35, 55), 2),
        round(random.uniform(40, 55), 2), round(random.uniform(35, 50), 2), round(random.uniform(40, 55), 2),
        round(random.uniform(20, 45), 2), round(random.uniform(20, 40), 2), round(random.uniform(20, 40), 2),

        round(random.uniform(35, 50), 2), round(random.uniform(25, 40), 2), round(random.uniform(40, 50), 2),
        round(random.uniform(35, 45), 2), round(random.uniform(25, 35), 2), round(random.uniform(40, 40), 2),
        round(random.uniform(35, 50), 2), round(random.uniform(25, 40), 2), round(random.uniform(45, 55), 2),
        round(random.uniform(35, 70), 2), round(random.uniform(25, 55), 2), round(random.uniform(40, 55), 2),
        round(random.uniform(35, 45), 2), round(random.uniform(25, 40), 2), round(random.uniform(40, 40), 2)
    ]
    
    return(np.select(cond_digit, choice_digit))

def digit_ress(gender, seniority):
    cond_digress = [
        gender == 'Homme' and seniority == 'Moins de 5 ans', 
        gender == 'Homme' and seniority == 'Entre 5 et 15 ans',
        gender == 'Homme' and seniority == 'Plus de 15 ans',

        gender == 'Femme' and seniority == 'Moins de 5 ans', 
        gender == 'Femme' and seniority == 'Entre 5 et 15 ans',
        gender == 'Femme' and seniority == 'Plus de 15 ans',

        gender == 'Non Spécifié' and seniority == 'Moins de 5 ans', 
        gender == 'Non Spécifié' and seniority == 'Entre 5 et 15 ans',
        gender == 'Non Spécifié' and seniority == 'Plus de 15 ans',]
    
    choice_digress = [
        random.choice(["Au cours de l'année 2020 à 2021"] * 55 + ["Au cours des années 2018 à 2020"] * 25 + ["Antérieure à 2018"] * 15 + ["Jamais"] * 5),
        random.choice(["Au cours de l'année 2020 à 2021"] * 30 + ["Au cours des années 2018 à 2020"] * 40 + ["Antérieure à 2018"] * 20 + ["Jamais"] * 10),
        random.choice(["Au cours de l'année 2020 à 2021"] * 10 + ["Au cours des années 2018 à 2020"] * 25 + ["Antérieure à 2018"] * 40 + ["Jamais"] * 25),

        random.choice(["Au cours de l'année 2020 à 2021"] * 50 + ["Au cours des années 2018 à 2020"] * 30 + ["Antérieure à 2018"] * 15 + ["Jamais"] * 5),
        random.choice(["Au cours de l'année 2020 à 2021"] * 25 + ["Au cours des années 2018 à 2020"] * 45 + ["Antérieure à 2018"] * 20 + ["Jamais"] * 10),
        random.choice(["Au cours de l'année 2020 à 2021"] * 5 + ["Au cours des années 2018 à 2020"] * 25 + ["Antérieure à 2018"] * 30 + ["Jamais"] * 40),

        random.choice(["Au cours de l'année 2020 à 2021"] * 50 + ["Au cours des années 2018 à 2020"] * 20 + ["Antérieure à 2018"] * 20 + ["Jamais"] * 10),
        random.choice(["Au cours de l'année 2020 à 2021"] * 30 + ["Au cours des années 2018 à 2020"] * 30 + ["Antérieure à 2018"] * 25 + ["Jamais"] * 15),
        random.choice(["Au cours de l'année 2020 à 2021"] * 15 + ["Au cours des années 2018 à 2020"] * 25 + ["Antérieure à 2018"] * 40 + ["Jamais"] * 20),
    ]

    return(np.select(cond_digress, choice_digress))

##################
# Build the Data #
##################

#Define a list of university
lst_uni = ['Angers', 'CY Cergy Paris', 'La Rochelle', 'Le Mans', 'Tours']

#Define a list of department
lst_dep = ['Droit', 'Histoire', 'Mathématiques', 'Informatique', 'Économie']

#Define a list of teacher names
db_TeacherName = pd.read_csv(path_data_names + 'French_Names_Lgh3378.csv')

#Set lists
university = []
department = []
teacher_id = []
teacher_name = []
teacher_gender = []
teacher_seniority = []
teacher_digit = []
teacher_ress = []

rand_list = [ind for ind in range(0, len(db_TeacherName['Last_Name']))]

for uni in lst_uni:
    teach_id = 1
    for dep in lst_dep:
        num_teacher = random.randint(50, 100)
        for i in range(0, num_teacher):
            rand = random.choice(rand_list)
            teach_name = db_TeacherName['Last_Name'][rand]
            teach_gender, teach_seniority = gender_seniority_choice(uni, dep)
            teach_digit = digit_gender(uni, dep, teach_gender)
            teach_ress = digit_ress(teach_gender, teach_seniority)
            if teach_ress == 'Jamais':
                teach_digit = 0
                
            #Append List
            university.append(uni)
            department.append(dep)
            teacher_id.append(teach_id)
            teacher_name.append(teach_name)
            teacher_gender.append(teach_gender)
            teacher_seniority.append(teach_seniority)
            teacher_digit.append(teach_digit)
            teacher_ress.append(teach_ress)

            if random.random() >= 0.5:
                rand_list.remove(rand)

            teach_id += 1

Teacher_Data = pd.DataFrame({
                        'Universite': university,
                        'Departement': department,
                        'Teacher_ID': teacher_id,
                        'Teacher_Name': teacher_name,
                        'Teacher_Gender': teacher_gender,
                        'Teacher_Seniority': teacher_seniority,
                        'Teacher_Digit': teacher_digit,
                        'Teacher_Ress': teacher_ress
})

print(Teacher_Data.head())


#############
# Save Data #
#############

#Save the Login into a CSV File.
Teacher_Data.to_csv(path_data + 'Digit_Gend_Senrt.csv')


##############################
# Data Gender Seniority DONE #
##############################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))