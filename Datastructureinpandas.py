####
Python Pandas | 1 | Data Structures in Pandas
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent the height of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Determine the shape of heights_A and display it.
####

import numpy as np
import pandas as pd
heights_A = pd.Series(np.array([176.2, 158.4, 167.6, 156.2, 161.4]),index=['s1','s2','s3','s4','s5'])
print(heights_A.shape)

####
Task 2
Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent the weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Determine data type of values in weights_A and display it.
####

weights_A = pd.Series(np.array([85.1, 90.2, 76.8, 80.4, 78.9]),index=['s1','s2','s3','s4','s5'])
print(weights_A.dtype)

####
Task 3
Create a dataframe named df_A, which contains the height and weight of five students namely s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Display the shape of df_A
####

df_A = pd.DataFrame(list(zip(heights_A,weights_A)), index = ['s1', 's2', 's3', 's4', 's5'], columns = ['Student_height', 'Student_weight'] )
print(df_A.shape)


####
Task 4
Create another series named heights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 170.0 and standard deviation 25.0.
Create another series named weights_B from a 1-D numpy array of 5 elements derived from the normal distribution of mean 75.0 and standard deviation 12.0.
Label both series elements as s1, s2, s3, s4 and s5.
Print the mean of series heights_B
####

heights_B_mean, heights_B_std = 170.0,25.0
weights_b_MEAN, weights_B_std = 75.0, 12.0
np.random.seed(100)
heights_B = pd.Series(np.random.normal(heights_B_mean, heights_B_std, 5), index=['s1', 's2', 's3', 's4', 's5'])
np.random.seed(100)
weights_B = pd.Series(np.random.normal(weights_B_mean, weights_B_std, 5), index=['s1', 's2', 's3', 's4', 's5'])
print(heights_B.mean())


####
Task 5
Create a dataframe df_B containing the height and weight of students s1, s2, s3, s4 and s5 belonging to class B.

Label the columns as Student_height and Student_weight respectively.

Display the column names of df_B.
####

df_B = pd.DataFrame(list(zip(heights_B,weights_B)), index = ['s1', 's2', 's3', 's4', 's5'], columns = ['Student_height', 'Student_weight'] )
print(df_B.columns)


####
Task 6
Create a panel p, containing the previously created two dataframes df_A and df_B.

Label the first dataframe as ClassA, and second as ClassB.

Determine the shape of panel p and display it.
####

data = {'ClassA' : df_A, 'ClassB' : df_B}
p = pd.Panel(data)
print(p.shape)
