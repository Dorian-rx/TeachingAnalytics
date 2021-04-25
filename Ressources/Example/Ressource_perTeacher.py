###################################
    #Ressources par Enseignant#
###################################

# Import Packages
#Basic packages
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#######################################################

# Définir les paramètres pandas
pd.set_option("display.min_rows", 100)
#pd.set_option("display.max_columns", 10)

# Definir un seed pour garder les même valeurs aléatoirement définies.
random.seed( 2000 )

#Import CSV
Course_PerYear = pd.read_csv('Ressources\Example\Data\Ressources_perTeacher.csv')
print(Course_PerYear.head(10))

for i in Course_PerYear['Year']:
    Course_PerYear['Courses_perYear'] == len(Course_PerYear['Course_Duration'][Course_PerYear['Year'] == year])

print(Course_perYear)
