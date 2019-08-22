####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent the heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Print the second element of series heights_A.

Note: Use index number or the value corresponding to the second element inside square brackets.
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4],index=['s1','s2','s3','s4','s5'])
print(heights_A['s2'])

####
Task 2
Print the middle three elements of Series heights_A.
Note: Use slice objects corresponding to index numbers or index values.
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

weights_A = pd.Series([85.1, 90.2, 76.8, 80.4, 78.9], index=['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame({'Student_height': heights_A, 'Student_weight': weights_A})
height = df_A['Student_height']
print(type(height))

####
Task 4
Select the rows corresponding to students s1, s2 of df_A, and capture them in another dataframe df_s1s2. Note: Use either .loc or .iloc methods.

Print the dataframe df_s1s2
####
