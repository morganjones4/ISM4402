#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:


df.hist()


# In[ ]:


df.hist(column="age")


# In[ ]:


df.hist(column="age", by="gender")

