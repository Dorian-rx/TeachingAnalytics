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
pd.set_option("display.min_rows", 100)
#pd.set_option("display.max_columns", 10)


# Definir un seed pour garder les même valeurs aléatoirement définies.
random.seed( 2000 )

#Import CSV
Course_PerYear = pd.read_csv('Ressources\Example\Data\Ressources_perTeacher.csv')

video = ['Course_ID', 'Year', 'Duration_Video', 'Number_Video', 'Number_Video_1H', 'Number_Video_2H', 'Number_video_3H', 'Number_Video_4H']
Course_PerYear_Video = Course_PerYear[video]

print(Course_PerYear_Video)