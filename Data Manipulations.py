
# coding: utf-8

# In[1]:


#Missing Values
import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.array([[1, 2, np.NaN], [4, np.NaN, np.NaN], [7, 5, 9]]),
                  columns=['A', 'B', 'C'])


# In[12]:


print(df)


# In[7]:


#Missing value are represented as NaN
#Delete NaN :we have to delete either row or column another option is to replace NaN
df.dropna()   #Delete Row Having NaN because by Default axis is 0


# In[10]:


df.dropna(axis=1) #Delete column having NaN


# In[13]:


df.dropna(thresh=2,axis=0)  #Delete Row having 2 NaN


# In[16]:


#Filling NaN
df.fillna(value='MV')  #NaN will get replaced with 'MV'
df.fillna(value=2)     #NaN replaced with 2


# In[20]:


#filling missing value with Mean
df['B'].fillna(value=df['A'].mean(),inplace=True)


# In[26]:


print(df)


# In[25]:


#Finding count of NaN in each column
df.isnull().sum()


# In[27]:


#when summing Data NaN will be treated as Zero
df.sum()


# In[30]:


#Concatenating Two Dataframes
df = pd.DataFrame(data=np.array([['A0','A1','A2','A3'], ['B0','B1','B2','B3'], ['C0','C1','C2','C3']
                                ,['D0','D1','D2','D3']]),columns=['A', 'B', 'C','D'])

df2 = pd.DataFrame(data=np.array([['A0','A1','A5','A3'], ['B10','B1','B2','B3'], ['C6','C1','C2','C3']
                                ,['D0','D1','D2','D8']]),columns=['A', 'B', 'C','D'])
print(df)


# In[31]:


print(df2)


# In[32]:


pd.concat([df,df2],axis=0)


# In[2]:


#Mergeing Dataframe

df = pd.DataFrame(data=np.array([['100','Ram',31,'PM'], ['101','Sam',35,'DM'], 
                                 ['102','Jim',55,'CEO'], ['103','karl',45,'CF0']
                                ]),columns=['ID', 'Name', 'Age','Job'])

df2 = pd.DataFrame(data=np.array([['100',100000], ['101',500000], 
                                 ['102',10000000],['109',500000]
                                ]),columns=['ID','Salary'])


# In[4]:


pd.merge(df,df2,how="inner",on='ID') #by Default inner join will be performed if we won't specify "How".


# In[5]:


pd.merge(df,df2,how="left",on='ID')


# In[6]:


pd.merge(df,df2,how="right",on='ID') #if we have multiple keys to be joined then on=['Key1','Key2']


# In[7]:


#To get unique value in a column
df['ID'].unique()


# In[8]:


#To get no of unique value in a column
df['ID'].nunique()


# In[10]:


#Counter
from collections import Counter
Counter(df['ID'])


# In[14]:


#Data Input and Output
df=pd.read_csv("G:\Python Class Recordings\Dataset\Advertising.csv")                         #To Read CSV file
df.to_csv("G:\Python Class Recordings\Dataset\AdvertisingfromPython.csv",index=False)        #write to CSV file
lemonade=pd.read_excel("D:\Study  Materials\R Language\Lemonade.xlsx",sheetname='Sheet2')    #To Read Excel file
#write to Excel file
lemonade.to_excel("G:\Python Class Recordings\Dataset\lemonadefromPython.xlsx",sheet_name='Sheet1',index=False)


# In[26]:


#to read HTML file
#conda install lxml
#conda install html5lib
#conda install BeautifulSoup4
#read_html read will read table from a webpage and return list of dataframe Objects
Banklist=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


# In[30]:


#Group By :Allows us to group rows of Data together and call aggregate functions
grp={'Company':['google','google','facebook','tesla','Microsoft'],
       'Person':['Sam','Charlie','Joe','Dave','Mark'],
       'Sales':[200,150,450,457,895]}
dfgrp=pd.DataFrame(grp)
print(dfgrp)


# In[36]:


dfgrp.groupby(['Company'])['Sales'].mean()

