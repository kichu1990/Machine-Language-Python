
# coding: utf-8

# In[24]:


get_ipython().magic('cd "D:\\\\Study  Materials\\\\R Language\\\\DataSet"')


# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy,scipy.stats
import seaborn as sns


# In[26]:


#Read CSV Files
pisa2009test=pd.read_csv("pisa2009test.csv")
pisa2009train=pd.read_csv("pisa2009train.csv")


# In[27]:


#Merge the Data for EDA
pisa=pd.concat([pisa2009test,pisa2009train],axis=0)


# In[28]:


pisa['male'].fillna(pisa['male'].mode()[0], inplace=True)
pisa['raceeth'].fillna(pisa['raceeth'].mode()[0], inplace=True)
pisa['preschool'].fillna(pisa['preschool'].mode()[0], inplace=True)
pisa['expectBachelors'].fillna(pisa['expectBachelors'].mode()[0], inplace=True)
pisa['motherHS'].fillna(pisa['motherHS'].mode()[0], inplace=True)
pisa['motherBachelors'].fillna(pisa['motherBachelors'].mode()[0], inplace=True)
pisa['motherWork'].fillna(pisa['motherWork'].mode()[0], inplace=True)
pisa['fatherHS'].fillna(pisa['fatherHS'].mode()[0], inplace=True)
pisa['fatherBachelors'].fillna(pisa['fatherBachelors'].mode()[0], inplace=True)
pisa['englishAtHome'].fillna(pisa['englishAtHome'].mode()[0], inplace=True)
pisa['computerForSchoolwork'].fillna(pisa['computerForSchoolwork'].mode()[0], inplace=True)
pisa['read30MinsADay'].fillna(pisa['read30MinsADay'].mode()[0], inplace=True)
pisa['schoolHasLibrary'].fillna(pisa['schoolHasLibrary'].mode()[0], inplace=True)
pisa['publicSchool'].fillna(pisa['publicSchool'].mode()[0], inplace=True)
pisa['urban'].fillna(pisa['urban'].mode()[0], inplace=True)
pisa['fatherWork'].fillna(pisa['fatherWork'].mode()[0], inplace=True)
pisa['selfBornUS'].fillna(pisa['selfBornUS'].mode()[0], inplace=True)
pisa['motherBornUS'].fillna(pisa['motherBornUS'].mode()[0], inplace=True)
pisa['fatherBornUS'].fillna(pisa['fatherBornUS'].mode()[0], inplace=True)


# In[30]:


df=pisa.dropna()


# In[34]:


plt.hist(df['schoolSize'], normed=True, bins=30)


# In[35]:


plt.hist(df['studentsInEnglish'], normed=True, bins=30)


# In[37]:


pisa['schoolSize'].fillna(pisa['schoolSize'].median(), inplace=True)
pisa['studentsInEnglish'].fillna(pisa['studentsInEnglish'].median(), inplace=True)
pisa['minutesPerWeekEnglish'].fillna(pisa['minutesPerWeekEnglish'].median(), inplace=True)


# In[47]:


get_ipython().magic('matplotlib inline')
pisa['minutesPerWeekEnglish'].plot.box()


# In[48]:


pisa['schoolSize'].plot.box()


# In[49]:


pisa['studentsInEnglish'].plot.box()


# In[91]:


pisa.describe()  


# In[41]:


q75_studentsInEnglish, q25_studentsInEnglish = np.percentile(pisa.studentsInEnglish.dropna(), [75 ,25])
iqr_studentsInEnglish = q75_studentsInEnglish - q25_studentsInEnglish
 
min_studentsInEnglish = q25_studentsInEnglish - (iqr_studentsInEnglish*1.5)
max_studentsInEnglish = q75_studentsInEnglish + (iqr_studentsInEnglish*1.5)


# In[43]:


q75_minutesPerWeekEnglish, q25_minutesPerWeekEnglish = np.percentile(pisa.minutesPerWeekEnglish.dropna(), [75 ,25])
iqr_minutesPerWeekEnglish = q75_minutesPerWeekEnglish - q25_minutesPerWeekEnglish
 
min_minutesPerWeekEnglish = q25_minutesPerWeekEnglish - (iqr_minutesPerWeekEnglish*1.5)
max_minutesPerWeekEnglish = q75_minutesPerWeekEnglish + (iqr_minutesPerWeekEnglish*1.5)


# In[44]:


q75_schoolSize, q25_schoolSize = np.percentile(pisa.schoolSize.dropna(), [75 ,25])
iqr_schoolSize = q75_schoolSize- q25_schoolSize
 
min_schoolSize = q25_schoolSize - (iqr_schoolSize*1.5)
max_schoolSize = q75_schoolSize + (iqr_schoolSize*1.5)


# In[45]:


pisa['studentsInEnglish'] = np.where(pisa.studentsInEnglish > (q75_studentsInEnglish + (iqr_studentsInEnglish*1.5)), q75_studentsInEnglish + (iqr_studentsInEnglish*1.5), pisa.studentsInEnglish)
pisa['studentsInEnglish'] = np.where(pisa.studentsInEnglish < (q25_studentsInEnglish - (iqr_studentsInEnglish*1.5)), q25_studentsInEnglish - (iqr_studentsInEnglish*1.5), pisa.studentsInEnglish)


# In[46]:


pisa['minutesPerWeekEnglish'] = np.where(pisa.minutesPerWeekEnglish > (q75_minutesPerWeekEnglish + (iqr_minutesPerWeekEnglish*1.5)), q75_minutesPerWeekEnglish + (iqr_minutesPerWeekEnglish*1.5), pisa.minutesPerWeekEnglish)
pisa['minutesPerWeekEnglish'] = np.where(pisa.minutesPerWeekEnglish < (q25_minutesPerWeekEnglish - (iqr_minutesPerWeekEnglish*1.5)), q25_minutesPerWeekEnglish - (iqr_minutesPerWeekEnglish*1.5), pisa.minutesPerWeekEnglish)


# In[50]:


#Find correlation between the  numerical variable
pisa.corr()


# In[59]:


#Convert string to Dummy Variable
dummy_va1=pd.get_dummies(pisa['raceeth'],drop_first=True)
pisa_new=pd.concat([pisa,dummy_va1],axis=1)


# In[61]:


pisa_new2=pisa_new.drop(['raceeth'],axis=1)


# In[65]:


pisa_new2.head()


# In[66]:


#Building a Simple Linear Regression Model
#Splitting Data to Test and Train
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation  import train_test_split
x_train,x_test,y_train,y_test=train_test_split(pisa
                        [["grade","male","preschool","expectBachelors","motherHS","motherBachelors",
                         "motherWork","fatherHS","fatherBachelors","fatherWork","englishAtHome","computerForSchoolwork",
                          "read30MinsADay","minutesPerWeekEnglish","studentsInEnglish","schoolHasLibrary",
                          "publicSchool","urban","schoolSize","readingScore"]],pisa['readingScore']
                        ,test_size=0.3,random_state=1)


# In[67]:


linreg=LinearRegression()
linreg.fit(x_train,y_train)         #fit model on Train Data


# In[68]:


print(linreg.intercept_)


# In[69]:


print(linreg.coef_)


# In[72]:


#Make Prediction
pred=linreg.predict(x_test)


# In[79]:


#Get P value for each predictor
from statsmodels.api import add_constant
X2=add_constant(x_train)
lm=sm.OLS(y_train,X2)
lm2=lm.fit()
lm2.pvalues


# In[82]:


print(lm2.summary())


# In[84]:


plt.hist(pisa_new2['readingScore'], normed=True, bins=30)


# In[86]:


x_train,x_test,y_train,y_test=train_test_split(pisa
                        [["grade","male","preschool","motherHS",
                        "fatherHS","fatherBachelors","fatherWork","englishAtHome","computerForSchoolwork",
                          "read30MinsADay","minutesPerWeekEnglish"
                          ,"urban","schoolSize","readingScore"]],pisa['readingScore']
                        ,test_size=0.3,random_state=1)


# In[89]:


linreg2=LinearRegression()
linreg2.fit(x_train,y_train)    


# In[91]:


#Make Prediction
pred2=linreg2.predict(x_test)


# In[99]:


print(pred2,y_test)


# In[107]:


from sklearn import metrics
from sklearn.metrics import r2_score
print(r2_score(y_test,pred2))
print(metrics.mean_absolute_error(y_test,pred2))

