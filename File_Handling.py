file = open("students.txt","r") # read, readline, readlines 
for line in file:
    print(line)
print("Data is changed")
file.close() 

with open("students.txt","r") as file1:
    for line in file1:
        print(line)
    print("Data is changed")