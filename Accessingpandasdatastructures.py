####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent the heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Print the second element of series heights_A.
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4], index = ['s1','s2','s3','s4','s5'])
print(heights_A[1])

####
Task 2
Print the middle three elements of Series heights_A.
####
print(heights_A['s2':'s4'])

####
Task 3
Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent the weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which contains the height and weight of five students namely s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Select the column df_A referring to student heights, and store it in the variable height. Note: Specify the required column name inside square brackets.

Print the type of object of the variable height.
####

weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index=['s1','s2','s3','s4','s5'])
d1 = {'Student_height': heights_A, 'Student_weight' : weights_A}
df_A = pd.DataFrame(d1)
height = df_A['Student_height']
print(type(height))

####
Task 4
Select the rows corresponding to students s1, s2 of df_A, and capture them in another dataframe df_s1s2. Note: Use either .loc or .iloc methods.

Print the dataframe df_s1s2.
####

df_s1s2 = df_A.loc['s1':'s2']
print(df_s1s2)

####
Task 5
Select the rows corresponding to students s1, s2 and s5 of df_A in the order s2, s5, s1, and capture them in another dataframe df_s2s5s1.
Note: Make use of either .loc or .iloc methods.

Print the dataframe df_s2s5s1
####

df_s2s5s1 = df_A.loc[1],df_A.loc[4], df_A.loc[0]
print(df_s2s5s1)



