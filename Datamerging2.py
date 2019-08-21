####
Task 1
Create the following two Series: nameid = pd.Series(range(101, 111))

name = pd.Series(['person' + str(i) for i in range(1, 11)])

Create the dataframe master with series nameid and name. Let the column names be nameid and name respectively.

Create the dataframe transaction using the command: transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})

Merge master with transaction on nameid, and save the merged dataframe as mdf. Perform inner join. Note: Use the merge method.

Display mdf.
####

import numpy as np
import pandas as pd
nameid = pd.Series(range(101, 111))
name = pd.Series(['person' + str(i) for i in range(1, 11)])
master = pd.DataFrame({'nameid':nameid,'name':name})
transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})
mdf = master.merge(transaction)
print(mdf)
