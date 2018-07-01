get_ipython().magic('pwd #To see Current working Directory')
get_ipython().magic('cd "D:\\\\Study  Materials\\\\R Language\\\\DataSet"                         #To change working Directory')

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

pisa.describe()   
pisa.head()

#Find NaN in the Data
pisa.info()
pisa.isnull().sum()

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
