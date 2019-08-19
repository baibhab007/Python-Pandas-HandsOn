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

