#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np

column_names = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style',
               'drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type',
               'num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower',
               'peak-rpm','city-mpg','highway-mpg','price']

df = pd.read_csv('automobile.data', names = column_names)
df.head(3)


# In[29]:


df.info()


# In[30]:


# memeriksa kolom normalized-losses

df['normalized-losses'].head(10)


# In[31]:


# definisikan format missing values
missing_value_format = ['N.A','na','n.a.','n/a','?','-']

# tambahkan parameter untuk memformat missing values
df = pd.read_csv('automobile.data', names = column_names, na_values = missing_value_format)
df.head()


# In[32]:


df.info()


# In[33]:


# menandai missing value
df['normalized-losses'].isnull().head(10)


# In[34]:


df['normalized-losses'].notnull().head(10)


# In[35]:


# mengecek missing values untuk keseluruhan dataframe
df.isnull().values.any()


# In[36]:


# mengecek missing values untuk tiap kolom
df.isnull().any()


# In[37]:


# memeriksa jumlah missing values tiap kolom
df.isnull().sum()


# In[38]:


# menghapus baris
df.dropna(subset=['price'],axis = 0, inplace = True)

# mereset index
df.reset_index(drop = True, inplace = True)
df.head()


# In[39]:


# mengecek jumlah masing kategori di kolom num-of-doors
df['num-of-doors'].value_counts()


# In[40]:


# mengisi missing value
df['num-of-doors'].fillna('four', inplace = True)


# In[41]:


df['normalized-losses'].fillna(df['normalized-losses'].mean(), inplace = True)


# In[42]:


df.head()


# In[43]:


# mengisi missing value pada kolom bore dengan nilai sebelumnya
df['bore'].fillna(method = 'pad', inplace = True)


# In[44]:


# replace missing value pada kolom peak-rpm dengan mean
df['peak-rpm'].replace(np.nan, df['peak-rpm'].mean(), inplace = True)


# In[45]:


df.info()


# In[ ]:





# In[ ]:




