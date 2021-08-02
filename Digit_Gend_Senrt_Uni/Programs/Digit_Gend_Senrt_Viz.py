#######################################
# Digitalisation, Genre et Ancienneté #
#######################################

#Import the required packages
import numpy as np
from numpy.lib.arraysetops import unique
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

######################
# Class and Function #
######################

#Function to display the values above the barplots.
def show_values_on_bars(axs, width, height):
    def _show_on_single_plot(ax, width, height):        
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / width
            _y = p.get_y() + p.get_height() + height
            value = '{:.0f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center", fontsize = 18, fontname = "Times New Roman") 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax, width, height)
    else:
        _show_on_single_plot(axs, width, height)


#################################
# Import the required Data file #
#################################

Teacher_DSG = pd.read_csv(path_data + 'Digit_Gend_Senrt.csv')


##################
# Visualizations #
##################

#########################################################################
# 1° - Heatmap
# Pourcentage de Digitalisation pour chaque Département des Universités #
#########################################################################

# Build the Data
Teacher_Digit_UniDep = Teacher_DSG.groupby(['Universite', 'Departement'])['Teacher_Digit'].mean().reset_index()
Teacher_Digit_UniDep['Teacher_Digit'] = round(Teacher_Digit_UniDep['Teacher_Digit']).astype(int)
Teacher_Digit_UniDep = Teacher_Digit_UniDep.pivot("Universite", "Departement", "Teacher_Digit")

# Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

# Color Bar
cbar_kws = {"orientation": "vertical",
            "shrink": 1,
            'extend': 'both',
            'ticks': [15, 18, 21, 24, 27, 30, 33, 36, 39],
} 

#Axis
ax = sns.heatmap(Teacher_Digit_UniDep, annot=True, linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 20})
ax.set_xlabel("Département", size=24)
ax.set_ylabel("Université", size=24)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)

plt.text(1.2, 0.5, 'Pourcentage de Digitalisation [%]', horizontalalignment='right', verticalalignment='center', transform=ax.transAxes, rotation=90, fontsize=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20, rotation=0)

# Figure
fig.suptitle("Pourcentage de Digitalisation des Cours pour des Département d'Universités Similaire", ha='center', size=24)
fig.tight_layout()

# Save Figure
fig.savefig(path_figures + "Heatmap - Prct Digit Départements Universités")

# Display the Figure
#plt.show()


################################################################
# 2° - Barplots
# Répartition du Genre des Enseignants au sein des Universités # 
################################################################

#Build the Data
Teacher_DSG_Gender = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Gender'])['Teacher_Gender'].count().reset_index(name='count')
Teacher_DSG_Gender2 = Teacher_DSG.groupby(['Universite', 'Departement'])['Teacher_Gender'].count().reset_index(name='count')

Gender_Prct = []
for uni1, dep1, count1 in zip(Teacher_DSG_Gender['Universite'], Teacher_DSG_Gender['Departement'], Teacher_DSG_Gender['count']):
    for uni2, dep2, count2 in zip(Teacher_DSG_Gender2['Universite'], Teacher_DSG_Gender2['Departement'], Teacher_DSG_Gender2['count']):
        if uni1 == uni2 and dep1 == dep2:
            prct = round((count1 / count2) * 100, 2)
            Gender_Prct.append(prct)
Teacher_DSG_Gender['Gender_Prct'] = Gender_Prct


#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
order_gender = ["Femme", "Homme", "Non Spécifié"]
sns.barplot(x ="Universite", y = 'Gender_Prct', data = Teacher_DSG_Gender, hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral", ci = 68, capsize= 0.05)
ax.set_xlabel("Nom de l'Université", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)
plt.ylim([0, 76]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition du Genre des Enseignants au sein des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.82)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Genre Universites")

#Display
#plt.show()


#################################################################################
# 3° - Barplots
# Répartition du Genre des Enseignants au sein des Départements des Universités # 
#################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Gender_Prct', data = Teacher_DSG_Gender, hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral", ci = 60, capsize=0.05)
ax.set_xlabel("Nom du Département", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)

plt.ylim([0, 65]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition du Genre des Enseignants au sein des Départements des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.820)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Genre Departments Universites")

#Display
#plt.show()


###################################################################################
# 4° - Barplots
# Répartition du Genre des Enseignants au sein des Départements de CY Cergy Paris # 
###################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Gender_Prct', data = Teacher_DSG_Gender[Teacher_DSG_Gender['Universite'] == 'CY Cergy Paris'], hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral")
ax.set_xlabel("Nom du Déparement", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 2, 1)

plt.ylim([0, 65]) #Set the y-axis lim

#Figure
fig.suptitle("Genres des Enseignants au sein des Départements de CY Cergy Paris", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.820)

#Save Figure
fig.savefig(path_figures + "Barplots - Genre Departments Universite")

#Display
#plt.show()


#######################################################################
# 5° - Barplots
# Répartition de l'Ancienneté des Enseignants au sein des Universités # 
#######################################################################

#Build the Data
Teacher_DSG_Senior = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Seniority'])['Teacher_Seniority'].count().reset_index(name='count')
Teacher_DSG_Senior2 = Teacher_DSG.groupby(['Universite', 'Departement'])['Teacher_Seniority'].count().reset_index(name='count')

Seniority_Prct = []
for uni1, dep1, count1 in zip(Teacher_DSG_Senior['Universite'], Teacher_DSG_Senior['Departement'], Teacher_DSG_Senior['count']):
    for uni2, dep2, count2 in zip(Teacher_DSG_Senior2['Universite'], Teacher_DSG_Senior2['Departement'], Teacher_DSG_Senior2['count']):
        if uni1 == uni2 and dep1 == dep2:
            prct = round((count1 / count2) * 100, 2)
            Seniority_Prct.append(prct)
Teacher_DSG_Senior['Seniority_Prct'] = Seniority_Prct


#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Universite", y = 'Seniority_Prct', data = Teacher_DSG_Senior, hue = "Teacher_Seniority", palette = "rocket", hue_order = ['Moins de 5 ans', 'Entre 5 et 15 ans', 'Plus de 15 ans'], ci = 68, capsize= 0.05)
ax.set_xlabel("Nom de l'Université", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.135, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title("Niveau d'Ancienneté", prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)

plt.ylim([0, 60]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition de l'Ancienneté des Enseignants au sein des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.80)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Ancienneté Universites")

#Display
#plt.show()


########################################################################################
# 6° - Barplots
# Répartition de l'Ancienneté des Enseignants au sein des Départements des Universités # 
########################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Seniority_Prct', data = Teacher_DSG_Senior, hue = "Teacher_Seniority", palette = "rocket", hue_order = ['Moins de 5 ans', 'Entre 5 et 15 ans', 'Plus de 15 ans'], ci = 60, capsize=0.025)
ax.set_xlabel("Nom du Département", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.135, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title("Niveau d'Ancienneté", prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.25, 0.5)

plt.ylim([0, 70]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition de l'Ancienneté des Enseignants au sein des Départements des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.80)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Ancienneté Departments Universites")

#Display
#plt.show()


##########################################################################################
# 7° - Barplots
# Répartition de l'Ancienneté des Enseignants au sein des Départements de CY Cergy Paris # 
##########################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Seniority_Prct', data = Teacher_DSG_Senior[Teacher_DSG_Senior['Universite'] == 'CY Cergy Paris'], hue = "Teacher_Seniority", palette = "rocket", hue_order = ['Moins de 5 ans', 'Entre 5 et 15 ans', 'Plus de 15 ans'])
ax.set_xlabel("Nom du Département", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.135, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title("Niveau d'Ancienneté", prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 2, 1)

plt.ylim([0, 70]) #Set the y-axis lim

#Figure
fig.suptitle("Ancienneté des Enseignants au sein des Départements de CY Cergy Paris", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.80)

#Save Figure
fig.savefig(path_figures + "Barplots - Anciennete Departments Universite")

#Display
#plt.show()


#################################################################################################
# 8° - Barplots
# Répartition de la Digitalisation en fonction du Genre des Enseignants au sein des Universités # 
#################################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Universite", y = 'Teacher_Digit', data = Teacher_DSG, hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral", ci = 90, capsize= 0.05)
ax.set_xlabel("Nom de l'Université", size=24)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)

plt.ylim([0, 45]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition du Pourcentage de Digitalisation des cours, \n en fonction du Genre des Enseignants au sein des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.82)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Digit Genre Universites")

#Display
#plt.show()


##################################################################################################################
# 9° - Barplots
# Répartition de la Digitalisation en fonction du Genre des Enseignants au sein des Départements des Universités # 
##################################################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Teacher_Digit', data = Teacher_DSG, hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral", ci = 60, capsize=0.05)
ax.set_xlabel("Nom du Département", size=24)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)

plt.ylim([0, 50]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition du Pourcentage de Digitalisation des cours, \n en fonction du Genre des Enseignants au sein des Départements des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.820)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Digit Genre Departments Universites")

#Display
#plt.show()

####################################################################################################################
# 10° - Barplots
# Répartition de la Digitalisation en fonction du Genre des Enseignants au sein des Départements de CY Cergy Paris # 
####################################################################################################################

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Departement", y = 'Teacher_Digit', data = Teacher_DSG[Teacher_DSG['Universite'] == 'CY Cergy Paris'], hue = "Teacher_Gender", hue_order=order_gender, palette = "Spectral", ci = 68, capsize = 0.025)
ax.set_xlabel("Nom du Déparement", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.25, 0.5)

plt.ylim([0, 60]) #Set the y-axis lim

#Figure
fig.suptitle("Répartition du Pourcentage de Digitalisation des cours, \n en fonction du Genre des Enseignants au sein des Départements de CY Cergy Paris", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.820)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Digit Genre Departments Universite")

#Display
#plt.show()


#####################################################################################################################
# 11° - Barplots
# Répartition de la période de dernière digitalisation en fonction du Genre des Enseignants au sein des Universités # 
#####################################################################################################################

#Build the Data
Teacher_DSG_Ress = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Gender', 'Teacher_Ress'])['Teacher_Ress'].count().reset_index(name='count')
Teacher_DSG_Ress2 = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Gender'])['Teacher_Ress'].count().reset_index(name='count')


Ress_Prct = []
for uni1, dep1, gend1, count1 in zip(Teacher_DSG_Ress['Universite'], Teacher_DSG_Ress['Departement'], Teacher_DSG_Ress['Teacher_Gender'], Teacher_DSG_Ress['count']):
    for uni2, dep2, gend2, count2 in zip(Teacher_DSG_Ress2['Universite'], Teacher_DSG_Ress2['Departement'], Teacher_DSG_Ress2['Teacher_Gender'], Teacher_DSG_Ress2['count']):
        if uni1 == uni2 and dep1 == dep2 and gend1 == gend2:
            prct = round((count1 / count2) * 100, 2)
            Ress_Prct.append(prct)
   
Teacher_DSG_Ress['Ress_Prct'] = Ress_Prct


#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
order_ress = ["Au cours de l'année 2020 à 2021", "Au cours des années 2018 à 2020", "Antérieure à 2018", "Jamais"]
order_gender = ["Femme", "Homme", "Non Spécifié"]
sns.barplot(x ="Teacher_Ress", y = 'Ress_Prct', data = Teacher_DSG_Ress, order = order_ress, hue = "Teacher_Gender", hue_order = order_gender, palette = "Spectral", ci = 68, capsize= 0.05)
ax.set_xlabel("Période de la Dernière Digitalisation d'une Ressource", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
ax.set_xticklabels(['Entre 2020 et 2021', 'Entre 2018 et 2020', 'Antérieure à 2018', 'Jamais'], size = 20)
plt.setp(ax.get_yticklabels(), fontsize=20)

leg = ax.legend(loc='center', bbox_to_anchor=(1.12, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Genre', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.3, 0.5)

plt.ylim([0, 45]) #Set the y-axis lim

#Figure
fig.suptitle("Répartitition de la Dernière Période de Digitalisation d'une Ressource, \n en fonction du Genre des Enseignants au sein des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.82)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt RessDigit Universites")

#Display
#plt.show()

############################################################################################################################
# 12° - Barplots
# Répartition de la période de dernière digitalisation en fonction de l'Ancienneté des Enseignants au sein des Universités # 
############################################################################################################################

#Build the Data
Teacher_DSG_Ress = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Seniority', 'Teacher_Ress'])['Teacher_Ress'].count().reset_index(name='count')
Teacher_DSG_Ress2 = Teacher_DSG.groupby(['Universite', 'Departement', 'Teacher_Seniority'])['Teacher_Ress'].count().reset_index(name='count')


Ress_Prct = []
for uni1, dep1, sen1, count1 in zip(Teacher_DSG_Ress['Universite'], Teacher_DSG_Ress['Departement'], Teacher_DSG_Ress['Teacher_Seniority'], Teacher_DSG_Ress['count']):
    for uni2, dep2, sen2, count2 in zip(Teacher_DSG_Ress2['Universite'], Teacher_DSG_Ress2['Departement'], Teacher_DSG_Ress2['Teacher_Seniority'], Teacher_DSG_Ress2['count']):
        if uni1 == uni2 and dep1 == dep2 and sen1 == sen2:
            prct = round((count1 / count2) * 100, 2)
            Ress_Prct.append(prct)
   
Teacher_DSG_Ress['Ress_Prct'] = Ress_Prct


#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
order_ress = ["Au cours de l'année 2020 à 2021", "Au cours des années 2018 à 2020", "Antérieure à 2018", "Jamais"]
order_seniority = ["Moins de 5 ans", "Entre 5 et 15 ans", "Plus de 15 ans"]
sns.barplot(x ="Teacher_Ress", y = 'Ress_Prct', data = Teacher_DSG_Ress, order = order_ress, hue = "Teacher_Seniority", hue_order = order_seniority,  palette = "rocket", ci = 80, capsize= 0.05)
ax.set_xlabel("Période de la Dernière Digitalisation d'une Ressource", size=24)
ax.set_ylabel("Pourcentage [%]", size=24)
ax.set_xticklabels(['Entre 2020 et 2021', 'Entre 2018 et 2020', 'Antérieure à 2018', 'Jamais'], size = 20)
plt.setp(ax.get_yticklabels(), fontsize=20)

leg = ax.legend(loc='center', bbox_to_anchor=(1.135, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title("Niveau d'Ancienneté", prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 1.30, 0.5)

plt.ylim([0, 60]) #Set the y-axis lim

#Figure
fig.suptitle("Répartitition de la Dernière Période de Digitalisation d'une Ressource, \n en fonction de l'Ancienneté des Enseignants au sein des Universités", ha = 'center', size=24)
fig.tight_layout()
fig.subplots_adjust(right=0.80)

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt RessSeniority Universites")

#Display
#plt.show()

###############
# END Program #
###############