#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('datasets_316056_639173_amazon.csv', encoding = "ISO-8859-1", engine = 'python')


# In[3]:


df.head()


# In[10]:


df.describe(include = 'all').transpose()


# In[5]:


#checking is there any NaN values present
df.isna().sum()


# In[6]:


df.shape


# In[7]:


df.replace(0, np.nan, inplace = True)


# In[8]:


df.dropna(subset = ['number'], inplace = True)


# In[11]:


df.shape


# In[13]:


df['number']


# In[14]:


df['state'].nunique()


# In[18]:


df.groupby('state').sum().sort_values('number')


# In[19]:


get_ipython().system('jupyter nbconvert --to script config_template.ipynb')

