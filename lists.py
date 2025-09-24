#Collection Data Types 
# These collection Data Types is also called as non-primitive data types
# These collection Data Types are used to store mutliple values in a single variable. 
# Types of CDT:
# 1. lists 
# 2. Tuples
# 3. sets
# 4. Dictionary 
# Lists in python
# Lists are collection data types which are used to store mutliple values in a variable 
# Lists are Ordered( the items have a fixed position ) and mutable (we can change, add or remove  items from the list). 
#  
# example 0 1  2  3   4 ... n-1 
# list1 = [10,20,30,40,50] #integer values
# fruits = ["apple","banana","mamgo"] #Strings values
# list2 = [10.1,20.2,30.3,40.4,50.5] #float values
# list3 = [True,False,True,True] #Boolean values
# list4 = [10,20.5,"hello",True,"False"] #Mutli datatype values. 
#output 
# print(list4)
#Accessing Elements: 
#Accessing Elements are used to retrive the list items or values stored at a position (index- indexs are starts from zero)
#index - In python, every element in a list is stored with a position number called as index 
#example:0  1  2  3   4 ... n-1 
# list1 = [10,20,30,40,50] 
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# #by negative values 
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])
#slicing in lists
# Slicing is taking out of a part from the main list. 
#slicing will extracts the part or sublist using [start idx : end idx]
#example: 
# slc1 = ["Prabhas","Balayya","PSPK","BOB","Bhai"]
# print(slc1[:3]) # 
# print(slc1[1:4]) #
# print(slc1[-3:])
#Adding Elements in list:
#We can add new values to a list in different ways: 
# 1. Append: Adds a single value at the end of the list. 
# kalkiCast = ["Prabhas","Kamal h","Amitha Bhachan","Deepika P","SSR"] 
# print(kalkiCast)
# kalkiCast.append("Deesha patani")
# print(kalkiCast)
# 2.Insert: Adds a single value at the perticular position using index
# kalkiCast.insert(2,"Vijay D")
# print(kalkiCast)
# 3.Extending : Adds mutliple values at once by combining the lists
# kalkiCast.extend(["Anudeep","Mrunal T","bujji"])
# print(kalkiCast)
# example: Add bhramanandham, after the Deepika p
# kalkiCast = ["Prabhas","Kamal h","Amitha Bhachan","Deepika P","SSR"] 
# kalkiCast.append("Deesha patani")
# kalkiCast.insert(2,"Vijay D")
# kalkiCast.extend(["Anudeep","Mrunal T","bujji"])
# print(kalkiCast)
# output = ['Prabhas', 'Kamal h', 'Amitha Bhachan', 'Deepika P', 'SSR', 'Deesha patani','Vijay D', 'Anudeep', 'Mrunal T', 'bujji']
# kalkiCast.insert(5,"bhramanandham")
# print(kalkiCast)
#Removing Elements in list
#Removes the items in the list in different ways 
# 1. remove(): Removes or deletes the first occurrence of the specific items 
# kalkiCast.remove("Mrunal T")
# print(kalkiCast)
# # 2. pop(): deletes the items from list at the perticular position 
# kalkiCast.pop(6)
# print(kalkiCast)
# # 3. clear(): Deletes the all items from the list
# kalkiCast.clear()
# print(kalkiCast) 
# kalkiCast[1] = "Sandeep R V"
# print(kalkiCast) 
# Changing the Elements: Lists are mutable, We can change the values after creating the lists using index
# kalkiCast[1] = "Sandeep R V"
# print(kalkiCast) 
# Mathematical Operations in lists
# 1. Concatenation: jions the two lists together in one list 
# a = [1,2]
# b = [3,4]
# c = a+b
# print(c)
# 2. Repetition: Repeats the elements of a lisr mutliple times 
# a = [1,2]
# n = int(input("Enter the n value:"))
# b = a * n
# print(b)
# Searching and Checking:
# We can check if an elements or values exists in a list or not:
# in operator: 
# It is a membership operator, which returns the Trues values if the elements exists in the lists.
# a = [2,4,6,8,8,8,10,12,14]
# if 2 in a:
#     print("Yes item is present in the list ")
# not in operator:
# It is a membership operator, which returns the Trues values if the elements is not exists in the list.
# print(3 not in a)
# index(): Which gives the position of the first occurrence of an element or value. 
# print(a.index(8)) #3
# count(): Which gives the number of elements in the lists. 
# a = [2,4,6,8,8,8,10,12,14]
# cnt = 0
# print(a.count(8))
# for i in range(10):
#     if i == 8:
#         cnt = cnt + 1 
# print(cnt)

# Sorting: sort()
# It arranges elements either in ascending order (small to large) or descending order (large to small).
# Reversing: reverse():
# It Flips the list so the last element will becomes the first element. 
# st = [25,12,5,31,list13,18,7,45,8,55,68]
# st.reverse() # 68,55,8,45,7,18,13,31,5,12,25
# st.sort()
# print(st) # AO = 5,7,8,12,13,18,25,31,45,55,68
# st.reverse()
# print(st) # DO = 68,55,45,31,25,18,13,12,8,7,5
# st1 = [25,8,4,7,10] # 25,10,8,7,4
# st1.sort(reverse=True)

#1 5 4 2 3 
#R = 3 2 4 5 1 # Ao = 1 2 3 4 5
# Ao = 1 2 3 4 5 

# Copying the list:
# copying creates a new list with the same elements, so chsnges in the new list do not affect the orginal list.  
# Frd1 = ["A","C","D","A","D","B","B","C","C","A","A"]
# Frd2 = Frd1.copy()
# Frd2[2] = "B"
# print(Frd2)

# #Built-in Functions with loops: 
# # Python Programming provides many ready-made functions to work with the items 
# st = [25,12,5,31,13,18,7,45,8,55,68]
# st.sort()
# # len(): Returns the number of elements. 
# print(len(st)) #11
# # max(): Returns the maximum element from the list.
# print(max(st)) #68
# # min(): Returns the Minimum element from the list.
# print(min(st)) #5 
# # sum(): Returns the total sum of all numeric elements.
# print(sum(st)) # 287
# a = "hello world to the python programming"
# b = a.split()
# print(b)
# Multipli values using input data to the list : 
# a = list(map(int, input("enter the mutliple values:").split())) # 10 20 30 40 50 

# print(a) #[10,20,30,40,50] #integer values

# b = input("enter the mutliple values:").split() # 10 20 30 40 50
# print(b) #['10','20','30','40','50'] #string values 

#Traversing a List:
# Accessing the elements using a loop
#using for loop 
# cars = ["thar","jaguer","Audi","bmw"]
# # index   0       1        2      3
# for car in range(0,4):
#     print("cars=",car)

# # Using index with for loop:
# a = len(cars) #4
# for i in range(0,a):
#     print("cars",i,cars[i])

# Adding elements using for loop: 
# list1 = []
# n = int(input("enter the number of list values: "))
# for i in range(0,n): # i 0 1 
#     a = input("Enter the list values: ")
#     list1.append(a)
# print(list1)
#give the input values to the lists from 1 to 10
# list1 = []
# n = int(input("enter the number of list values: ")) # 10
# for i in range(n): # i 0 1 2 3 4 5 6 7 8 9 10 
#     list1.append(i)
# print(list1)

# sum of list items = 10 20 30 40 50 without using sum(). 

# list1 =[10,20,30,40,50]
# sum = 0 # 100 
# for i in list1: # 10 20 30 40 50
#     sum = sum + i # 150
# print(sum)
# #Convert ["p","y","t","h","o","n"] to python
# list1 =["p","y","t","h","o","n"]
# word = "" 
# for i in list1: # y t h o n
#     word = word + i 
# print(word)

# Find the Maximum and minimum number from list without using max() and min(). 
# list1 = [52,7,18,12,31,45,17,10,23,229,227] # Max = 229 # Min = 7
# list1.sort()
# # [7, 10, 12, 17, 18, 23, 31, 45, 227, 229]
# #  0   1   2   3   4   5   6   7   8     9
# print(list1)
# print("Maximum of list :",list1[9])
# print("Manimum of list :",list1[0])
# Find the Maximum and minimum number from list without using max(),min(), sort().
# list1 = [52,7,18,12,31,45,17,10,23,229,227] 
# max1 = list1[0] # 229
# min1 = list1[0] # 7
# for num in list1: # [52,7,18,12,31,45,17,10,23,229,227]
#     if num > max1: 
#         max1 = num
#     if num < min1: 
#         min1 = num

# print(max1)
# print(min1)
# Searching for an element in a List 
# Names = ["Mallareddy sir","Revanth reddy sir","Modi","Rahul gandhi"]
# Searching_name = input("enter the name to be found: ") # modi # kcr
# found = False
# for i in Names:
#     if Searching_name == i:
#         found = True
# if found:
#     print("Yes")
# else:
#     print("No")

# Count even and odd numbers 
# numbers = [7, 10, 12, 17, 18, 23, 31, 45, 227, 229]
# # o = 7
# # e = 3
# evn_cnt = 0 #2
# odd_cnt = 0 #1
# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         evn_cnt += 1
#     else:
#         odd_cnt += 1
# print("Number of even numbers are: ",evn_cnt)
# print("Number of odd numbers are: ",odd_cnt)

# Reversing a list without reverse
# list1 = [7, 10, 12, 17, 18, 23, 31, 45, 227, 229] # l = 10
# #ind  =  0   1   2   3   4   5   6   7   8    9
# l = len(list1)
# r_list = []
# for i in range(l-1,-1,-1):
#     r_list.appe,nd(list1[i])
# print(r_list)

# Removing all negative numbers using loop # = (2,30,45,23,72,7)
# numbers = [-56,-9,2,-8,-30,30,45,23,-19,72,-55,-18,7,0]
# postive_list = []
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         postive_list.append(numbers[i])
# print(postive_list)

# Multiply each element in the list
numbers = [56,92,8,30,30,45,23,19,72,55,18,7,0]
m = int(input("Enter the number to be mutliplied: "))
After_mutliplication = []
for i in numbers:
    After_mutliplication.append(i*m)
print(After_mutliplication)
