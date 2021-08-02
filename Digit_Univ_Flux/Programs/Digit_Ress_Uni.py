################################
# Digitalisation et Université #
################################

# Import the required packages
import random
import numpy as np
from numpy.core.fromnumeric import mean
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


#Initialize a pseudorandom number generator (seed) to preserve the same values randomly obtained after any execution
random.seed( 2021 ) #The seed does not need to be randomize.


######################
# Class and Function #
######################

#Function to display the values above the barplots.
def show_values_on_bars(axs):
    def _show_on_single_plot(ax):        
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height() + 1
            value = '{:.0f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center") 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)


##################
# Build the Data #
##################

hype13_universities = ["CY Cergy Paris", "La Rochelle", "Caen Normandie", "Savoie Mont Blanc", "Tours", "°Autres"]

scolar_year = [year for year in range(2013, 2021)]

df_universities = pd.DataFrame({'Universities': hype13_universities*len(scolar_year)}).sort_values(by = 'Universities', ascending= True)
df_universities['Year'] = scolar_year*len(hype13_universities)                         

digit_ratio = []
while len(digit_ratio) != len(df_universities):
    if len(digit_ratio) == 0:
        digit_ratio.append(0.25)
    elif 0 < len(digit_ratio) <= 7:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))
    
    if len(digit_ratio) == 8:
        digit_ratio.append(0.12)
    elif 8 < len(digit_ratio) <= 15:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))
    
    if len(digit_ratio) == 16:
        digit_ratio.append(0.16)
    elif 16 < len(digit_ratio) <= 23:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))
    
    if len(digit_ratio) == 24:
        digit_ratio.append(0.20)
    elif 24 < len(digit_ratio) <= 31:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))

    if len(digit_ratio) == 32:
        digit_ratio.append(0.08)
    elif 32 < len(digit_ratio) <= 39:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))
     
    if len(digit_ratio) == 40:
        digit_ratio.append(0.30)
    elif 40 < len(digit_ratio) <= 48:
        digit_ratio.append(round(digit_ratio[-1] * random.uniform(1, 1.25), 2))
      

df_universities['Digit_ratio'] = digit_ratio
df_universities['Digit_prct'] = round(df_universities['Digit_ratio'] * 100).astype(int)

print(df_universities.head(5))


##################
# Visualizations #
##################

###########################################################################################
# 1° - HEATMAP
# Pourcentage de Digitalisation pour chaque Module des Universités Factice de 2013 à 2020 #
###########################################################################################

# Build the Data
Digitalization_Univs_pivot = df_universities.pivot("Universities", "Year", "Digit_prct")

# Build the Figure
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font',family='Times New Roman')

# Color Bar
cbar_kws = {"orientation": "vertical",
            "shrink": 1,
            'extend': 'both',
            'ticks': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
} 

#Axis
ax = sns.heatmap(Digitalization_Univs_pivot, annot=True, linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 20})
ax.set_xlabel("Année", size=24)
ax.set_ylabel("Université", size=24)

cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)

plt.text(1.2, 0.5, 'Pourcentage de Digitalisation [%]', horizontalalignment='right', verticalalignment='center', transform=ax.transAxes, rotation=90, fontsize=24)
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=20, rotation=0)

# Figure
fig.suptitle("Pourcentage de Digitalisation des Cours des Universités de 2013 à 2020", ha='center', size=26)
fig.tight_layout()

# Save Figure
fig.savefig(path_figures + "Heatmap - Prct Digit Universités 2013 à 2020")

# Display the Figure
# plt.show()

###############
# END Program #
###############