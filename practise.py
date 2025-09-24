# #Area of circle 
# r = float(input("Enter r value: "))
# AOC = 3.14*r**2
# print(AOC)
# #Area of Triangle
# h = float(input("Enter Height: "))
# b = float(input("Enter Base: "))
# AOT = 1/2*h*b
# print(AOT)
# #Simple Intrests 
# #(p*r*t)/100
# # f -> c (f = (c*9/5)+32)
# #km -*> m
# #m -> km
# #m -> cm 
# #cm -> m
# #km -> Mlies
# m = int(input("Enter the meters: "))
# km = m*1000
# print(km)
# km = int(input("Enter the kilometers: "))
# m = km/1000
# print(m)
# cm = int(input("Enter the centimeters: "))
# m1 = cm * 100
# print(m1)
# m2 = int(input("Enter the meters: "))
# cm = m2 / 100
# print(cm)
#check whether Even or odd
# number = int(input("Enter your Number: "))
# if number%2==0: 
#     print("the number Even")
# else:
#     print("The number is odd")
#leap 
# year = int(input("Enter your year: "))
# if (year%4==0 and year%100!=0) or year%400 == 0:
#     print("Leap")
# else:
#     print("not leap ")

# Check the number whether it is positive, negative, zero 

num = int(input("Enter num value: "))
if num > 0:
    print("positive")
elif num < 0: 
    print("Negative")
elif num == 0:
    print("zero")