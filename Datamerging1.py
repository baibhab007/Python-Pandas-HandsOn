####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which holds the height and weight of five students s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Add a new column Gender to the dataframe df_A with values ['M', 'F', 'M', 'M', 'F'].

Create another Series s, from a list [165.4, 82.7, 'F'].

Provide the following values to the argument index: ['Student_height', 'Student_weight', 'Gender']

Set the value of the name argument of series, s, to s6.

Append the series s to the dataframe df_A, and store the captured array in df_AA.

Display the dataframe df_AA.
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4],index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height': heights_A, 'Student_weight': weights_A})
df_A['Gender']=['M', 'F', 'M', 'M', 'F']
s=pd.Series([165.4, 82.7, 'F'], index=['Student_height', 'Student_weight', 'Gender'], name='s6')
df_AA = df_A.append(s)
print(df_AA)

####
Task 2
Create another Series named heights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 170.0 and standard deviation 25.0.
Note: Set random seed to 100 before creating heights_B series. Note: Set random seed to 100 before creating weights_B series.

Create another Series named weights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 75.0 and standard deviation 12.0.

Label both Series elements as s1, s2, s3, s4 and s5.

Create a dataframe df_B containing the height and weight of students s1, s2, s3, s4 and s5 belonging to class B.

Label the columns as Student_height and Student_weight respectively.

Change the index of df_B to [ 's7', 's8', 's9', 's10', 's11'].

Create the Gender column in df_B with values ['F', 'M', 'F', 'F', 'M'].
Concatenate two dataframes df_AA and df_B, and assign the result to df. Note: Use the concat method of pandas.
Display the dataframe df.
####

np.random.seed(100)
heights_B = pd.Series(170.0+25.0*np.random.randn(5),index=['s1','s2','s3','s4','s5'])
weights_B = pd.Series(75.0+12.0*np.random.randn(5),index=['s1','s2','s3','s4','s5'])
df_B = pd.DataFrame({'Student_height':heights_B,'Student_weight':weights_B})
df_B.index(['s7','s8','s9','s10','s11'])
df_B['Gender']=['F', 'M', 'F', 'F', 'M']
df = pd.concat([df_AA, df_B])
print(df)
