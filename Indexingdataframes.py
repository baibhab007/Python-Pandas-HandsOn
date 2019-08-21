####
Task 1
Create an index named dates representing a range of dates starting from 1-Sep-2017 to 15-Sep-2017.
Note: Use the date_range method of pandas.

Print the 3rd element of the created DateTimeIndex.
####

import datetime
import numpy as np
import pandas as pd
dates = pd.date_range(start='9/1/2017', end='9/15/2017')
print(dates[2])

####
Task 2
Convert the following date strings into datetime objects: datelist = ['14-Sep-2017', '9-Sep-2017'].
Note: Use the to_datetime method of pandas.

Capture the result in the variable 'dates_to_be_searched' and print it.
####

datelist = ['14-Sep-2017', '9-Sep-2017']
dates_to_be_searched = pd.to_datetime(datelist)
print(dates_to_be_searched)
