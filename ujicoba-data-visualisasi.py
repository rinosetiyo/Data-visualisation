#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import pandas
import pandas as pd

# membuat list buah
buah = ['jeruk','melon','pisang','semangka','apel']

# membuat series dari list buah
a = pd.Series(buah, index=[1,2,3,4,5])
a


# In[9]:


# membuat series dengan indeks default
b = pd.Series(buah)
b


# In[10]:


# membuat dictionary
dic = {'ID': [110, 276, 298, 312, 501, 529],
      'Name': ['Mark','Michelle','Alina','Noah','Justin','Sherin'],
      'Gender': ['Male','Female','Female','Male','Male','Female']}
df_x = pd.DataFrame(dic)
df_x


# In[11]:


df = pd.read_csv('austin_weather.csv')
df


# In[12]:


# menampilkan data teratas
df.head()


# In[13]:


# menampilkan data terbawah
df.tail()


# In[14]:


# melihat info singkat masing masing kolom
df.info()


# In[15]:


# melihat deskriptif statistik
df.describe()


# In[16]:


# menampilkan kolom templowf sebagai series
a = df['TempLowF']
a


# In[17]:


# menampilkan beberapa kolom
b = df[['Date','TempAvgF','HumidityAvgPercent','WindAvgMPH']]
b


# In[18]:


# menampilkan data teratas dari beberapa kolom
df[['Date','TempAvgF','HumidityAvgPercent','WindAvgMPH']].head()


# In[19]:


# menampilkan data pada indeks baris 1 kolom 2
df.iloc[1,2]


# In[20]:


# menampilkan data pada indeks baris 872 kolom 16
df.iloc[872,16]


# In[21]:


# menampilkan data pada indeks baris 1199 kolom 8
df.iloc[1199,8]


# In[22]:


# menampilkan data baris 0 kolom Tempavgf
df.loc[0,'TempAvgF']


# In[23]:


# menampilkan data baris 100 kolom date
df.loc[100,'Date']


# In[24]:


# menampilkan data baris 1287 kolom windhighmph
df.loc[1287,'WindHighMPH']


# In[25]:


# slicing dataframe
df.iloc[0:6, 2:5]


# In[26]:


# Outliers materi
import pandas as pd
import numpy as np
df = pd.read_csv('automobile.data', header=None)
df.head()


# In[27]:


# membuat list nama kolom
column_names = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style',
               'drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type',
               'num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower',
               'peak-rpm','city-mpg','highway-mpg','price']

# mengubah nama kolom
df.columns = column_names
df.head()


# In[28]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# memeriksa outliers menggunakan box plot
df['wheel-base'].plot(kind='box')
plt.title('Box plot of Wheel Base', size=16)
plt.show()


# In[29]:


import seaborn as sns
sns.boxplot(y=df['engine-size']).set_title('Box plot Engine Size', size=16)


# In[30]:


# membuat boxplot untuk kolom symboling berdasarkan kolom fuel type
sns.boxplot(y=df['symboling'], x=df['fuel-type']).set_title('Group by fuel type', size=16)


# In[31]:


# memeriksa outliers dengan scatter plot matplotlib
df.plot(kind='scatter', x='engine-size', y='wheel-base')

plt.xlabel('Engine Size')
plt.ylabel('Wheel Base')
plt.show()


# In[32]:


# memeriksa outliers dengan scatter plot seaborn
sns.scatterplot(x=df['engine-size'], y=df['compression-ratio']).set(xlabel='Engine Size', ylabel='Compression Ratio')


# In[33]:


# menghitung nilai IQR
Q1 = df['wheel-base'].quantile(0.25)
Q3 = df['wheel-base'].quantile(0.75)
IQR = Q3 - Q1

print('Q1 = ', Q1)
print('Q3 = ', Q3)
print('IQR wheel base = ', IQR)


# In[34]:


# memeriksa outlier
nilai_min = df['wheel-base'].min()
nilai_max = df['wheel-base'].max()

min_IQR = Q1 - 1.5 * IQR
max_IQR = Q3 + 1.5 * IQR

# buat kondisi untuk mencari low outlier
if (nilai_min < min_IQR):
    print('Low outlier is found <', min_IQR)
    print('Low outlier index : ', list(df[df['wheel-base'] < min_IQR].index))
    
# buat kondisi untuk mencari high outlier
if (nilai_max > max_IQR):
    print('High outlier is found >', max_IQR)
    print('High outlier index : ', list(df[df['wheel-base'] > max_IQR].index))


# In[35]:


# menghitung IQR dan memeriksa outlier untuk semua kolom bertipe int64 dan float64
for i in (df.columns):
    if (df[i].dtypes in ['int64', 'float64']):
        print(i, ':' ,df[i].dtypes)
        
        Q1 = df[i].quantile(0.25)
        print('Q1', Q1)
        
        Q3 = df[i].quantile(0.75)
        print('Q3', Q3)
        
        IQR = Q3 - Q1
        print('IQR', IQR)
        

        nilai_min = df[i].min()
        nilai_max = df[i].max()

        min_IQR = Q1 - 1.5 * IQR
        max_IQR = Q3 + 1.5 * IQR

        # buat kondisi untuk mencari low outlier
        if (nilai_min < min_IQR):
            print('Low outlier is found <', min_IQR)
            print('Low outlier index : ', list(df[df[i] < min_IQR].index))

        # buat kondisi untuk mencari high outlier
        if (nilai_max > max_IQR):
            print('High outlier is found >', max_IQR)
            print('High outlier index : ', list(df[df[i] > max_IQR].index))
            
        print('\n')


# In[36]:


# menampilkan data yang mengandung outliers pada kolom wheel base
df.iloc[[70,71,73], :]


# In[37]:


# menghapus baris yang mengandung outliers pada kolom wheel base
df.drop([70,71,73], axis = 0)


# In[64]:


from itertools import chain

outlier_index = []

for i in (df.columns):
    if (df[i].dtypes in ['int64', 'float64']):
        print(i, ':' ,df[i].dtypes)

        Q1 = df[i].quantile(0.25)
        print('Q1', Q1)

        Q3 = df[i].quantile(0.75)
        print('Q3', Q3)

        IQR = Q3 - Q1
        print('IQR', IQR)


        nilai_min = df[i].min()
        nilai_max = df[i].max()

        min_IQR = Q1 - 1.5 * IQR
        max_IQR = Q3 + 1.5 * IQR

        # buat kondisi untuk mencari low outlier
        if (nilai_min < min_IQR):
            print('Low outlier is found <', min_IQR)
            print('Low outlier index : ', list(df[df[i] < min_IQR].index))

        # buat kondisi untuk mencari high outlier
        if (nilai_max > max_IQR):
            print('High outlier is found >', max_IQR)
            print('High outlier index : ', list(df[df[i] > max_IQR].index))
            outlier_index.append(list(df[df[i] > max_IQR].index))
        print('\n')
        
        # mengaplikasikan chain, serta mengambil nilai uniknya saja, lalu memasukkan dalam list baru
unique_out_ind = list(set(list(chain(*outlier_index))))
print(unique_out_ind)


# In[65]:


# mencetak indeks data yang mengandung outlier secara terurut
print(sorted(unique_out_ind))


# In[66]:


# menampilkan seluruh baris data yang mengandung outliers
df.iloc[sorted(unique_out_ind), :]


# In[72]:


# menghapus seluruh baris yang mengandung outliers
df.drop(sorted(unique_out_ind), axis=0).head(8)


# In[73]:


# menghapus outliers dan mereset indeksnya
df_without_outlier = df.drop(sorted(unique_out_ind), axis=0)

# mereset indeks dataframe setelah menghapus outliers
df_without_outlier.reset_index(drop=True, inplace=True)
df_without_outlier.head(8)


# In[ ]:





# In[ ]:




