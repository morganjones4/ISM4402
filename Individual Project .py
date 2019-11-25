#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

Location = 'downloads/datasets/datasets/axisdata.csv'
df = pd.read_csv(Location)
df.head()


# In[4]:


df['Cars Sold'].mean()


# In[7]:


df['Cars Sold'].max()


# In[6]:


df['Cars Sold'].min()


# In[8]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[9]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[13]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[12]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[16]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])


# In[19]:


pd.pivot_table(df, values=['Hours Worked'], index=['SalesTraining'])

