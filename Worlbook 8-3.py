#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location= "datasetsgradedata/csv"
df=pd.read_csv(Location)
df.head()


# In[ ]:


plt.scatter(df['Hours'], df['grade'])

