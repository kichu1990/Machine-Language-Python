
# coding: utf-8

# In[1]:


#To install Package
pip install seaborn  #To be Done in command prompt


# In[2]:


import seaborn as sns


# In[5]:


tips=sns.load_dataset('tips')
tips.tail()     #To see last 5 Rows


# In[7]:


tips.shape        #To see Dimension


# In[8]:


tips.head()     #To see first 5 rows


# In[9]:


tips.head(10) #To see specified number of rows


# In[21]:


tips[(tips['sex']=='Male')].shape            #To see number of male
tips[(tips['sex']=='Female')].shape          #To see number of female
tips[(tips['sex']=='Female')].count() 
sum(tips['sex']=='Female')


# In[24]:


tips['sex'].value_counts() #Similar to table function in R but one variable at a time


# In[26]:


tips[(tips['sex']=='Female')&(tips['smoker']=='Yes')].shape #No of Female who are smokers


# In[28]:


import pandas as pd


# In[29]:


pd.crosstab(tips['sex'],tips['smoker'])


# In[30]:


tips[(tips['tip']>5)].shape    #No of people who gave tip more than 5$


# In[36]:


tips[tips['tip']>5]['tip']


# In[37]:


tips.describe()            #only Display the statistics for continuous variable 


# In[40]:


tips.info()             #Display DataType.Nulls in variable


# In[1]:


#Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[41]:


get_ipython().magic('matplotlib inline')


# In[47]:


tips.columns      #To see all columns in Dataframe
#scatter plot :between two continuous variables
plt.plot(tips['total_bill'],tips['tip'],'bo')
plt.xlabel("Total Bill in $")
plt.ylabel("Tip in $")
plt.title("Bill vs Tip in $")


# In[52]:


#histogram
plt.hist(tips['total_bill'],bins=40)
plt.xlabel("Total Bill in $")
plt.ylabel("Frequency")
plt.title("Histogram of Total Bill in $")


# In[59]:


#boxplot
plt.boxplot(tips['total_bill'],showfliers=True)


# In[ ]:


#Distribution plot or Distplot same as Histogram

