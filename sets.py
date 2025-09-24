# Sets:
# Set is a collection datatype which is used to stored mutliple values in a single varaible.
# Sets are unordered, unindexed, mutable, and they do not allow duplicate values. 
# They are useful when you want to store unique elements and performs the mathematical operationsl like union, intersection, and difference. 
# Syntax:
# My_set = {element1,element2,element3}
# Characteristics of Sets: 
# Unordered:
#example: {1,2,3} and {3,2,1} are considered the same set. 
# unindexed: You cannot access set elements by the index like lists or tuples. set[1]
# a = {1,2,3}
# print(a[1]) 
# Unique values only: Duplicate values are automatically removed from the set
a = {1,2,3,3,2,1,1,1,2}
print(a)  # output {1,2,3}

# Creating a set:
s1 = {1,2,3}
s2 = {10,12.5,"Hello",True}
# Empty set:
s31 = {}
s3 = set()
print(type(s3)) # set

# Accessing sets:
# We cannot directly access an element using index but we access an element using loops. 
A = {"Rajinikant","Snake king","Upendra"}
for role in A:
    print(role)
# Adding an element in sets:
S = {12,18,20}
S.add(25) # adds only single element in any position 
S.update([34,29]) # adds the mutliple values in the set
print(S) # {12,18,20,25,34,29,25}
# Deleting the elemets in set:
# remove(): Removes the element, but it gives an error if the value is not found in the set 
# S = {12,18,20,25,34,29,25}
# S.remove(26) 
# print(S) # Keyvalue error
# discard(): Removes the element, but it gives no error if the value is not found in the set
S = {12,18,20,25,34,29,25}
S.discard(26) 
print(S) # {12,18,20,34,29}
# pop(): Removes the random element from the set. 
S = {12,18,20,25,34,29,25}
S.pop() 
print(S)
# clear(): Removes the every element from the set.
S = {12,18,20,25,34,29,25}
S.clear() 
print(S)

# Mathematical Operations in set: Δ
# Union "U"="|": Prints all unique values or elements from the both sets. 
A = {1,2,3}
B = {4,5,6}
print(A | B) # {1,2,3,4,5,6}
# Intersection "∩" = "&" : Prints the common elements from the set
A = {1,2,3,4}
B = {3,4,5,6}
print(A & B) # {3,4}
# Difference "-" = "-": removes the common elements from the lists but prints only the first sets values. 
A = {1,2,3,4} 
B = {3,4,5,6}
print(A - B) # {1,2} 
print(B - A) # {5,6} 
# Symmetric difference "Δ" = "^": 
# removes the common elements from the lists but prints only the first sets values.
A = {1,2,3,4} 
B = {3,4,5,6}
print(A ^ B) # {1,2,5,6} 

# Mathematical operations using functions: 
A = {1,2,3,4} 
B = {3,4,5,6}
# Union
print(A.union(B)) # {1,2,3,4,5,6}
# Intersection
print(A.intersection(B)) # {3,4}
# Difference
print(A.difference(B)) # {1,2}
# Symmetric difference
print(A.symmetric_difference(B)) # {1,2,5,6}
# len():
S = {10,15,82,96,22}
print(len(S)) # 5 
# max():
S = {10,15,82,96,22}
print(max(S)) # 96
# min():
S = {10,15,82,96,22}
print(min(S)) # 10
# sum():
S = {10,15,82,96,22}
S.sum()
print(S) # 225