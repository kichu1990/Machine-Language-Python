#List : Collection of numeric,strings or list itself,similar to Vector in R but it can hold multiple Datatype.Denoted by [].
#Vector in R can have only one DataType.Elements in List is accessed using Index.Index in Python start from Zero.

x=[1,"python",2,3]

#Accessing List Element
x[1]

#Nested List : List inside List
x=[1,2,["python",4]]
x[2]
x[2][1]

#find length of List
len(x)

#To print series of Element from List.
x=[1,2,3,4,5]
x[0:3]          

#Negative Indexing: Return the Last Element,In x[-1] delete the first Element.
x[-1]

x=[1,5,"R",["Python",[1,9],"Data"],3]
x[3][1][1]  #Access the Element 9

# To add New element to List use append function
x.append(10)
print(x)

x.append(["Data Science"])
print(x)

#Dictionaries in Python Unordered Collection of Item,give by {}.Have key:value pair key represent the address
#so it will be a single item.
x={1:100,2:201,3:301,4:506}
print(x)

y={"emp#1":"Raj","emp#2":"Ramesh","emp#3":"vijay","emp#4":"XY"}
print(y)

my_dict={"name":"john",1:[2,4,3]}
y.keys()     # Access all the keys
len(y)       #length of Dictionary
y.values()   #Access the values

print(y['emp#1'])   # Indexing do not work in Dictionary

#Updating value using it key in Dictionary
y['emp#1']="Rahul"
print(y)

#Deleting Items
del y['emp#1']
print(y)

#To remove all entries in Dictionary,leave empty Dictionary
y.clear()
print(y)

#To Delete the Dictionary
del y

#Duplicate Keys
y={"emp#1":"Raj","emp#2":"Ramesh","emp#1":"vijay","emp#4":"XY"}
print(y)

# we cannot give duplicate keys because the values will be overwritten.Keys must be immutable.we cannot use list or Dictionary as Keys.

#To add new Element to Dioctionary
y["emp#5"]="jose"
print(y)

#Iteration through Dictionary
for i in y:
    print(y[i])

# To get sorted list of keys
print(sorted(y))

#Tuples are immutable Objects.Immutable means values cannot be changed once initialized
x=(1,2,3)
x[1]
x[1]=5        #statement gives an error since Tuple are immutable.

#type() function return the DataType of variable
type(x)

#Sets defined using {},collection of multpile Datatype but will have always unique Element.
x={1,1,2}
print(x)

y={1,3,5,(3,5),9}
print(y)

#Making Set froma List
z=set([1,2,3,2])
print(z)

#Add Element to set
y.add(10)
print(y)

#To discard an Element from a set
y.discard(10)
print(y)

#To Remove and Element from set
y.remove(9)
print(y)
