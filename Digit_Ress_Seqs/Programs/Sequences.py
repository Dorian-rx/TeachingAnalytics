#####################################
# Séquences des Cours et Ressources #     
#####################################

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

#
def Prep_Seq(rng1, rng2, string):
    temp_seq = []
    rng = rng1 - rng2
    for l in range(rng):
        temp_seq.append(string)
    return(temp_seq)


#
def pos(array, str_array):
    index_str = [i for i in range(len(array)) if array[i] in str_array]   #Find the index of the identical ID as the current «course» selected ID.    
    if len(index_str) == 0:
        pass
    elif len(index_str) == 1:
        nw_position = len(array) - 1
        old_position = index_str[0]
        value_exchange = array[nw_position]
        array[nw_position] = array[old_position]
        array[old_position] = value_exchange
    else:
        for index, i in zip(index_str, range(1, len(index_str)+1)):
            nw_position = round(((len(array) - 1)*i)/len(index_str))
            old_position = index
            value_exchange = array[nw_position]
            array[nw_position] = array[old_position]
            array[old_position] = value_exchange

    if 'Examen' in array:
        index_exam = [i for i in range(len(array)) if array[i] == 'Examen']   #Find the index of the identical ID as the current «course» selected ID.    
        nw_position = len(array) - 1
        old_position = index_exam[0]
        value_exchange = array[nw_position]
        array[nw_position] = array[old_position]
        array[old_position] = value_exchange

    return array

#
def swap(glob_array, add_array, strng_change):
    for add in add_array:
        index = [i for i in range(len(glob_array)) if glob_array[i] == strng_change]   #Find the index of the identical ID as the current «course» selected ID.    
        if index != []:
            if len(index) == 0:
                continue
            else:
                glob_array[random.choice(index)] = add
                
    return glob_array


#################################
# Import the required Data file #
#################################

#Import the dataframe
Resources_Sequence = pd.read_csv(path_data + 'Resources.csv')

#Drop the first column of the dataframe (empty)
Resources_Sequence = Resources_Sequence.iloc[: , 1:]

##################
# Build the Data #
##################

#Basic Sequence Lists
basic_SeqJoint = []   #Basic List containing the sequence joint of each course

#Temporary ID:
temp_ID = []

#Loop 
for seq, course_ID in zip(range(0, len(Resources_Sequence)), Resources_Sequence['Course_ID']):
    if course_ID in temp_ID:
        ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        basic_SeqJoint_INS = [basic_SeqJoint[ins[-1]]]
        basic_SeqJoint_INS = basic_SeqJoint_INS[0].split('-')

        #Digit
        num_Video = Resources_Sequence['Number_Video'].iloc[ins[-1]]
        num_QCM = Resources_Sequence['Number_QCM'].iloc[ins[-1]]
        num_Test = Resources_Sequence['Number_Test'].iloc[ins[-1]]

    else: 
        num_Video = num_QCM = num_Test = 0
        num_Lecture = num_Exercise = num_Exam = 0

    Digit_VidTemp = Prep_Seq(Resources_Sequence['Number_Video'].iloc[seq], num_Video, 'Video')
    Digit_QCMTemp = Prep_Seq(Resources_Sequence['Number_QCM'].iloc[seq], num_QCM, 'QCM')
    Digit_ExamTemp = Prep_Seq(Resources_Sequence['Number_Test'].iloc[seq], num_Test, 'Test')

    if course_ID in temp_ID: 
        #Basic List
        basic_SeqTemp = swap(basic_SeqJoint_INS, Digit_VidTemp, 'Lecture')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_QCMTemp, 'Exercise')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_ExamTemp, 'Examen')
        basic_SeqTemp = pos(basic_SeqTemp, ['Test', 'Examen'])
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)

    else:
        #Presentiel
        num_Lecture = 0
        num_Exercise = 0
        num_Exam = 0
        Pres_LectTemp = Prep_Seq(Resources_Sequence['Number_Lecture'].iloc[seq], num_Lecture, 'Lecture')
        Pres_ExerTemp = Prep_Seq(Resources_Sequence['Number_Exercise'].iloc[seq], num_Exercise, 'Exercise')
        Pres_ExamTemp = Prep_Seq(Resources_Sequence['Number_Exam'].iloc[seq], num_Exam, 'Examen')

        #Basic List
        basic_SeqTemp = Digit_VidTemp + Pres_LectTemp +  Digit_QCMTemp + Pres_ExerTemp + Digit_ExamTemp + Pres_ExamTemp
        random.shuffle(basic_SeqTemp)
        basic_SeqTemp = pos(basic_SeqTemp, ['Test', 'Examen'])      
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)
        
    temp_ID.append(course_ID)

Resources_Sequence['Sequence'] = basic_SeqJoint
print(Resources_Sequence.head(5))


#######################
# Preparing Sequences #
#######################

list_Course_ID = []
list_Course_Year = [] 
list_Duration = []
list_Ress_Digit = []
list_Ress_inClass = []
list_Resources = []
list_Count = []
list_BasicSeq = []

for num in range(len(Resources_Sequence)):
    count = 1
    list_basic = Resources_Sequence.iloc[num]['Sequence'].split("-")
    for basic in list_basic:
        list_Course_ID.append(Resources_Sequence.iloc[num]['Course_ID'])
        list_Course_Year.append(Resources_Sequence.iloc[num]['Year'])
        list_Duration.append(Resources_Sequence.iloc[num]['Course_Duration'])
        list_Ress_Digit.append(Resources_Sequence.iloc[num]['Course_Ress_Digit'])
        list_Ress_inClass.append(Resources_Sequence.iloc[num]['Course_Ress_inClass'])
        list_Resources.append(Resources_Sequence.iloc[num]['Course_Resources'])
        list_Count.append(count) 
        list_BasicSeq.append(basic)
        count += 1

Prepared_Sequence = pd.DataFrame({'Course_ID': list_Course_ID,
              'Year': list_Course_Year,
              'Course_Duration': list_Duration,
              'Course_Ress_Digit': list_Ress_Digit,
              'Course_Ress_inClass': list_Ress_inClass,
              'Resources_Amount': list_Resources,
              'Resources_Rank': list_Count,
              'Resources_Type_Basic': list_BasicSeq,
})

print(Prepared_Sequence.head(5))


#############
# Save Data #
#############

#Save the «Resources_Sequence» into a CSV file.
Resources_Sequence.to_csv(path_data + 'Resources_Sequence.csv')

#Save the «Prepared_Sequence» into a CSV File.
Prepared_Sequence.to_csv(path_data + 'Prepared_Sequences.csv')


#######################
# Data Sequences DONE #
#######################

Total_Time = round(time.time() - start_time, 2)
print("Program Execution Time: %s seconds" % (Total_Time))
