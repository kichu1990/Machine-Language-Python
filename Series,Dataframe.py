
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
#Series in Python
#One Diemnsional Array with axis Labels
#The axis labels for the data as referred to as the index. The length of index must be the same as the length of data
#series can have multiple Datatype
label=["A","B","C","D"]
age=[23,34,56,12]
aseries=pd.Series(data=age,index=label)


# In[5]:


aseries


# In[7]:


aseries["A"]                       #To access data using index


# In[21]:


label1=["A","B","C","D"]
age1=[23,34,56,"D"]
aseries1=pd.Series(data=age1,index=label1)
print(aseries1)
arage1=np.array(age1)   #Moment we convert age1 to Array it convert 23,34,56 to string becuase Array can 
                        #hold only single DataType
alabel1=np.array(label1) 
print(arage1)
aseries2=pd.Series(data=age1,index=label1)
print(aseries2)


# In[23]:


#Dataframe :collection of Array with Indexes
df=pd.DataFrame(data=age1,index=label1,columns=['column1'])
df


# In[26]:


df['column1']              #To access the columns in Dataframe -->dataframename['columname']
#OR
df.column1


# In[28]:


df1=pd.DataFrame(data=np.array(['1','2','3','4']).reshape(2,2),columns=['column1','column2'])


# In[29]:


df1


# In[35]:


a1=np.array([100,"John","Pune"])
a2=np.array([101,"Jack","USA"])
a3=np.array([102,"Jim","Belgium"])
df1=pd.DataFrame(data=[a1,a2,a3],columns=['ID','Name','Location'])


# In[36]:


print(df1)


# In[38]:


df1[["ID","Name"]]                              #To access multiple Columns


# In[53]:


#Creating Dataframe from Dictionary
myData={'Name':['Sam','Ajay','Anand'],'Age':[23,22,34]}
df2=pd.DataFrame(data=myData)
print(df2)


# In[61]:


# Using `iloc[]`
print(df1.iloc[0][0])

# Using `loc[]`
print(df1.loc[0]['Name'])

# Using `at[]`
print(df1.at[0,'Name'])

# Using `iat[]`
print(df1.iat[0,0])


# In[62]:


# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

# Take a dictionary as input to your DataFrame 
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series))


# In[64]:


# Use the `shape` property Return Dimesnion of the Dataframe
print(df2.shape)

# Or use the `len()` function with the `index` property Return no of rows in Dataframe
print(len(df2.index))

