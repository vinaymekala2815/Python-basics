# Arithmetic Operators
a = 10 
b = 3 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#Comparison or Relational Operator
x = 5 
y = 8 
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical Operator 
#and
p = 5
q = 10
print(p>2 and q>5)
print(p>2 and q<5)
print(p<2 and q>5)
print(p<2 and q<5)
#or
p1 = 5
q1 = 10
print(p1>2 or q1>5)
print(p1>2 or q1<5)
print(p1<2 or q1>5)
print(p1<2 or q1<5)
#not 
p2 = 5 
q2 = 0 
print(not(p2))
print(not(q2))
#Assignment operotor 
a1 = 10
a1 += 1
print(a1)
a1 -= 1
print(a1)
a1 *= 2
print(a1)
a1 /= 2
print(a1)
a1 //= 2
print(a1)
a1 %= 2
print(a1)
a1 **= 2
print(a1)
#Bitwise operator 
x1 = 5
y1 = 3 
print(x1 & y1)
print(x1 | y1)
print(~x1)
print(x1 ^ y1)
print(x1 << y1)
print(x1 >> y1)
#identity Operator
x = [1,2,3,4]
y = x 
z = [1,2,3,4]
print(x is y) #True 
print(x is z) # False
print(x is not z)#True  
print(x is not y) #False
# #membership Operator 
text = [1,2,3,4]
print(4 in text) #T
print(5 in text) #F
print(4 not in text) #F
print(5 not in text) #T