import pandas as pd
import random
import numpy as np

Test = pd.read_csv('Ressources\Example\Data\Ressources_perTeacher.csv').reset_index()
Test = Test[0:10]

print(Test)

array_solution = [] 
list_video_1H = []
list_video_2H = []
list_video_3H = []
list_video_4H = []


random.seed( 1052 )

count = 0
for X, Y in zip(Test['Duration_Video'], Test['Number_Video']):
    if (X == 0 or Y == 0):
        array_solution.append([0,0,0,0])
        list_video_1H.append(0)
        list_video_2H.append(0)
        list_video_3H.append(0)
        list_video_4H.append(0)
    else:
        array = []
        for i in range(0, Y+1):
            for j in range(0, Y+1):
                for k in range(0, Y+1):
                    for l in range(0,Y+1):
                        if X == (1*i + 2*j + 3*k + 4*l) and Y == (i + j + k + l):
                            array.append([i,j,k,l])
                    count +=1
        if len(array) == 1:
            array_solution.append(array[0])
        elif len(array) == 0:
            array_solution.append([0,0,0,0])
            list_video_1H.append(0)
            list_video_2H.append(0)
            list_video_3H.append(0)
            list_video_4H.append(0)
        else:
            ran = random.randint(0, len(array)-1)
            array_solution.append(array[ran])
            list_video_1H.append(array[ran][0])
            list_video_2H.append(array[ran][1])
            list_video_3H.append(array[ran][2])
            list_video_4H.append(array[ran][3])


print(len(array_solution))
print(count)


#print(list_video_1H)
#Test['Number_Video_1H'] = list_video_1H