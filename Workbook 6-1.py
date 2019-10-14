#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


df = df.sort_values(by=[ 'lname', 'age' ,'grade', ], ascending=[True, True, False])
df.head()

