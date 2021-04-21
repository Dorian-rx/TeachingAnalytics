#Teaching Analytics


############################################
    #Taux d'Hybridation par Enseignant#
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
random.seed( 1965 )

#Let us use the previous dataframe that display the hybridation of each teacher
EN_Hybridation_teach_db = pd.read_csv('Hybridation/Example/Data/Hybridation_perDepartment.csv').reset_index()

#Definir 4 nouveaux dataframes pour chaque niveau d'hybridation
Low_Hybridation_teach_db = EN_Hybridation_teach_db[EN_Hybridation_teach_db['Hybridation_Level'] == 'Low Hybridation'].sort_values(by = 'Teacher_ID', ascending = True)
MidLow_Hybridation_teach_db = EN_Hybridation_teach_db[EN_Hybridation_teach_db['Hybridation_Level'] == 'Medium-Low Hybridation'].sort_values(by = 'Teacher_ID', ascending = True)
MidHigh_Hybridation_teach_db = EN_Hybridation_teach_db[EN_Hybridation_teach_db['Hybridation_Level'] == 'Medium-High Hybridation'].sort_values(by = 'Teacher_ID', ascending = True)
High_Hybridation_teach_db = EN_Hybridation_teach_db[EN_Hybridation_teach_db['Hybridation_Level'] == 'High Hybridation'].sort_values(by = 'Teacher_ID', ascending = True)


#Visualisations

fig, ((ax1), (ax2), (ax3), (ax4)) = plt.subplots(4, 1, figsize=(20, 9), sharey=True  )
fig.tight_layout()
fig.suptitle("Répartition du nombre d'heures enseigné à travers des MOOCs et des cours magistraux, \n dependamment du niveau d'Hybridation, et, pour chaque enseignant (sample=141)", ha = 'center', size=14, fontweight='bold')
fig.subplots_adjust(top=0.91)

#Matplotlib Figure
width = 0.35
rects10 = ax1.bar(np.arange(len(Low_Hybridation_teach_db['Teacher_ID']))-(width/2), Low_Hybridation_teach_db['Teaching_Duration_MOOC'], width, label='Faible Hybridation - MOOC', color = '#b3b3ff')
rects11 = ax1.bar(np.arange(len(Low_Hybridation_teach_db['Teacher_ID']))+(width/2), Low_Hybridation_teach_db['Teaching_Duration_Lecture'], width, label='Faible Hybridation - Lecture', color = '#1a1aff')

rects20 = ax2.bar(np.arange(len(MidLow_Hybridation_teach_db['Teacher_ID']))-(width/2), MidLow_Hybridation_teach_db['Teaching_Duration_MOOC'], width, label='Moyen-Faible Hybridation - MOOC', color = '#80ff80')
rects21 = ax2.bar(np.arange(len(MidLow_Hybridation_teach_db['Teacher_ID']))+(width/2), MidLow_Hybridation_teach_db['Teaching_Duration_Lecture'], width, label='Moyen-Faible Hybridation - Lecture', color = '#009900')

rects30 = ax3.bar(np.arange(len(MidHigh_Hybridation_teach_db['Teacher_ID']))-(width/2), MidHigh_Hybridation_teach_db['Teaching_Duration_MOOC'], width, label='Moyen-Forte Hybridation - MOOC', color = '#ff9999')
rects31 = ax3.bar(np.arange(len(MidHigh_Hybridation_teach_db['Teacher_ID']))+(width/2), MidHigh_Hybridation_teach_db['Teaching_Duration_Lecture'], width, label='Moyen-Forte Hybridation - Lecture', color = '#cc0000')

rects40 = ax4.bar(np.arange(len(High_Hybridation_teach_db['Teacher_ID']))-(width/2), High_Hybridation_teach_db['Teaching_Duration_MOOC'], width, label='Forte Hybridation - MOOC', color = '#ffcc80')
rects41 = ax4.bar(np.arange(len(High_Hybridation_teach_db['Teacher_ID']))+(width/2), High_Hybridation_teach_db['Teaching_Duration_Lecture'], width, label='Forte Hybridation - Lecture', color = '#e68a00')

#Ajouter des labels

#ax1
ax1.set_ylabel("Heures d'enseignement")
ax1.set_xticks(np.arange(len(Low_Hybridation_teach_db['Teacher_ID'])))
ax1.set_xticklabels(Low_Hybridation_teach_db['Teacher_ID'])
ax1.legend()

for rect, label in zip(rects10, Low_Hybridation_teach_db['Teaching_Duration_MOOC']):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects11, Low_Hybridation_teach_db['Teaching_Duration_Lecture']):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

#ax2
ax2.set_ylabel("Heures d'enseignement")
ax2.set_xticks(np.arange(len(MidLow_Hybridation_teach_db['Teacher_ID'])))
ax2.set_xticklabels(MidLow_Hybridation_teach_db['Teacher_ID'])
ax2.legend()

"""
for rect, label in zip(rects20, MidLow_Hybridation_teach_db['Teaching_Duration_MOOC']):
    height = rect.get_height()
    ax2.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects21, MidLow_Hybridation_teach_db['Teaching_Duration_Lecture']):
    height = rect.get_height()
    ax2.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
"""

#ax3
ax3.set_ylabel("Heures d'enseignement")
ax3.set_xticks(np.arange(len(MidHigh_Hybridation_teach_db['Teacher_ID'])))
ax3.set_xticklabels(MidHigh_Hybridation_teach_db['Teacher_ID'])
ax3.legend()

"""
for rect, label in zip(rects30, MidHigh_Hybridation_teach_db['Teaching_Duration_MOOC']):
    height = rect.get_height()
    ax3.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects31, MidHigh_Hybridation_teach_db['Teaching_Duration_Lecture']):
    height = rect.get_height()
    ax3.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
"""

#ax4
ax4.set_ylabel("Heures d'enseignement")
ax4.set_xticks(np.arange(len(High_Hybridation_teach_db['Teacher_ID'])))
ax4.set_xticklabels(High_Hybridation_teach_db['Teacher_ID'])
ax4.legend()

for rect, label in zip(rects40, High_Hybridation_teach_db['Teaching_Duration_MOOC']):
    height = rect.get_height()
    ax4.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects41, High_Hybridation_teach_db['Teaching_Duration_Lecture']):
    height = rect.get_height()
    ax4.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')


ax1.set_xlabel("Identifiant de l'Enseignant")
ax2.set_xlabel("Identifiant de l'Enseignant")
ax3.set_xlabel("Identifiant de l'Enseignant")
ax4.set_xlabel("Identifiant de l'Enseignant")

fig.tight_layout()
fig.suptitle("Répartition du nombre d'heures enseigné à travers des MOOCs et des cours magistraux, \n dependamment du niveau d'Hybridation, et, pour chaque enseignant (sample=141)", ha = 'center', size=14, fontweight='bold')
fig.subplots_adjust(top=0.91)

plt.ylim([0, 600])

#Save Figure
fig.savefig("Hybridation/Example/Figures/Barplots sur le niveau d'hybridation par enseignant")

#Display
#plt.show()

