#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os #to start the work 1st thing import the os only to load data
os.chdir('C:/Users/hp/OneDrive/Desktop/herovired')  #change the back slash to forward slash to run 
os.getcwd()


# In[5]:


os.listdir() #it shows all the files of the directory we loaded


# In[6]:


import pandas as pd
df=pd.read_excel('01 Super Mart Case Study Data.xlsx',sheet_name='Data')
df


# ### NUMBER OF CUSTOMERS WHO HAVE ACCEPTED CAMPAIGN 1 AND CAMPAIGN 2 (1)

# In[7]:


df[df['AcceptedCmp1']&df['AcceptedCmp2']==1]


# ### NUMBER OF WEBPURCHASES PER WEB VISIT (2)

# In[8]:


df1=df.groupby('NumWebVisitsMonth').agg({'NumWebPurchases':['mean']})
df1


# In[9]:


df1['NumWebPurchases'].describe()


# In[10]:


df


# In[11]:


df.columns


# In[12]:


df2=df.loc[:,['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']]
df2


# In[13]:


df['Total Spends']=df2.sum(axis=1)
df


# In[14]:


df['Total Spends'].max()


# In[15]:


Total_Spends1=pd.crosstab(df['Total Spends'],columns=df['NumWebVisitsMonth']<10)
Total_Spends1


# ### TOTAL SPENDS FOR WEB VISITS<10 (3)

# In[16]:


Total_Spends1.describe()


# ### TOTAL SPENDS VS DIFFERENT TYPES OF PURCHASES (INCLUDE ONLY MEAN AND 50TH PERCENTILE OF TOTAL SPENDS) (4)

# ### ON WEBVISITS PERMONTH

# In[17]:


df[df['NumWebVisitsMonth']<10].describe()


# In[18]:


df[df['NumWebVisitsMonth']>=10].describe()


# ### ON NUMBER OF DEALS PURCHASES

# In[19]:


df[df['NumDealsPurchases']>=10].describe()


# ### ON NUMBER OF STORE PURCHASES

# In[20]:


df[df['NumStorePurchases']>=10].describe()


# In[21]:


df[df['NumStorePurchases']<10].describe()


# In[22]:


df


# In[23]:


df.info()


# In[24]:


import seaborn as sns
sns.set_theme()


# In[ ]:





# ### TYPE OF PURCHASES VS TOTAL SPENDS (5)

# In[25]:


sns.barplot(data=df,x='NumDealsPurchases',y='Total Spends',ci=None);


# In[26]:


sns.barplot(data=df,x='NumStorePurchases',y='Total Spends',ci=None);


# In[27]:


sns.barplot(data=df,x='NumWebPurchases',y='Total Spends',ci=None);


# In[28]:


sns.barplot(data=df,x='NumCatalogPurchases',y='Total Spends',ci=None);


# ### TOTAL SPENDS VS PRODUCTS (6)

# In[30]:


import matplotlib.pyplot as plt


# In[31]:


plt.scatter(data=df,x='MntWines',y='Total Spends');


# In[32]:


plt.scatter(data=df,x='MntFruits',y='Total Spends');


# In[33]:


plt.scatter(data=df,x='MntMeatProducts',y='Total Spends');


# In[34]:


plt.scatter(data=df,x='MntSweetProducts',y='Total Spends');


# In[35]:


plt.scatter(data=df,x='MntFishProducts',y='Total Spends');


# In[36]:


plt.scatter(data=df,x='MntGoldProds',y='Total Spends');


# ### CHILDREN VS TOTAL SPENDS(7)

# In[37]:


sns.barplot(data=df,x='Kidhome',y='Total Spends',ci=None);


# In[38]:


sns.barplot(data=df,x='Teenhome',y='Total Spends',ci=None);


# In[39]:


df.info()


# In[40]:


df[' Income ']=df[' Income '].str.replace('$','').str.strip().str.strip("'").str.replace(',', '').astype(float)
df


# ### RECENCY VS TOTAL SPENDS (8)

# In[41]:


plt.scatter(data=df,x='Recency',y='Total Spends');


# ## INCOME VS TOTAL SPENDS (9)

# In[42]:


plt.xlim(0,175000)
plt.scatter(data=df,x=' Income ',y='Total Spends');


# In[43]:


df[' Income '].describe()


# ### COUNTRY WISE SPENDS(10)

# In[44]:


spends_countrywise=df.groupby('Country').agg({'Total Spends':['mean','median']})
spends_countrywise


# ### MARITAL STATUS VS TOTAL SPENDING (11)

# In[45]:


Marital_spending =df.groupby('Marital_Status').agg({'Total Spends':['mean','median']})
Marital_spending


# In[46]:


df.drop('sortedNumDealsPurchases',axis=1)


# In[47]:


df.info()


# ### CONVERSION OF SOME INT TO OBJECT VARIABLE

# In[48]:


df['Campaign_1']= df['AcceptedCmp1'].replace([1,0],['Yes','No'])
df1=df.drop('AcceptedCmp1',axis=1)


# In[57]:


df['Campaign_2']= df['AcceptedCmp2'].replace([1,0],['Yes','No'])
df2=df1.drop('AcceptedCmp2',axis=1)


# In[58]:


df['Campaign_3']= df['AcceptedCmp3'].replace([1,0],['Yes','No'])
df3=df2.drop('AcceptedCmp3',axis=1)


# In[59]:


df['Campaign_4']= df['AcceptedCmp4'].replace([1,0],['Yes','No'])
df4=df3.drop('AcceptedCmp4',axis=1)


# In[60]:


df['Campaign_5']= df['AcceptedCmp5'].replace([1,0],['Yes','No'])
df5=df4.drop('AcceptedCmp5',axis=1)


# In[61]:


df5.columns


# ### CAMPAIGN VS TOTAL SPENDS(12)

# In[62]:


df5.groupby('Campaign_1').agg({'Total Spends':['mean','median']})


# In[65]:


df5.info()

