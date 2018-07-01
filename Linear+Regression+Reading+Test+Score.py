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

#Filling missing value
pisa2009train['male'].fillna(train['male'].mode()[0], inplace=True)
pisa2009train['raceeth'].fillna(train['raceeth'].mode()[0], inplace=True)
pisa2009train['preschool'].fillna(train['preschool'].mode()[0], inplace=True)
pisa2009train['expectBachelors'].fillna(train['expectBachelors'].mode()[0], inplace=True)
pisa2009train['motherHS'].fillna(train['motherHS'].mode()[0], inplace=True)
pisa2009train['motherBachelors'].fillna(train['motherBachelors'].mode()[0], inplace=True)
pisa2009train['motherWork'].fillna(train['motherWork'].mode()[0], inplace=True)
pisa2009train['fatherHS'].fillna(train['fatherHS'].mode()[0], inplace=True)
pisa2009train['fatherBachelors'].fillna(train['fatherBachelors'].mode()[0], inplace=True)
pisa2009train['englishAtHome'].fillna(train['englishAtHome'].mode()[0], inplace=True)
pisa2009train['computerForSchoolwork'].fillna(train['computerForSchoolwork'].mode()[0], inplace=True)
pisa2009train['read30MinsADay'].fillna(train['read30MinsADay'].mode()[0], inplace=True)
pisa2009train['schoolHasLibrary'].fillna(train['schoolHasLibrary'].mode()[0], inplace=True)
pisa2009train['publicSchool'].fillna(train['publicSchool'].mode()[0], inplace=True)
pisa2009train['urban'].fillna(train['urban'].mode()[0], inplace=True)
pisa2009train['fatherWork'].fillna(train['fatherWork'].mode()[0], inplace=True)
pisa2009train['selfBornUS'].fillna(train['selfBornUS'].mode()[0], inplace=True)
pisa2009train['motherBornUS'].fillna(train['motherBornUS'].mode()[0], inplace=True)
pisa2009train['fatherBornUS'].fillna(train['fatherBornUS'].mode()[0], inplace=True)
