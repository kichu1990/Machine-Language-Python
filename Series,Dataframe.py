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
df1[["ID","Name"]]         #To access multiple Columns
#OR
df.column1

df1=pd.DataFrame(data=np.array(['1','2','3','4']).reshape(2,2),columns=['column1','column2'])
print(df1)

a1=np.array([100,"John","Pune"])
a2=np.array([101,"Jack","USA"])
a3=np.array([102,"Jim","Belgium"])
df1=pd.DataFrame(data=[a1,a2,a3],columns=['ID','Name','Location'])
print(df1)


# Check out the DataFrame `df`
print(df)

# Drop the index at position 1
print(df.drop(df.index[1]))

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

#.loc[] works on labels of your index.
#.iloc[] works on the positions in your index.

# Use `iloc[]` to select a row
print(dataf.iloc[0])

# Use `loc[]` to select a column
print(dataf.loc[:,'Col2'])

#To make Index part of the Dataframe
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

# Use `.index`
df['D'] = df.index

# Print `df`
print(df)

#Append column to Dataframe
df.loc[:,'D'] = pd.Series([10,11,12],index=df.index)
df['E'] = df.index

# Print `df`
print(df)

##use one of your columns and make it your index.
dataf.set_index('Col2')

#Resetting the Index of Your DataFrame
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2.5, 12.6, 4.8], columns=[48, 49, 50])
print(df)
df_reset = df.reset_index(level=0, drop=True)
print(df_reset)

#Deleting an Index from Your DataFrame
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), 
                  index= [2.5, 12.6, 4.8, 4.8, 2.5], 
                  columns=[48, 49, 50])
df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2, 'A', 4], columns=[48, 49, 50])
print(df)

# Drop the column with label 50                 
df.drop(50, axis=1, inplace=True)      #inplace=True means t will override original Datafarme
#or
del df[50] 

#subsetting based on condition
df[(df[50]>6)]                         #Return all the rows where column 50 greater than 6

# Drop the column at position 1
df.drop(df.columns[[1]], axis=1)

#The axis argument is either 0 when it indicates rows and 1 when it is used to drop columns.
#set inplace to True to delete the column without having to reassign the DataFrame.

# Drop  method() using the index 
print(df.drop(df.index[1]))

#remove duplicate rows from your DataFrame by executing df.drop_duplicates(). You can also remove rows from your DataFrame, taking 
#into account only the duplicate values that exist in one column.

df=pd.DataFrame(data=np.array([[1,2,3,4],[4,5,6,5],[7,8,9,6],[23,50,60,7],[23,35,37,23]]),index=[2.5,12.6,4.8,4.8,2.5],
                columns=[48,49,50,50])

df.drop_duplicates([48], keep='last')

#drop() method, use the index property to specify the index of which rows you want to remove from your DataFrame:
# Drop the index at position 1
print(df.drop(df.index[1]))

#Rename the Index or Columns of a  DataFrame
df=pd.DataFrame(data=np.array([[1,2,3,4],[4,5,6,5],[7,8,9,6],[23,50,60,7],[23,35,37,23]]),
                columns=[48,49,50,51])

newcols = {
    48: 'new_column_1', 
    49: 'new_column_2', 
    50: 'new_column_3',
    51: 'new_column_4'
}

df.rename(columns=newcols, inplace=True)
df.rename(index={1: 'a'})                   #rename Index 1 to 'a'

products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],
                        'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                        'testscore': [4, 3, 5, 7, 5, 8]})
pivot_products = products.pivot(index='category', columns='store', values='price')
