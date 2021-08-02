################################
# Ressources et Digitalisation #
################################

# Import the required packages
import numpy as np
from numpy.lib.arraysetops import unique
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


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

Resources = pd.read_csv(path_data + 'Resources.csv')


##################
# Visualizations #
##################

############################################################################################################
# 1° - HEATMAP
# Pourcentage de Digitalisation pour chaque Module des Départements de l'Université Factice de 2013 à 2020 #
############################################################################################################

# Build the Data
Digitalization_Depts = Resources.groupby(['Departement', 'Year'])['Digitalization_Ressource_Percent'].mean().reset_index()
Digitalization_Depts['Digitalization_Ressource_Percent'] = round(Digitalization_Depts['Digitalization_Ressource_Percent']).astype(int)
Digitalization_Depts_pivot = Digitalization_Depts.pivot("Departement", "Year", "Digitalization_Ressource_Percent")

# Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

# Color Bar
cbar_kws = {"orientation": "vertical",
            "shrink": 1,
            'extend': 'both',
            'ticks': [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43],
} 

#Axis
ax = sns.heatmap(Digitalization_Depts_pivot, annot=True, linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 20})
ax.set_xlabel("Année", size=24)
ax.set_ylabel("Département", size=24)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)

plt.text(1.2, 0.5, 'Pourcentage de Digitalisation [%]', horizontalalignment='right', verticalalignment='center', transform=ax.transAxes, rotation=90, fontsize=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20, rotation=0)

# Figure
fig.suptitle("Pourcentage de Digitalisation des Cours de chaque Département de l'Université de 2013 à 2020", ha='center', size=26)
fig.tight_layout()

# Save Figure
fig.savefig(path_figures + "Heatmap - Prct Digit Département 2013 à 2020")

# Display the Figure
# plt.show()


############################################################################################################################################
# 2° - BOXPLOTS
# Distribution of the Digitalization Percentage for each Module of the Factice University Department of Computer Science from 2013 to 2020 #
############################################################################################################################################

# Build the Data
Digitalization_CptScs = Resources[Resources['Departement'] == 'Informatique']

# Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

# Axis
ax = sns.boxplot(x="Year", y="Digitalization_Ressource_Percent", hue = "Year", dodge = False, data=Digitalization_CptScs, palette = 'magma')
ax.set_xlabel("Année", size=24)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=24)
ax.set_xticklabels(Digitalization_CptScs['Year'].unique(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
ax.get_legend().remove()

# Figure
fig.suptitle("Répartition du Pourcentage de Digitalisation des Cours du Département d'Informatique de 2013 à 2020", ha = 'center', size=24)
fig.tight_layout()

# Save Figure
fig.savefig(path_figures + "Boxplots - Rprt Pcrt Digit Département Informatique 2013 à 2020")

# Display the Figure
# plt.show()


################################################################################################################################################
# 3° - Barplots
# Percentage of Digitalisation for each Module of all Teachers from the Artificial University Department of Computer Science from 2017 to 2020 #  
################################################################################################################################################

#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Departement'] == 'Informatique']
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2016]

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
sns.barplot(x ="Teacher_Name", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral", ci = 50, capsize=0.1)
ax.set_xlabel("Nom de l'Enseignant", size=24)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.07, 0.5), shadow=True, prop={'size':20}, labelspacing=0.5)
leg.set_title('Année', prop = {'size': 24}) 

plt.ylim([0, 51]) #Set the y-axis li

# Figure
fig.suptitle("Répartition du Pourcentage de Digitalisation des Cours par Enseignant du Département d'Informatique de 2016 à 2020", ha = 'center', size=24)
fig.tight_layout()

#Save Figure
fig.savefig(path_figures + "Barplots - Rprt Prct Digit Teachers Département Informatique 2016 à 2020")

#Display
#plt.show()


#######################################################################################################################################
# 4° - Barplots
# Pourcentage de Digitalisation de certains Modules de Mr ROGIER du Département d'Informatique de l'Université Factice de 2013 à 2020 #         
#######################################################################################################################################

####
#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Course_ID'].isin([60,64,41,68,70])]
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2016]
Module_Title_FR = ["Les Logiciels", "Réseaux et Internet", "Systèmes Informatiques", "Sécurité Informatique", "Manipulation de Données"]
Digitalization_Teach_CptSc['Module_Title'] = Digitalization_Teach_CptSc['Course_ID'].replace([60,64,41,68,70], Module_Title_FR)

#Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')


#Axis
sns.barplot(x ="Course_ID", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral")
ax.set_xlabel("Nom du Cours", size=24)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=24)
ax.set_xticklabels(unique(Digitalization_Teach_CptSc['Module_Title']), size = 20, rotation = 0)
plt.setp(ax.get_yticklabels(), fontsize=20)
leg = ax.legend(loc='center', bbox_to_anchor=(1.07, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Année', prop = {'size': 24, 'family':'Times New Roman'})
show_values_on_bars(ax, 2, 1)

plt.ylim([0, max(Digitalization_Teach_CptSc['Digitalization_Ressource_Percent']) + 5]) #Set the y-axis lim

#Figure
fig.suptitle("Pourcentage de Digitalisation de certains Cours de Mr ROGIER du Département d'Informatique de 2016 à 2020", ha = 'center', size=24)
fig.tight_layout()

#Save Figure
fig.savefig(path_figures + "Barplots - Prct Digit a Teacher Département Informatique 2016 à 2020")

#Display
#plt.show()


###############
# END Program #
###############