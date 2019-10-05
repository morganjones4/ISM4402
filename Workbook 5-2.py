#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[ ]:


GradeList = zip(names,grades,hoursstudy)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades','BS', 'MS', 'PhD'])
df


# In[ ]:


df.count()


# In[ ]:


df.std()


# In[ ]:


df.min()


# In[ ]:


df.max()


# In[ ]:


df.quantile(.25)


# In[ ]:


df.quantile(.5)


# In[ ]:


df.quantile(.75)

