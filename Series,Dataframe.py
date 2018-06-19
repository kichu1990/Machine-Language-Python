import pandas as pd
import numpy as np
#Series in Python
#One Diemnsional Array with axis Labels
#The axis labels for the data as referred to as the index. The length of index must be the same as the length of data
#series can have multiple Datatype
label=["A","B","C","D"]
age=[23,34,56,12]
aseries=pd.Series(data=age,index=label)
print(aseries)
aseries["A"]                       #To access data using index

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

#Dataframe :collection of Array with Indexes
df=pd.DataFrame(data=age1,index=label1,columns=['column1'])
print(df)

df['column1']              #To access the columns in Dataframe -->dataframename['columname']
#OR
df.column1

df1=pd.DataFrame(data=np.array(['1','2','3','4']).reshape(2,2),columns=['column1','column2'])
print(df1)

a1=np.array([100,"John","Pune"])
a2=np.array([101,"Jack","USA"])
a3=np.array([102,"Jim","Belgium"])
df1=pd.DataFrame(data=[a1,a2,a3],columns=['ID','Name','Location'])
print(df1)

df1[["ID","Name"]]                              #To access multiple Columns

#Creating Dataframe from Dictionary
myData={'Name':['Sam','Ajay','Anand'],'Age':[23,22,34]}
df2=pd.DataFrame(data=myData)
print(df2)

# Using `iloc[]`
print(df1.iloc[0][0])

# Using `loc[]`
print(df1.loc[0]['Name'])

# Using `at[]`
print(df1.at[0,'Name'])

# Using `iat[]`
print(df1.iat[0,0])

# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series))

# Use the `shape` property Return Dimesnion of the Dataframe
print(df2.shape)

# Or use the `len()` function with the `index` property Return no of rows in Dataframe
print(len(df2.index))

data1 = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
dataf=pd.DataFrame(data=data1[1:,1:],
                  columns=data1[0,1:])
print(dataf)

# Use `iloc[]` to select a row
print(dataf.iloc[0])

# Use `loc[]` to select a column
print(dataf.loc[:,'Col2'])
