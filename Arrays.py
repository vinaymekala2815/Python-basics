# Arrays in Python:
# An Array is collection of elements of the same datatype stored in a continuous memory location. 
# Arrays are used to store mutliple values in a single variable. 
# Why Arrays?
# Easy to manage multiple values. 
# Allows Faster operations like searching and sorting. 
# Useful in mathematica and scientific problems. 
# Saves Memory. 
# Array VS Lists:
# Importing the array module. 
import array as arr

# Creating an array:

Numbers = arr.array('i',[1,2,3,4,5])
#                        0 1 2 3 4
print(type(Numbers))
print(Numbers)
# i = integer
# f = float
# u = String 

# Accessing Array Elements. 
print(Numbers[0]) # 1
print(Numbers[3]) # 4
print(Numbers[-1]) # 5

# Addind An element in array:
# append():
Numbers.append(7)
print(Numbers)
# insert():
Numbers.insert(2,6)
print(Numbers)
# extend():
Numbers.extend([8,9])
print(Numbers)

# Deleting an element:
# remove():
Numbers.remove(7)
print(Numbers)
# pop(): 
Numbers.pop(3)
print(Numbers)
# clear():
Numbers.clear()
print(Numbers)

# Updating an Element: 
Numbers[0] = 10
print(Numbers) # [10, 2, 6, 3, 4, 5, 7, 8, 9]

# Looping through Arrays: 
for i in Numbers:
    print(i)
# Basic Operations on Arrays:  
# len():
# max():
# min():

# sum():

