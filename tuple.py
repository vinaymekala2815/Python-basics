#Tuple is a Collection datatype, Which is used to store the multiple values in a single variable. 
# Tuple is a ordered, Immutable, Also allows the duplicate values, and can store mixed data types in values. 

# example :
coordinates = ("x","y")
My_tuple = (10,20,30)
print(My_tuple)
print(type(My_tuple))

# Creating a Tuple:
# Empty tuple
Et = ()
# tuple with numbers:
N = (1,2,3,4,5,6)
#Tuple with Strings:
S = ("A","B","C","a","b","c")
# Tuple with mixed datatypes 
M = (24,3.14,"A","c",True,"False")
# Tuple with single element:
a = 10 # Int
print(type(a)) 
b = [10] # List
print(type(b))
c = (10,) # Tuple 
print(type(c))

# Accessing Elements: 
# Tuple uses index values to access an element. 
A = (10,20,30,40)
#i    0  1  2  3
#-i  -4 -3 -2 -1
print(A[0]) # 10 
print(A[1]) # 20
print(A[2]) # 30
print(A[3]) # 40
print(A[-1]) # 40 
print(A[-2]) # 30
print(A[-3]) # 20
print(A[-4]) # 10

# Slicing the tuple:
# Extracts part of the tuple using start index and end index 
# ([start index: end index])
# In tuple it will print before the end index value.
A = (10,20,30,40)
#i    0  1  2  3
#-i  -4 -3 -2 -1
print(A[1:3]) # 20 30 
print(A[:2]) # 10 20 
print(A[-3 :-1]) # 20 30

# Changing the Values: 
# Tuples are immutable, So we cannot change the values. 
A[1] = 50
print(A) #TypeError: 'tuple' object does not support item assignment
# append():
A.append(50)
print(A)

# Length: 
# max:
# min:
# sum: 
# Concatination 
# Repetation 

# Searching and Checking: 
# in operator:
# not in operator:
# index():
# count():
# sorting and Reversing: 
#Iterating tuple using for loop:

# Nested Tuple:
T = (10,(20,30),(40,50))
#i    0    1       2
print(T[2][1])