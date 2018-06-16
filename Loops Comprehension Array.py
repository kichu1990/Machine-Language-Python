#For Loop
x=[1,2,3,4]
for i in x:
    print(i)

#while loop
i=1
while i<11:
    print(i)
    i=i+1

#if elif Loop
if i<4:
    print("i less than 4")
elif i>4:
    print("i greater tha 4")
else:
    print("i is equal to 4")

#Range
for i in range(5):
    print(i)

for i in range(3,9,2):
    print(i)

#Break and Continue
#Break will come out of all the Loop,continue will come out of current Loop
count=0
while True:
    print(count)
    count+=1
    if count>5:
       break

for i in range(10):
    print(i)
    if  i%2==0:
        continue
    print

#comprehension in Python : for loop in not efficent since it iterate through one record at a time.
#Comprehension are written in square Bracket
x=[1,2,3,4,5]
[i*2 for i in x]

#split function
x="I love Python for Data Science"
x=x.split()

stuff=[[i.upper(),i.lower(),len(i)] for i in x]

for i in stuff:
    print(i)

#Create pythagorean triples using Comprehension
[(x,y,z) for x in range(1,30) for y in range(1,30) for z in range(1,30) if x**2+y**2==z**2]

#To find intersection of two list
x=[2,3,5,6]
y=[2,9,6]
[i for i in x if i in y]
[i for i in x if i not in y]

#numpy Array contain Mathematical functions.
#pandas library contain function for Data Manipulations
#matplotlib and seaborn for Visualization
#sklearn for Machine learning
#Array numpy Array formally called as ndarray,conatin element fo same type
import numpy as np
x=[1,2,3]
xx=np.array(x)
type(xx)

x=['A',1,2,3,4]
xx=np.array(x)
type(xx)
print(xx)

x=np.array(range(20))
print(x)

#reshape function IN Array used to convert 1D Array to 2D Array
y=x.reshape(5,4)
print(y)

#Accessing Elements from an Array.Arrayname[rowno,colno],rowno and colno start from zero.
print(y[0,3])
print(y[1,2:])
print(y[0,:3])
print(y[y>5])  #Return Array Elements
print(y>5)     #Return a Boolean Array

#To find Max of value in Array0
y.max()

[y[0,i] for i in[0,2]]
y[0,[0,2]]

#rand(x) Return x random Number between 0 and 1 from a uniform Distribution
np.random.rand(10)

#rand(x) Return x random Number b from a Normal Distribution with mean=0 and sd=1
np.random.randn(10)

#linespace(start,stop,N) #N is the evenly spaced points between start and stop
x=np.linspace(1,20,6)
print(x)

a=[1,2,3]
b=[4,5,6]
print(a+b)                          #Elements are appeneded at the end
print(np.array(a)+np.array(b))      #Add teh corrosponding Difference

#Difference between Array and List
#Same DataType ,Multiuple DataType
#Difficult to add Element,Easy to add using append function
#numpy array support vectorised operations whereas list do not
