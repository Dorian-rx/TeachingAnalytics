##################################
# Digitalisation et Réingénierie #
##################################

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
            value = '{:.2f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center", fontsize = 16, fontname = "Times New Roman") 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax, width, height)
    else:
        _show_on_single_plot(axs, width, height)


#################################
# Import the required Data file #
#################################

Quizz = pd.read_csv(path_data + 'Quizzes.csv')


##################
# Visualizations #
##################

####################################################################################################
# 1° - HEATMAP
# Pourcentage de Réussite pour chaque Quiz des Départements de l'Université Factice de 2015 à 2020 #
####################################################################################################

#Build the Data
Quizz_Depts = Quizz.groupby(['Departement', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Departement", "Year", "Success_Prct")

#Build the figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')


cbar_kws = {"orientation": "vertical",
            "shrink": 1,
            'extend': 'both',
            'ticks': [31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61] ,
} # color bar keyword arguments

#Axis
ax = sns.heatmap(Quizz_Depts_pivot, annot= True, linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 20})
ax.set_xlabel("Année", size=24)
ax.set_ylabel("Département", size=24)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)

plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20, rotation=0)


#Figure
fig.suptitle("Pourcentage de Réussite aux Quiz des Cours de chaque Département de l'Université de 2015 à 2020", ha = 'center', size=24)
fig.tight_layout()

#Save Figure
fig.savefig(path_figures  + "Heatmap - Prct Réussite Département 2015 à 2020")

#Display the Figure
#plt.show()


#####################################################################################################################
# 2° - HEATMAP
# Pourcentage de Réussite pour chaque Quiz du Département de Mathématique de l'Université Factice de 2015 à 2020    #
#####################################################################################################################

#Build the Data
Quizz_Depts = Quizz[Quizz['Departement'] == "Mathématiques"]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': [27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51] ,
} # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 20})
ax.set_xlabel("Année", size=24)
ax.set_ylabel("Nom du Cours", size=24)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)

plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20, rotation=0)

#Figure
fig.suptitle("Pourcentage de Réussite aux Quiz de certains Cours du Département de Mathématiques de 2015 à 2020", ha = 'center', size=24)
fig.tight_layout()

#Save Figure
fig.savefig(path_figures  + "Heatmap - Prct Réussite Département Mathématiques 2015 à 2020")

#Display the Figure
#plt.show()


#####################################################################################################################
# 3° - BARPLOTS
# Pourcentage de Réussite pour chaque Quiz du Département de Mathématique de l'Université Factice de 2015 à 2020    #
#####################################################################################################################

#Build the data
Quizz['Correct_Difficulty_Rank'] = Quizz['Correct_Difficulty'].replace(['Facile', 'Moyen', 'Difficile'],[0, 1, 2])
Quizz['Quizz_Type_Rank'] = Quizz['Quizz_Type'].replace(['QCU', 'QCM', 'QROC', 'QO'],[0, 1, 2, 3])
Quizz = Quizz.sort_values(by = ['Correct_Difficulty_Rank', 'Quizz_Type_Rank'], ascending = True)


#Build the figure
sns.set_style("white")
fig, ax = plt.subplots(1, 2, figsize=(16, 9), sharey=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')


sns.barplot(x="Quizz_Type", y="Guess", hue = 'Correct_Difficulty', data=Quizz, palette = "flare", ax = ax[0], capsize=.2)
ax[0].set_title("Répartition des valeurs du «Guess», \n en fonction du Type et du Niveau de Difficulty des Quiz", size=20)
ax[0].set_xlabel("Types des Quiz", size=22)
ax[0].set_ylabel("Valeurs", size=22)
ax[0].get_legend().remove()
plt.setp(ax[0].get_xticklabels(), fontsize=20)
plt.setp(ax[0].get_yticklabels(), fontsize=20, rotation=0)
show_values_on_bars(ax[0], 1.8, 0.04)


sns.barplot(x="Quizz_Type", y="Slip",  hue = 'Correct_Difficulty', data=Quizz, palette = "flare", ax = ax[1], capsize=.2)
ax[1].set_title("Répartition des valeurs du «Slip», \n en fonction du Type et du Niveau de Difficulty des Quiz", size=20)
ax[1].set_xlabel("Types des Quiz", size=22)
ax[1].set_ylabel("", size=22)   
plt.setp(ax[1].get_xticklabels(), fontsize=20)
show_values_on_bars(ax[1], 2.2, 0.04)

leg = ax[1].legend(loc='center', bbox_to_anchor=(1.18, 0.5), shadow=True, prop={'size':20, 'family': 'Times New Roman' }, labelspacing=0.5)
leg.set_title('Difficulté', prop = {'size': 22, 'family':'Times New Roman'})

plt.ylim([0, 1])

#Figure
fig.suptitle("Répartition des valeurs du «Guess» et du «Slip» en fonction du Type et du Niveau de Difficulté de l'Intégralité des Quiz ", ha = 'center', size=22)
fig.subplots_adjust(top=0.860, bottom=0.08, left=0.06, right=0.860, hspace=0.2, wspace=0.05)

#Save Figure
fig.savefig(path_figures  + "Barplots - Rprt Slip and Guess per Type and Difficulty Level")

#Display the plots
#plt.show()


###############
# END Program #
###############
