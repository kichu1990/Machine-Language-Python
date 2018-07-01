
# coding: utf-8

# In[5]:


get_ipython().magic('pwd #To see Current working Directory')


# In[10]:


get_ipython().magic('cd "D:\\\\Study  Materials\\\\R Language\\\\DataSet"                         #To change working Directory')


# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy,scipy.stats
import seaborn as sns
get_ipython().magic('matplotlib inline')

#Read CSV Files
pisa2009test=pd.read_csv("pisa2009test.csv")
pisa2009train=pd.read_csv("pisa2009train.csv")

#Merge the Data for EDA
pisa=pd.concat([pisa2009test,pisa2009train],axis=0)


# In[14]:


#Find NaN in the Data
pisa.info()
pisa.isnull().sum()


# In[15]:


pisa.describe()   


# In[16]:


sns.distplot(pisa['readingScore'])


# In[17]:


pisa.head()


# In[88]:


#Creating Categorical Variable
pisa["male"] = pisa["male"].astype('category')
pisa["raceeth"] = pisa["raceeth"].astype('category')
pisa["preschool"] = pisa["preschool"].astype('category')
pisa["expectBachelors"] = pisa["expectBachelors"].astype('category')
pisa["motherHS"] = pisa["motherHS"].astype('category')
pisa["motherBachelors"] = pisa["motherBachelors"].astype('category')
pisa["motherWork"] = pisa["motherWork"].astype('category')
pisa["fatherHS"] = pisa["motherWork"].astype('category')
pisa["fatherBachelors"] = pisa["fatherBachelors"].astype('category')
pisa["englishAtHome"] = pisa["englishAtHome"].astype('category')
pisa["computerForSchoolwork"] = pisa["computerForSchoolwork"].astype('category')
pisa["read30MinsADay"] = pisa["read30MinsADay"].astype('category')
pisa["schoolHasLibrary"] = pisa["schoolHasLibrary"].astype('category')
pisa["publicSchool"] = pisa["publicSchool"].astype('category')
pisa["urban"] = pisa["urban"].astype('category')
pisa["fatherWork"] = pisa["fatherWork"].astype('category')
pisa["selfBornUS"] = pisa["selfBornUS"].astype('category')
pisa["motherBornUS"] = pisa["motherBornUS"].astype('category')
pisa["fatherBornUS"] = pisa["fatherBornUS"].astype('category')


# In[18]:


#filling missing value
pisa['male'].fillna(value=1,inplace=True)
pisa['raceeth'].fillna(value='White',inplace=True)
pisa['preschool'].fillna(value=1,inplace=True)
pisa['expectBachelors'].fillna(value=1,inplace=True)
pisa["motherHS"].fillna(value=1,inplace=True)
pisa["motherBachelors"].fillna(value=0,inplace=True)
pisa["motherWork"].fillna(value=1,inplace=True)
pisa["fatherHS"].fillna(value=1,inplace=True)
pisa["fatherBachelors"].fillna(value=0,inplace=True)
pisa["englishAtHome"].fillna(value=1,inplace=True)
pisa["computerForSchoolwork"].fillna(value=1,inplace=True)
pisa["read30MinsADay"].fillna(value=0,inplace=True)
pisa["schoolHasLibrary"].fillna(value=1,inplace=True)
pisa["publicSchool"].fillna(value=1,inplace=True)
pisa["urban"].fillna(value=0,inplace=True)
pisa["fatherWork"].fillna(value=1,inplace=True)
pisa["selfBornUS"].fillna(value=1,inplace=True)
pisa["motherBornUS"].fillna(value=1,inplace=True)
pisa["fatherBornUS"].fillna(value=1,inplace=True)


# In[19]:


pisa.isnull().sum()


# In[23]:


plt.boxplot(pisa['minutesPerWeekEnglish'],showfliers=True)

