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

#Filling missing value for categorical Variable
pisa2009train['male'].fillna(pisa2009train['male'].mode()[0], inplace=True)
pisa2009train['raceeth'].fillna(pisa2009train['raceeth'].mode()[0], inplace=True)
pisa2009train['preschool'].fillna(pisa2009train['preschool'].mode()[0], inplace=True)
pisa2009train['expectBachelors'].fillna(pisa2009train['expectBachelors'].mode()[0], inplace=True)
pisa2009train['motherHS'].fillna(pisa2009train['motherHS'].mode()[0], inplace=True)
pisa2009train['motherBachelors'].fillna(pisa2009train['motherBachelors'].mode()[0], inplace=True)
pisa2009train['motherWork'].fillna(pisa2009train['motherWork'].mode()[0], inplace=True)
pisa2009train['fatherHS'].fillna(pisa2009train['fatherHS'].mode()[0], inplace=True)
pisa2009train['fatherBachelors'].fillna(pisa2009train['fatherBachelors'].mode()[0], inplace=True)
pisa2009train['englishAtHome'].fillna(pisa2009train['englishAtHome'].mode()[0], inplace=True)
pisa2009train['computerForSchoolwork'].fillna(pisa2009train['computerForSchoolwork'].mode()[0], inplace=True)
pisa2009train['read30MinsADay'].fillna(pisa2009train['read30MinsADay'].mode()[0], inplace=True)
pisa2009train['schoolHasLibrary'].fillna(pisa2009train['schoolHasLibrary'].mode()[0], inplace=True)
pisa2009train['publicSchool'].fillna(pisa2009train['publicSchool'].mode()[0], inplace=True)
pisa2009train['urban'].fillna(pisa2009train['urban'].mode()[0], inplace=True)
pisa2009train['fatherWork'].fillna(pisa2009train['fatherWork'].mode()[0], inplace=True)
pisa2009train['selfBornUS'].fillna(pisa2009train['selfBornUS'].mode()[0], inplace=True)
pisa2009train['motherBornUS'].fillna(pisa2009train['motherBornUS'].mode()[0], inplace=True)
pisa2009train['fatherBornUS'].fillna(pisa2009train['fatherBornUS'].mode()[0], inplace=True)

df=pisa2009train.dropna()

#Plot Histogram for Variables
sns.distplot(df['minutesPerWeekEnglish']);
sns.distplot(df['schoolSize']);
sns.distplot(df['studentsInEnglish']);

#Check the Outlier
df['minutesPerWeekEnglish'].plot.box()
df['studentsInEnglish'].plot.box()
df['schoolSize'].plot.box()

#Filling missing value for Continouous variable minutesPerWeekEnglish,studentsInEnglish, schoolSize               
#As it is a numerical variable, we can use mean or median to impute the missing values. We will use median to fill the null values 
#as earlier we saw that loan amount have outliers so the mean will not be the proper approach as it is highly affected by the 
#presence of outliers.
pisa2009train['schoolSize'].fillna(pisa2009train['schoolSize'].median(), inplace=True)
pisa2009train['studentsInEnglish'].fillna(pisa2009train['studentsInEnglish'].median(), inplace=True)
pisa2009train['minutesPerWeekEnglish'].fillna(pisa2009train['minutesPerWeekEnglish'].median(), inplace=True)



