####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent the heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent the weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which holds the height and weight of five students s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Filter the rows from df_A, whose Student_height > 160.0 and Student_weight < 80.0, and capture them in another dataframe df_A_filter1.

Print the dataframe df_A_filter1.
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4],index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height': heights_A, 'Student_weight': weights_A})
df_A_filter = df_A[(df_A['Student_height'] > 160.0) & (df_A['Student_weight'] < 80.0)]
print(df_A_filter)


####
Task 2
Filter the rows from df_A, whose index values end with 5, and capture them in another dataframe df_A_filter2.

Print the dataframe df_A_filter2.
####

df_A_filter2 = df_A.loc[['s5']]
print(df_A_filer2)

#####

Task 3
Create a new column Gender in the dataframe df_A using the command: df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']
Group df_A based on Gender, and capture the result in df_groups.
Print the mean height and weight of each group. Note: Use the groupby method to group df_A, and then call the mean method on grouped data df_groups.

####

df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']
df_groups = df_A.groupby('Gender').mean()
print(df_groups)
