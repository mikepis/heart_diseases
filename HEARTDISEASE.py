#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd


# In[50]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[51]:


print(df.head())


# In[52]:


print(df['AnnualHouseholdIncome'].describe())


# In[53]:


import matplotlib.pyplot as plt


# In[80]:


counts = df['HistoryHD '].value_counts()
print(counts)


# In[94]:


import matplotlib.pyplot as plt


# In[95]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[81]:


counts = df['HomeSize'].value_counts()
print(counts)


# In[82]:


import matplotlib.pyplot as plt

counts = df['HomeSize'].value_counts()

fig, ax = plt.subplots()
ax = counts.plot.bar()
ax.set_xlabel('Home Size')
ax.set_ylabel('Count')
plt.show()


# In[83]:


import pandas as pd


# In[84]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[85]:


print(df.head())


# In[86]:


counts = df['Race'].value_counts()
print(counts)


# In[87]:


import matplotlib.pyplot as plt


# In[100]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[107]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")
print(df.columns)


# In[108]:


import matplotlib.pyplot as plt


# In[112]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[114]:


import pandas as pd
import matplotlib.pyplot as plt


# In[115]:


df = pd.read_excel("C:/Users/User/Desktop/mydata.xlsx")


# In[117]:


print(df.columns)


# In[119]:


df.columns = df.columns.str.strip().str.replace(' ', '')


# In[121]:


df['HistoryHD'].replace({0: 'No', 1: 'Yes'}, inplace=True)


# In[122]:


df['HistoryHD'].value_counts().plot(kind='bar')


# In[ ]:




