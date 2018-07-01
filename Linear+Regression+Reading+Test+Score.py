%pwd                                                                           #To see Working Directory   
%cd "D:\\Study  Materials\\R Language\\DataSet"                                #To change working Directory

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy,scipy.stats
import seaborn as sns

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
pisa['motherBornUS'].fillna(pisa['motherBornUS'].mode()[0], inplace=Tru
pisa['fatherBornUS'].fillna(pisa['fatherBornUS'].mode()[0], inplace=True)

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

q75_studentsInEnglish, q25_studentsInEnglish = np.percentile(pisa.studentsInEnglish.dropna(), [75 ,25])
iqr_studentsInEnglish = q75_studentsInEnglish - q25_studentsInEnglish
min_studentsInEnglish = q25_studentsInEnglish - (iqr*1.5)
max_studentsInEnglish = q75_studentsInEnglish + (iqr*1.5)

q75_minutesPerWeekEnglish, q25_minutesPerWeekEnglish = np.percentile(pisa.minutesPerWeekEnglish.dropna(), [75 ,25])
iqr_minutesPerWeekEnglish = q75_minutesPerWeekEnglish - q25_minutesPerWeekEnglish
min_minutesPerWeekEnglish = q25_minutesPerWeekEnglish - (iqr*1.5)
max_minutesPerWeekEnglish = q75_minutesPerWeekEnglish + (iqr*1.5)
                            
q75_schoolSize, q25_schoolSize = np.percentile(pisa.schoolSize.dropna(), [75 ,25])
iqr_schoolSize = q75_schoolSize- q25_schoolSize 
min_schoolSize = q25_schoolSize - (iqr*1.5)
max_schoolSize = q75_schoolSize + (iqr*1.5)
                            
pisa['studentsInEnglish'] = np.where(pisa.studentsInEnglish > max_studentsInEnglish, max_studentsInEnglish, pisa.studentsInEnglish)
pisa['studentsInEnglish'] = np.where(pisa.studentsInEnglish < min_studentsInEnglish, min_studentsInEnglish, pisa.studentsInEnglish) 
                            

pisa['minutesPerWeekEnglish'] = np.where(pisa.minutesPerWeekEnglish > max_minutesPerWeekEnglish, max_minutesPerWeekEnglish, 
                                         pisa.minutesPerWeekEnglish)
pisa['minutesPerWeekEnglish'] = np.where(pisa.minutesPerWeekEnglish < min_minutesPerWeekEnglish, min_minutesPerWeekEnglish, 
                                         pisa.minutesPerWeekEnglish)                              
