####
Task 1
Create a series named heights_A with values 176.2, 158.4, 167.6, 156.2, and 161.4. These values represent heights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create another series named weights_A with values 85.1, 90.2, 76.8, 80.4, and 78.9. These values represent weights of 5 students of class A.

Label each student as s1, s2, s3, s4, and s5.

Create a dataframe named df_A, which contains the height and weight of five students namely s1, s2, s3, s4 and s5.

Label the columns as Student_height and Student_weight, respectively.

Set height and weight values of student s3 to NaN .

Note: Use .loc to select the s3 record and set the values to np.nan.

Set the weight of s5 to NaN.

Drop the rows having null values in any of the columns, and assign the result to df_A2. Note: Use the dropna method.

Display the dataframe df_A2.
####

import numpy as np
import pandas as pd
heights_A = pd.Series([176.2, 158.4, 167.6, 156.2, 161.4],index=['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1, 90.2, 76.8, 80.4, 78.9],index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height': heights_A, 'Student_weight': weights_A})
df_A.iloc[2]=np.nan
df_A['s5']=np.nan
df_A2=df_A.dropna(how='any')
print(df_A2)
