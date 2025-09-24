# Functions: 
# A function is a block of code that performs a specific task.
# It allows us to group instructions together and reuse them whenever we needed. 
# Instead of writing the same code again and again, we just define a function once and call it whenever required. 
# Syntax:
# def function_name(parameters):
#     # function body code
#     return value # optional
# function_name()
# example:
# def greet():
#     print("Hello World1")
# greet()
# Calling a Function:
# Calling a Function means telling python to run the code inside a function by using it's name followed by paranthese().
# If the function needs input (parameter), We provide values(argument) inside the parantheses. 
# When we call a function, Python jumps to the function, excutes it's code,and then comes back to continue the program.
# def greet(): # function name 
#     print("Hello World1") # 
# greet() # calling a function. 

# Passing Parameters & Arguments. 
# Parameters: A variable declared inside the function definition. It's acts like an empty container waiting to receive a value.
# Arguments: The actual value we pass into the function when calling it. It fills the empty container(Parameter.)
# example: 
# def greet(name):
#     print("Hello",name)
# greet("Nandhan")

# Types of Functions Arguments:
# A. Positional Arguments:
# When we pass Arguments in the same order as the function parameter, they are called positional Arguments.
# here the order(position) is very important. 
#example:
# def greet(rollno,name):
#     print("Hello",name,",Your rollno is",rollno)
# greet("L6","Nandhan")
# B. Keyword Arguments: 
# When we pass values or Arguments by writing the parameter(variable = value), they are called as Keyword Arguments. 
# def greet(rollno,name):
#     print("Hello",name,",Your rollno is",rollno)
# greet(name="Nandhan",rollno="L6")
# C. Default Arguments:
# When a parameter has default value(tassigning the value in parameter) in the function definition, it becomes a default argumen. 
# def greet(rollno, name="Student"):
#     print("Hello",name,",Your rollno is",rollno)
# greet(rollno="L6") # Hello student, your no is L6
# greet(name="Nandhan",rollno="L6") # Hello Nandhan, your rollno is L6
# D. Varible-Length Arguments:
# Sometimes we don't know how many arguments will be passed to a function. 
# Python provides two special ways to handle this:
# 1. *args:(Varible-Length Arguments): 
# Collects mutliple values into a tuple. 
# def summ(*L):
#     print(sum(L))
# summ(10,20,30,40,50)
# 2. **kwargs:(Keyword Varible-Length Arguments)
# Collects multiple key=value pair into a dictionary. 
# def data(**info):
#     for key,value in info.items():
#         print(key,":",value)
# data(name="Nandhan",rollno="L6",branch="CSC")
# data(name="Anurag",rollno="L5",branch="CSC")
# data(name="Nikhil",rollno="16",branch="CSC")
# data(name="Kaveri",rollno="L6",branch="CSC")
# data(name="Susmitha",rollno="7",branch="CSC")

# Scope of the variable: 
# The scope of a variable means the part of the program where that variable can be accessed or used. 
# In python, variables can be local and global, depending on where they are created. 
# Local Variable: 
# A variable declared inside a function is called a local variable. 
# It exists only while the function is running.
# It cannot be used outside that function. 
# Global Variable: 
# A variable declared outside all function is called a global variable. 
# It can be accessed anywhere in the program(inside or outside functions). 
# example: 
# x = 10 # global 
# print("x=10 is global")
# print("x=5 is local")
# def test():
#     x = 5 # Local
#     print("Inside Function:",x)
# test()
# print("outside Function:",x) # y is not defined  
# Lambda functions
# A lambda function is a small, anonymous function in python. 
# Unlike normal functions defined using def, a lambda function does not have a name. 
# it is usually used for short,simple operations. 
# Syntax:
# lambda arguments: expression
# normal function for squaring a number
# def sqe(x):
#     print(x*x)
# sqe(5) # 25
# lambda function for squaring a number
# squ = lambda x: x*x
# print(squ(5))

# Recursive Function: 
# normal Factorail function:
# 5! = 5*4*3*2*1 = 120
# def factorial(n):
#     fact = 1 # 5
#     for i in range(n,0,-1): # 5 4 3 2 1 
#         fact = fact * i # = 5 * 4 = 120
#     print(fact) # 120
# factorial(5)
# Recursive Function: 
# Recurion is when a function calls itself to solve a part of the same problem is called recursion. 
# Two parts every recursive function needs:
# 1. Base Case: 
# the simplest input you know the answer to stop the function.
# 2. Recursive case:
# how to reduce the problem and call the same function on the smaller problem.  
def Rfactorial(n):
    if n == 0: # base case 
        return 1
    else:
        return n * Rfactorial(n-1) # recursive case.
print(Rfactorial(5))


# Higher order Functions: 
# Python provides some very powerful built-in higher order functions that makes it easier to process collections (like lists,tuple).
# the most three common ones are:
# 1. map()
# 2. filter()
# 3. reduce()

# 1. map():
# map() appllies a function to each element of a sequence (list,tuple) and return a new sequence(iterable). 
# Syntax:
# map(function, iterable)
# numbers = [1,2,3,4,5]
# squ = list(map(lambda x:x*x, numbers))
# print(squ) # [1,4,9,16,25]
# filter():
# filter() selects  elements from a sequence that satisfy a condition(True/False)
# Syntax:
# filter(function, iterator)
# numbers = [1,2,3,4,5]
# squ = list(filter(lambda x:x%2 == 0, numbers))
# print(squ) # [2,4]
# reduce():
# reduce() is in the functools module. it applies a function cumullatively to the elements of a sequence, reducing it to single value. 
# from functools import reduce
# numbers = [1,2,3,4,5]
# squ = reduce(lambda x,y:x+y, numbers)
# print(squ) # 15

# write a function to check wheather the number is even or odd. 
# def check(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# check(1)
# check(2)
# check(8)
# write a function to check wheather the number is positive, negative and zero.
# def checkn(n):
#     if n>0:
#         print("+ve") 
#     elif n<0:
#         print("-ve")
#     else:
#         print("zero")
# checkn(1)
# checkn(-2)
# checkn(0)
# Write a function to check the largest number amoung three numbers. 
