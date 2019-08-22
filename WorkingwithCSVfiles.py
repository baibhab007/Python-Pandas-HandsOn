####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which contains the height and weight of five students namely s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Write the contents of df_A to a CSV file named classA.csv.

Note: Use the to_csv method associated with a dataframe.

Verify if the file classA.csv exists in the present directory using command ls -l.

You can also view the contents of the file using the command cat classA.csv
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4],index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height': heights_A, 'Student_weight': weights_A})
df_A.to_csv('classA.csv')

####
Task 2
Read the contents of the CSV file, classA.csv into a dataframe named df_A2. Note: Use read_csv method of pandas.

Display the dataframe df_A2.
####

df_A2 = pd.read_csv('classA.csv')
print(df_A2)

####
Task 3
Read the contents of the CSV file classA.csv into a dataframe named df_A3, such that the first column data values are treated as index to df_A3.
Note: Use the index_col argument of read_csv method.

Display the dataframe df_A3.
####

df_A3 = pd.read_csv('classA.csv', index_col='Unnamed: 0')
print(df_A3)

####
Task 4
Create another Series named heights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 170.0 and standard deviation 25.0.
Note: Set random seed to 100 before creating heights_B series. Use numpy.

Create another Series named weights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 75.0 and standard deviation 12.0.
Note: Set random seed to 100 again before creating weights_B series. Use numpy.

Label both Series elements with s1, s2, s3, s4 and s5.

Create a dataframe df_B containing the height and weight of students s1, s2, s3, s4 and s5 belonging to class B.

Label the columns as Student_height and Student_weight respectively.

Write the contents of df_B without the index to a CSV file named classB.csv. Note: Use the index argument of to_csv method.

Verify if the file classB.csv exists in the present directory using the command ls -1.

Display the contents of classB.csv using the command cat classB.csv.
####

