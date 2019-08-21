# Python-Pandas-HandsOn

Pandas

1. Pandas is a popular Python data analysis tool

Data Structure
-Series: A 1-D array.
-Data Frame: A 2-D array or two or more Series joined together
-Panel: A 3-D array

pip install --user pandas

Installation
import numpy as np
import pandas as pd

-Series
d = {'A':15, 'B':25, 'C':35}
print(pd.Series(d))
print(pd.Series(np.random.randn(5)))
print(pd.Series(np.random.randn(5), index=['a1', 'a2', 'a3', 'a4', 'a5'])

-Data Frame
d1 = {'c1': pd.Series(['A', 'B', 'C']), 'c2': pd.Series([1,2.,3.,4.])}
d2 = {'c1': ['A', 'B', 'C', 'D'], 'c2': [1,2.0,3.0,4.0]}
print(pd.DataFrame(d1))
print(pd.DataFrame(d2))

-Panel
d = {'Item1': pd.DataFrame(np.random.randn(4,3)), 'Item2': pd.DataFrame(np.random.randn(4,2))}
print(pd.Panel(d))

-Panel4D

-PanelND

-xarray package have replaced the Panel4D and PanelND


2. Accessing Data
Pandas provide utilities like loc and iloc to get data from a Series, DataFrame or Panel

Individual elements can be accessed by specifying either index number or index value, inside the square brackets.
import pandas as pd
import numpy as np
z = np.arange(10, 16)
s = pd.Series(z, index=list('abcdef'))
#Accessing 3rd element of s.
print(s[2]) # ---> Returns '12' 
#Accessing 4th element of s.
print(s['d']) # ---> Returns '13'

It is also possible to access a single element by passing index number or index value, as an argument to get method.
s.get(2) # ---> Returns '12'
s.get('d') # ---> Returns '13'

A Series can be sliced in a way, very similar to slicing a python list.
print(s[1:4])
print(s['b':'e'])
Elements corresponding to start and end index values are included, when index values are used for slicing.

-Accessing data from a Data Frame
import numpy as np
import pandas as pd
d = {'c_A' : [1,2,3,4], 'c_B' : [2,4,6,8], 'c_C' : [3,6,9,12], 'c_D' : [4,8,12,16]}
df = pd.DataFrame(d, index = ['r_one', 'r_two,', 'r_three', 'r_four'])
df['c_C']
df['c_C'][:3]
df.loc['r_four']
df.iloc[1]
df[2:4]
df['c_New'] = df['c_C'] % 2 == 0


3. Knowing a Series
It is possible to understand a Series better by using describe method
import pandas as pd
import numpy as np
temp = pd.Series(28 + 10*np.random.randn(10))
print(temp.describe())

Knowing a DataFrame
Two methods majorly info and describe can be used to know about the data, present in a data frame
You can use include argument to know about other columns
import pandas as pd
import numpy as np
df = pd.DataFrame({'temp':pd.Series(28 + 10*np.random.randn(10)), 
                'rain':pd.Series(100 + 50*np.random.randn(10)),
             'location':list('AAAAABBBBB')})
print(df.info())
print(df.describe())
print(df.describe(include=['object']))


4. Reading and Writing Data with Pandas
read_csv is used to read data from a CSV file and to_csv is utilized to write data to a CSV file

help('pandas.read_csv')
help('pandas.DatFrame.to_csv')
help('pandas.read_excel')
help('pandas.DatFrame.to_excel')
help('pandas.read_sql_table')
help('pandas.read_json')

import numpy as np
import pandas as pd
new_text = pd.read_csv('C:/JAN07.csv')
print(new_text)

import numpy as np
import pandas as pd
new_text = pd.read_csv('C:/JAN07.xlsx')
print(new_text)
d = {'xxx' : pd.Series(['yyy','zzz']),
	 'aaa' : pd.Series(['bbb','ccc']),
	 '111' : pd.Series(['222','333'])}
df = pd.DatFrame(d)
new_text = df.to_csv('C:/JAN07_1.csv', index = False)
print(new_text)

Reading data from URL
from sklearn import datasets
iris = datasets.load_iris()
iris.DESCR
import pandas as pd
import urllib
myUrl = "http://aima.cs.berkeley.edu/data/iris.csv"
urlRequest = urllib.request.Request(myUrl)
iris_file = urllib.reuqest.urlopen(urlRequest)
iris_fromUrl = pd.read_csv(iris_file,sep=',',header=None, decimal='.',names=['sepal_length','sepal_width','petal_length','petal_width','target'])
iris_fromUrl.head(6)

Reading from Databases
pip install pymysql / conda install pymysql
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+pymysql://baibhab:password@localhost:8889/employeesdb'
df = pd.read_sql_table('Persons', engine)
print(df)

Handling Large datasets
import pandas as pd
import urllib
myUrl = "http://aima.cs.berkeley.edu/data/iris.csv"
urlRequest = urllib.request.Request(myUrl)
iris_file = urllib.reuqest.urlopen(urlRequest)
myIrisIterator = pd.read_csv(iris_file,sep=',',header=None, decimal='.',names=['sepal_length','sepal_width','petal_length','petal_width','target'], iterator=True)
print(myIrisIterator.get_chunk(15).shape)
print(myIrisIterator.get_chunk(15)

Reading data from JSON
pandas provides the utilities read_json and to_json to deal with JSON strings or files
EmployeeRecords = [{'EmployeeID':451621, 'EmployeeName':'Preeti Jain', 'DOJ':'30-Aug-2008'},
{'EmployeeID':123621, 'EmployeeName':'Ashok Kumar', 'DOJ':'25-Sep-2016'},
{'EmployeeID':451589, 'EmployeeName':'Johnty Rhodes', 'DOJ':'04-Nov-2016'}]
import json
emp_records_json_str = json.dumps(EmployeeRecords)
df = pd.read_json(emp_records_json_str, orient='records', convert_dates=['DOJ'])
print(df)

5. Indexing DataFrame
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5,2))
df.index = [ 'row_' + str(i) for i in range(1, 6) ]
df

Pandas supports generating a range of dates, with methods like date_range, bdate_range
import pandas as pd
print(pd.date_range('1/1/2016', periods=36, freq='D')
print(pd.date_range('1/1/2016', periods=4, freq='BQ')
print(pd.to_datetime(['20150720','20161028'],format='%Y%m%d'))
print(pd.to_datetime([''20160915','some string'], format='%Y%m%d', errors='coerce'))
print(pd.to_datetime(pd.DataFrame({'year': [2014,2015], 'month': [7,2], 'day': [28,16]})))

Hierarchical Indexing
myarrays = [['blue','blue','red','red','yellow','yellow'],['true','false','true','false','true','false']]
import numpy as np
import pandas as pd
myindex = pd.MultiIndex.from_arrays(myarrays, names=['name1','name2'])
print(myindex)
myseries = pd.Series(np.random.randn(6),index=myindex)
print(myseries)
print(myseries['blue'])
print(myseries['blue','true'])


6. Data Cleaning
Pandas provide methods like drop_duplicates, isnull, etc to deal with missing data

remove duplicate records
d = d.drop_duplicates()

to find missing values
d['cname'].isnull().value_counts()

extract string data
d['cname'].str.extract('(\w+)')

replace string data
d['newCol'] =
d['cname'].str.replace('^pink','blue')

remove all rows with missing data
d = d.dropna(how='any')

replace missing data
df.fillna(0)
df.fillna(method='pad')
df.fillna(df.mean())

Data cleansing with Python: Exploratory cleaning, Production cleaning, Machine learning to clean data, Data merging, Rebuilding missing data, Standardize data, Normalize data, De-duplicate data

Steps:
Import data
Merge datasets
Rebuilding missing data
Standardize data
Normalize data
De-duplicate
Verify and Enrich
Export data

Replace missing data example
import pandas as pd
city_data = pd.read_csv('C:/JAN07.csv', sep=',',parse_dates=[0])
print(city_data)
print(city_data.fillna(city_data.mean(axis=0)))

removing errorious data example
my_data = pd.read_csv('C:/JAN07.csv') 
print(my_data) //will give error
my_data = pd.read_csv('C:/JAN07.csv', error_bad_lines=False) 
print(my_data) //will not give error


7. Data Aggregation

import numpy as np
import pandas as pd
import urllib
myUrl = "http://aima.cs.berkeley.edu/data/iris.csv"
urlRequest = urllib.request.Request(myurl)
iris_fp = urllib.request.urlopen(urlRequest)
iris = pd.read_csv(iris_fp, sep=',', header=None, decimal='.', names=['sepal_length','sepal_width','petal_length','petal_width','target'])
print(type(iris))
print(iris.head(6))
print(iris['target'].count())
df = iris[iris['target']=='setosa']
print(df)
print(df.count())
print(df['target'].count())
print(df['petal_length'].mean())
print(df['petal_length'].min())
print(df['petal_length'].max())
print(df['petal_length'].std())

Transforming data example
df = pd.DataFrame({'temp':pd.Series(28 + 10*np.random.randn(10)),
                   'rain':pd.Series(100 + 50*np.random.randn(10)),
                   'location':list('AAAAABBBBB')
})
print(df.head(2))
replacements = {
'location': {'A':'Hyderabad', 'B':'Mumbai'}
}
df = df.replace(replacements, regex=True)
print(df.head(2))
mumbai_data = df.loc[df.location.str.contains('umb'),:]
print(mumbai_data.head(2))
regions = df.groupby('location')
print(regions.mean())


8. Merging Data
Pandas provide merge method to join two data frames

import numpy as np
import pandas as pd
df1 = pd.DataFrame({'key':['K0','K1','K2','K3'], 'A':['A0','A1','A2','A3'], 'B':['B0','B1','B2','B3']})
df2 = pd.DataFrame({'key':['K0','K1','K2','K3'], 'C':['C0','C1','C2','C3'], 'D':['D0','D1','D2','D3']})
print(pd.merge(df1,df2,on='key'))
df3 = pd.DataFrame({'key':['K0','K1','K4','K3'], 'C':['C0','C1','C2','C3'], 'D':['D0','D1','D2','D3']})
print(pd.merge(df1,df3,on='key',how='left'))
dfleft = pd.DataFrame({'key1':['K0','K0','K1','K1'], 'key2':['K0','K1','K2','K3'], 'A':['A0','A1','A2','A3'], 'B':['B0','B1','B2','B3']})
dfright = pd.DataFrame({'key1':['K0','K0','K2','K1'], 'key2':['K0','K1','K1','K2'], 'A':['A0','A1','A2','A3'], 'B':['B0','B1','B2','B3']})
print(pd.merge(dfleft,dfright,on=['key1','key2']))
