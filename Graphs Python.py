#To install Package
pip install seaborn  #To be Done in command prompt

#Importing Package
import seaborn as sns
tips=sns.load_dataset('tips')
tips.tail()                                  #To see last 5 Rows

tips.shape                                   #To see Dimension
tips.head()                                  #To see first 5 rows
tips.head(10)                                #To see specified number of rows
tips[(tips['sex']=='Male')].shape            #To see number of male
tips[(tips['sex']=='Female')].shape          #To see number of female
tips[(tips['sex']=='Female')].count() 
sum(tips['sex']=='Female')
tips['sex'].value_counts()                                  #Similar to table function in R but one variable at a time
tips[(tips['sex']=='Female')&(tips['smoker']=='Yes')].shape #No of Female who are smokers

import pandas as pd
pd.crosstab(tips['sex'],tips['smoker'])
tips[(tips['tip']>5)].shape                                 #No of people who gave tip more than 5$
tips[tips['tip']>5]['tip']
tips.describe()                                             #only Display the statistics for continuous variable 
tips.info()                                                 #Display DataType.Nulls in variable

#Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips.columns                                                #To see all columns in Dataframe

#scatter plot :between two continuous variables
plt.plot(tips['total_bill'],tips['tip'],'bo')
plt.xlabel("Total Bill in $")
plt.ylabel("Tip in $")
plt.title("Bill vs Tip in $")

#histogram
plt.hist(tips['total_bill'],bins=40)
plt.xlabel("Total Bill in $")
plt.ylabel("Frequency")
plt.title("Histogram of Total Bill in $")

#boxplot
plt.boxplot(tips['total_bill'],showfliers=True)

#Distribution plot or Distplot same as Histogram

