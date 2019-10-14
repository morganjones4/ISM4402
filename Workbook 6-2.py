#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


def gen_to_num(x):
    if x =='Female':
        return 1 
    if x == 'Male':
        return 0


# In[ ]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[ ]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gen_val', data=df).fit()
result.summary()


# In[ ]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gen_val', data=df).fit()
result.summary()

