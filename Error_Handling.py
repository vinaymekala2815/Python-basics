# Types of Exceptions:
# 1.ZeroDivisionError
# 2.ValueError => if the variable given is in int and if we given the value has str then it is called as value
# 3.TypeError
# 4.NameError
# 5.IndexError
# 6.KeyError
# 7.FileNotFoundError

# To handle an error we use try,except.
# 1.ZeroDivisionError:
# try:
#     nume = int(input("Enter the Numerator: "))
#     demo = int(input("Enter the denominator: "))
#     divi = nume/demo
#     print(divi)
# except ZeroDivisionError: 
#     print("error")
#     print("Invalid")
# 2.ValueError => if the variable given is in int and if we given the value has str then it is called as value
# try:
#     a = int(input("Enter a value: "))
#     print(a)
# except ValueError:
#     print("Error: invalid datatype given for the output")
# 3.TypeError: 
# try:
#     a = [10,20,30] # 0 1 2
#     b = 5
#     print(a+b)
# except TypeError:
#     print("Error: invalid types to perform an operation.")
# 4.NameError
# try:
#     a = [10,20,30] # 0 1 2
#     b = 5
#     print(c)
# except NameError:
#     print("Error: invalid types to perform an operation.")
# 5.IndexError
# try:
#     a = [10,20,30] # 0 1 2
#     print(a[5])
# except IndexError:
#     print("Error: invalid types to perform an operation.")
# 6.KeyError
# try:
#     d = {"name":"Nandhan","rollNo":"L6"}
#     print(d["age"])
# except KeyError:
#     print("Error: invalid types to perform an operation.")
# 7.FileNotFoundError
# try: 
#     file = open("details.txt","r")
#     print(file.read())
# except FileNotFoundError:
#     print("given file is not created in folder")
# finally:
#     print("Program is excuted")
try:
    nume = int(input("Enter the Numerator: "))
    demo = int(input("Enter the denominator: "))
    divi = nume/demo
    print(divi)
except ValueError:
    print("error")
except ZeroDivisionError: 
    print("error")
    print("Invalid")