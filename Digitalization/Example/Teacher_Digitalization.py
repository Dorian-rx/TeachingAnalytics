##########################################################################
# Ratio of Digitalization per Teacher of University Department (Factice) #        
##########################################################################

#Import the required packages
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt


#Set a seed to keep the same values randomly defined after each execution.
seed( 1980 )


################
# Factice Data #
################

#Let us import the dataframe used for the ratio of digitalization per university department
Digitalization_Teach = pd.read_csv('Digitalization/Example/Data/Digitalization_perDepartment.csv').reset_index()

#Select three departments to build a figure
department = []
for i in range(3):
    ran_num = random.randint(0, (len(Digitalization_Teach['Department'].unique())-1))
    if Digitalization_Teach['Department'].unique()[ran_num] not in department:
            department.append(Digitalization_Teach['Department'].unique()[ran_num])
        
#Definir 3 nouveaux dataframes pour trois département aléatoire
print(department)

Digitalization_Teach_D1 = Digitalization_Teach[Digitalization_Teach['Department'] == department[0]].sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Teach_D1_2017 = Digitalization_Teach_D1[Digitalization_Teach_D1['Year'] == 2017]
Digitalization_Teach_D1_2018 = Digitalization_Teach_D1[Digitalization_Teach_D1['Year'] == 2018]
Digitalization_Teach_D1_2019 = Digitalization_Teach_D1[Digitalization_Teach_D1['Year'] == 2019]

Digitalization_Teach_D2 = Digitalization_Teach[Digitalization_Teach['Department'] == department[1]].sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Teach_D2_2017 = Digitalization_Teach_D2[Digitalization_Teach_D2['Year'] == 2017]
Digitalization_Teach_D2_2018 = Digitalization_Teach_D2[Digitalization_Teach_D2['Year'] == 2018]
Digitalization_Teach_D2_2019 = Digitalization_Teach_D2[Digitalization_Teach_D2['Year'] == 2019]

Digitalization_Teach_D3 = Digitalization_Teach[Digitalization_Teach['Department'] == department[2]].sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Teach_D3_2017 = Digitalization_Teach_D3[Digitalization_Teach_D3['Year'] == 2017]
Digitalization_Teach_D3_2018 = Digitalization_Teach_D3[Digitalization_Teach_D3['Year'] == 2018]
Digitalization_Teach_D3_2019 = Digitalization_Teach_D3[Digitalization_Teach_D3['Year'] == 2019]


##################
# Visualisations #
##################

#Matplotlib Figure
fig, ((ax10, ax11, ax12), (ax20, ax21, ax22), (ax30, ax31, ax32)) = plt.subplots(3, 3, figsize=(17, 9.5), sharey=True)
fig.suptitle("Percentage of Digitalization for each teacher of respectively the AGORA, LPTM and LT2D University Departments from 2017 to 2020", ha = 'center', size=14, fontweight='bold')
width = 0.35  #Define the width of the bars

#Make the barplots
rects10 = ax10.bar(Digitalization_Teach_D1_2017['Teacher_ID'], Digitalization_Teach_D1_2017['Digit_Percentage'], width, color = '#18ff6d')
rects11 = ax11.bar(Digitalization_Teach_D1_2018['Teacher_ID'], Digitalization_Teach_D1_2018['Digit_Percentage'], width, color = '#04e824')
rects12 = ax12.bar(Digitalization_Teach_D1_2019['Teacher_ID'], Digitalization_Teach_D1_2019['Digit_Percentage'], width, color = '#138a36')

rects20 = ax20.bar(Digitalization_Teach_D2_2017['Teacher_ID'], Digitalization_Teach_D2_2017['Digit_Percentage'], width, color = '#faa307')
rects21 = ax21.bar(Digitalization_Teach_D2_2017['Teacher_ID'], Digitalization_Teach_D2_2018['Digit_Percentage'], width, color = '#dc2f02')
rects22 = ax22.bar(Digitalization_Teach_D2_2017['Teacher_ID'], Digitalization_Teach_D2_2019['Digit_Percentage'], width, color = '#9d0208')

rects30 = ax30.bar(Digitalization_Teach_D3_2017['Teacher_ID'], Digitalization_Teach_D3_2017['Digit_Percentage'], width, color = '#ade8f4')
rects31 = ax31.bar(Digitalization_Teach_D3_2018['Teacher_ID'], Digitalization_Teach_D3_2018['Digit_Percentage'], width, color = '#00b4d8')
rects32 = ax32.bar(Digitalization_Teach_D3_2019['Teacher_ID'], Digitalization_Teach_D3_2019['Digit_Percentage'], width, color = '#023e8a')


###################
#Additional Labels#
###################

###############
#AXIS 10/11/12#
###############

ax10.set_title('Percentage of Digitalization \nFrom AGORA Department Teachers in 2017')
ax10.set_ylabel("Percentage of Digitalization")
ax10.set_xlabel("Teachers Identification")
ax10.set_xticks(Digitalization_Teach_D1_2017['Teacher_ID'])
ax10.set_xticklabels(Digitalization_Teach_D1_2017['Teacher_ID'], rotation = 45)

ax11.set_title('Percentage of Digitalization \nFrom AGORA Department Teachers in 2018')
#ax11.set_ylabel("Percentage of Digitalization")
ax11.set_xlabel("Teachers Identification")
ax11.set_xticks(Digitalization_Teach_D1_2018['Teacher_ID'])
ax11.set_xticklabels(Digitalization_Teach_D1_2018['Teacher_ID'], rotation = 45)

ax12.set_title('Percentage of Digitalization \nFrom AGORA Department Teachers in 2019')
#ax12.set_ylabel("Percentage of Digitalization")
ax12.set_xlabel("Teachers Identification")
ax12.set_xticks(Digitalization_Teach_D1_2019['Teacher_ID'])
ax12.set_xticklabels(Digitalization_Teach_D1_2019['Teacher_ID'], rotation = 45)

for rect, label in zip(rects10, Digitalization_Teach_D1_2017['Digit_Percentage']):
    height = rect.get_height()
    ax10.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects11, Digitalization_Teach_D1_2018['Digit_Percentage']):
    height = rect.get_height()
    ax11.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects12, Digitalization_Teach_D1_2019['Digit_Percentage']):
    height = rect.get_height()
    ax12.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')


###############
#AXIS 20/21/22#
###############

ax20.set_title('Percentage of Digitalization \nFrom LPTM Department Teachers in 2017')
ax20.set_ylabel("Percentage of Digitalization")
ax20.set_xlabel("Teachers Identification")
ax20.set_xticks(Digitalization_Teach_D2_2017['Teacher_ID'])
ax20.set_xticklabels(Digitalization_Teach_D2_2017['Teacher_ID'], rotation = 45)

ax21.set_title('Percentage of Digitalization \nFrom LPTM Department Teachers in 2018')
#ax21.set_ylabel("Percentage of Digitalization")
ax21.set_xlabel("Teachers Identification")
ax21.set_xticks(Digitalization_Teach_D2_2018['Teacher_ID'])
ax21.set_xticklabels(Digitalization_Teach_D2_2018['Teacher_ID'], rotation = 45)

ax22.set_title('Percentage of Digitalization \nFrom LPTM Department Teachers in 2019')
#ax22.set_ylabel("Percentage of Digitalization")
ax22.set_xlabel("Teachers Identification")
ax22.set_xticks(Digitalization_Teach_D2_2019['Teacher_ID'])
ax22.set_xticklabels(Digitalization_Teach_D2_2019['Teacher_ID'], rotation = 45)

for rect, label in zip(rects20, Digitalization_Teach_D2_2017['Digit_Percentage']):
    height = rect.get_height()
    ax20.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects21, Digitalization_Teach_D2_2018['Digit_Percentage']):
    height = rect.get_height()
    ax21.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects22, Digitalization_Teach_D2_2019['Digit_Percentage']):
    height = rect.get_height()
    ax22.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')


###############
#AXIS 30/31/32#
###############

ax30.set_title('Percentage of Digitalization \nFrom LT2D Department Teachers in 2017')
ax30.set_ylabel("Percentage of Digitalization")
ax30.set_xlabel("Teachers Identification")
ax30.set_xticks(Digitalization_Teach_D3_2017['Teacher_ID'])
ax30.set_xticklabels(Digitalization_Teach_D3_2017['Teacher_ID'], rotation = 45)

ax31.set_title('Percentage of Digitalization \nFrom LT2D Department Teachers in 2018')
#ax31.set_ylabel("Percentage of Digitalization")
ax31.set_xlabel("Teachers Identification")
ax31.set_xticks(Digitalization_Teach_D3_2018['Teacher_ID'])
ax31.set_xticklabels(Digitalization_Teach_D3_2018['Teacher_ID'], rotation = 45)

ax32.set_title('Percentage of Digitalization \nFrom LT2D Department Teachers in 2019')
#ax32.set_ylabel("Percentage of Digitalization")
ax32.set_xlabel("Teachers Identification")
ax32.set_xticks(Digitalization_Teach_D3_2019['Teacher_ID'])
ax32.set_xticklabels(Digitalization_Teach_D3_2019['Teacher_ID'], rotation = 45)

for rect, label in zip(rects30, Digitalization_Teach_D3_2017['Digit_Percentage']):
    height = rect.get_height()
    ax30.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects31, Digitalization_Teach_D3_2018['Digit_Percentage']):
    height = rect.get_height()
    ax31.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

for rect, label in zip(rects32, Digitalization_Teach_D3_2019['Digit_Percentage']):
    height = rect.get_height()
    ax32.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')


############################
#Settings and Visualization#
############################

#Last Setting
plt.ylim([0, 120]) #Set the y-axis lim
fig.tight_layout()

#Save Figure
fig.savefig("Digitalization/Example/Figures/Barplot of the Digitalization per Teacher of Department from 2017 to 2020")

#Display
plt.show()

