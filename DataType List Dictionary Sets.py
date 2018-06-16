
# coding: utf-8

# In[4]:


#List : Collection of numeric,strings or list itself,similar to Vector in R but it can hold multiple Datatype.Denoted by [].
#Vector in R can have only one DataType.Elements in List is accessed using Index.Index in Python start from Zero.


# In[9]:


x=[1,"python",2,3]


# In[ ]:


#Accessing List Element


# In[10]:


x[1]


# In[11]:


#Nested List : List inside List


# In[13]:


x=[1,2,["python",4]]


# In[14]:


x[2]


# In[15]:


x[2][1]


# In[17]:


#find length of List


# In[18]:


len(x)


# In[19]:


#To print series of Element from List.


# In[20]:


x=[1,2,3,4,5]


# In[21]:


x[0:3]          


# In[22]:


#Negative Indexing: Return the Last Element,In x[-1] delete the first Element.
x[-1]


# In[23]:


x=[1,5,"R",["Python",[1,9],"Data"],3]


# In[24]:


x[3][1][1]  #Access the Element 9


# In[26]:


# To add New element to List use append function


# In[27]:


x.append(10)


# In[28]:


x


# In[29]:


x.append(["Data Science"])


# In[30]:


x


# In[31]:


#Dictionaries in Python Unordered Collection of Item,give by {}.Have key:value pair key represent the address
#so it will be a single item.


# In[32]:


x={1:100,2:201,3:301,4:506}


# In[33]:


x


# In[34]:


print(x)


# In[36]:


y={"emp#1":"Raj","emp#2":"Ramesh","emp#3":"vijay","emp#4":"XY"}


# In[38]:


y


# In[39]:


my_dict={"name":"john",1:[2,4,3]}


# In[40]:


y.keys()     # Access all the keys


# In[41]:


len(y)       #length of Dictionary


# In[42]:


y.values()   #Access the values


# In[45]:


print(y['emp#1'])   # Indexing do not work in Dictionary


# In[46]:


#Updating value using it key in Dictionary
y['emp#1']="Rahul"


# In[47]:


print(y)


# In[48]:


#Deleting Items
del y['emp#1']


# In[49]:


print(y)


# In[50]:


#To remove all entries in Dictionary,leave empty Dictionary
y.clear()


# In[51]:


print(y)


# In[53]:


#To Delete the Dictionary
del y


# In[55]:


#Duplicate Keys
y={"emp#1":"Raj","emp#2":"Ramesh","emp#1":"vijay","emp#4":"XY"}


# In[56]:


print(y)


# In[57]:


# we cannot give duplicate keys because the values will be overwritten.
#Keys must be immutable.we cannot use list or Dictionary as Keys.


# In[58]:


#To add new Element to Dioctionary
y["emp#5"]="jose"


# In[59]:


print(y)


# In[61]:


#Iteration through Dictionary
for i in y:
    print(y[i])


# In[63]:


# To get sorted list of keys
print(sorted(y))


# In[5]:


#Tuples are immutable Objects.Immutable means values cannot be changed once initialized


# In[34]:


x=(1,2,3)


# In[35]:


x[1]


# In[37]:


x[1]=5        #statement gives an error since Tuple are immutable.


# In[15]:


#type() function return the DataType of variable
type(x)


# In[16]:


#Sets defined using {},collection of multpile Datatype but will have always unique Element.


# In[17]:


x={1,1,2}


# In[18]:


print(x)


# In[20]:


y={1,3,5,(3,5),9}


# In[21]:


print(y)


# In[22]:


#Making Set froma List


# In[23]:


z=set([1,2,3,2])


# In[24]:


print(z)


# In[27]:


#Add Element to set
y.add(10)


# In[28]:


print(y)


# In[29]:


#To discard an Element from a set
y.discard(10)


# In[30]:


print(y)


# In[31]:


#To Remove and Element from set
y.remove(9)


# In[32]:


print(y)

