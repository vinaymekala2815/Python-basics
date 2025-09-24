# Dictionary:
# Dictionary is a in-built datatype, which is used to store multipl values in a single varaible.
# Dictionary stores the data in the form of key-values pairs.
# Each key is unique and works as an index to access its corresponding value.
# Keys are immutable(can't be changed once created), while values can be anything(mutable).
# Dictionary are: Ordered(From python 3.7+ version), Mutable, Do not allows the duplicate keys 
# Syntax: 
# My_dict = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(My_dict)
# Characteristics of Dictionary:
# key-value pairs: 
# Every entry of Dictionary's element is a pair: keys and values. 
# { "name":"nandhan"}
# Unique Keys: 
# example: 
# A = {"n":"Nandhan","n":"Anurag"}
# print(A) # "n1":"Anurag"
# Keys must be immutable: 
# keys can be(valid keys): integer,float,string
# My_dict = {
#     1:"value1",
#     10.2:"value2",
#     "key3":"value3",
#     "key4":"value4"
# }

# Creating Dictionary:
# Normal Dictionary:
# BioData = {
#     "Name":"Nandhan",
#     "Roll.No":"5L6",
#     "Branch": "CSE AI&ML",
#     "Place":"Kamareddy"
# }
# Dictionary using Constructor:
# BioData1 = dict( Name="Nandhan", Roll_No="5L6",Branch="CSE AI&ML", Place="Kamareddy")
# Empty Dictionary:
# E_D = {}

# Accessing the Dictionary:
# -> To access an element we use key names inside the square brackets [] or we can use get() method.
# Example: 
# BioData = {
#     "Name":"Anurag",
#     "Roll.No":"5L6",
#     "Branch": "CSE AI&ML",
#     "Place":"Kamareddy"
# }
# square brackets []
# print(BioData["Name"]) # Anurag
# print(BioData["Roll.No"]) # 5L6
# print(BioData["Branch"]) # CSE AI&ML
# print(BioData["Place"]) # Kamareddy
# print(BioData["age"]) # keyerror(because the "age" is not created in dictionary)
 
# using get() method:
# print(BioData.get("Name")) # Anurag
# print(BioData.get("Roll.No")) # 5L6
# print(BioData.get("Branch")) # CSE AI&ML
# print(BioData.get("Place")) # Kamareddy
# print(BioData.get("age")) # None instead of error 

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pari into a dictionary.
# Updating: You can update or change the values using exsisted keys in the dictionary. 
# BioData = {
#     "Name":"Anurag",
#     "Roll.No":"5L6",
#     "Branch": "CSE AI&ML",
#     "Place":"Kamareddy"
# }
# BioData["age"] = 24 #adding the new key and values
# print(BioData)
# BioData["Place"] = "Hyderabad" # changing or updating the exsisted key's value.
# print(BioData)

# Removing in Dictionary:
# Python gives mutliple ways to delete items from a dictionary. 
# pop(),popitem(),clear(), del(delete)
# BioData = {
#     "Name":"SaiRam",
#     "Roll.No":"F9",
#     "Branch": "CSE AI&ML",
#     "Place":"charminar",
#     "Role":"charminar_model"
# }
# pop(): Removes the key value
# BioData.pop("Roll.No")
# print(BioData)
# popitem(): Removes the Last inserted item from the dictionary. 
# BioData.popitem()
# print(BioData)
# del(delete): Deletes the keys from dictionary. 
# del BioData["Branch"]
# print(BioData)
# clear(): Removes every item from the dictionary. 
# BioData.clear()
# print(BioData)

# Dictionary methods:
# Methods allow you to access dictionary data easily. 
# keys(),values(), items()
BioData = {
    "Name":"SaiRam",
    "Roll.No":"F9",
    "Branch": "CSE AI&ML",
    "Place":"charminar",
    "Role":"Software Developer"
}
# keys(): It prints only the keys of dictionary
print(BioData.keys())
# values(): It prints only the values of dictionary
print(BioData.values())
# items(): It prints both the keys and values of dictionary
print(BioData.items())

# updating update(): update the mutliple values 
BioData.update({"Role":"Web Developer","Place":"Hyderabad"})
print(BioData)

#Loops for Dictionary:

# Loops using lists 
L = [10.10,20,30,40,50]
for i in L:
    print(i)
BioData = {
    "Name":"SaiRam",
    "Roll.No":"F9",
    "Branch": "CSE AI&ML",
    "Place":"charminar",
    "Role":"Software Developer"
}
# Loops to iterate the keys(dy default the Dictionary's will stores the keys value.):
for i in BioData:
    print(i)
# Loops to iterate the keys using keys() method:
for i in BioData.keys():
    print(i)
# Loops to iterate the values using values() method:
for i in BioData.values():
    print(i)
# Loops to iterate the items using items() method:
for i in BioData.items():
    print(i)

# Nested Tuple:
T = (10,(20,30),(40,50))
#i    0    1       2
print(T[2][1])

# Nested Dictionary
Students = {
    "S1":{"Name":"Nandhan", "RollNO":"L6"},
    "S2":{"Name":"Anurag", "RollNO":"L7"},
    "S3":{"Name":"Mani", "RollNO":"L8"}
}
print(Students["S1"]["Name"]) # Nandhan
print(Students["S2"]["Name"]) # Anurag
print(Students["S3"]["Name"]) # Mani
print(Students["S1"]["RollNO"]) # L6
print(Students["S2"]["RollNO"]) # L7
print(Students["S3"]["RollNO"]) # L8
