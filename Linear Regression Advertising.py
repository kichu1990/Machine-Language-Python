
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy,scipy.stats
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[43]:


#Reading CSV File
adv=pd.read_csv("G:\Python Class Recordings\Dataset\Advertising.csv",index_col=0)
adv.head()
#response variable is sales
#feature variables are TV,radio,newspaper


# In[44]:


adv.info()                       


# In[6]:


adv.isnull().sum()                   #No NULL Values Present


# In[45]:


adv.describe()                     #Descriptive statistics on Data


# In[46]:


#search for multicolinearity
adv.corr()


# In[47]:


sns.heatmap(adv.corr(),annot=True,cmap="coolwarm")


# In[48]:


sns.pairplot(adv)


# In[79]:


#Building a Simple Linear Regression Model
#Splitting Data to Test and Train
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation  import train_test_split
x_train,x_test,y_train,y_test=train_test_split(adv
                        [["TV","radio"]],adv['sales']
                        ,test_size=0.3,random_state=1)


# In[80]:


linreg=LinearRegression()
linreg.fit(x_train,y_train)         #fit model on Train Data


# In[81]:


linreg.intercept_           #interceptof model


# In[82]:


linreg.coef_


# In[83]:


#final equation of line is
#2.9372157346906125+(0.04695205*TV+0.17658644*radio+0.00185115*newspaper)
#Make predcition on train Data after Building Model
pred=linreg.predict(x_train)


# In[96]:


#SSE,RMSE,MAPE on training Data
actual=np.array(y_train)
predicted=np.array(pred)
SSE=sum((actual-predicted)**2)
print(SSE)
RMSE=(SSE/len(x_train))**0.5
print(RMSE)
MAPE=sum(abs((actual-predicted)/actual))
print(MAPE)
TSS=sum((actual-np.mean(y_train))**2)
print(TSS)
R2=1-(SSE/TSS)
print(R2)


# In[85]:


#To find P values of each predictors
from statsmodels.api import add_constant
X2=add_constant(x_train)
lm=sm.OLS(y_train,X2)
lm2=lm.fit()
lm2.pvalues
print(lm2.summary())


# In[86]:


#Make prediction on test Data
pred_test=linreg.predict(x_test)
actual_test=np.array(y_test)
predicted_test=np.array(pred_test)
#SSE,RMSE,MAPE on training Data
SSE_Test=sum((actual_test-predicted_test)**2)
print(SSE_Test)
RMSE_Test=(SSE/len(x_test))**0.5
print(RMSE_Test)
MAPE_Test=sum(abs((actual_test-predicted_test)/actual_test))
print(MAPE_Test)
TSS_Test=sum((actual_test-np.mean(y_test))**2)
print(TSS_Test)
R2_Test=1-(SSE_Test/TSS_Test)
print(R2_Test)


# In[92]:


#comparing prediction with actual
test_act_pred=pd.DataFrame({'Actual':y_test,
                            'Predicted':np.round(predicted_test,2),
                            'Residual':y_test-predicted_test})
print(test_act_pred)


# In[98]:


#Measurng Model Accuracy using metrice
from sklearn import metrics
MSE_met=metrics.mean_squared_error(y_test,predicted_test)
print(MSE_met)
RMSE_met=np.sqrt(MSE)
print(RMSE_met)
R2_met=metrics.r2_score(y_test,predicted_test)
print(R2_met)

