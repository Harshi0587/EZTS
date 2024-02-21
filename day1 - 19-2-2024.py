"""
#p1
a,b= map(int, input().split())
if(a>b):
    print(a, " is greater than", b)
else:
    print(b, " is greater than", a)
"""

"""
#p2
a,b,c=map(int,input().split())
z=max(a,b,c)
print(z)
"""

"""
#p2
a,b,c=map(int,input().split())
if(a>b & a>c):
    print(b)
elif(b>a & b>c):
    print(a)
else:
    print(c)
"""
    

"""
#p3
a= list(map(int,input().split()))
a.sort()
print(a[-2])
"""

"""
#p3
a,b,c= map(int,input().split())
if(a>b & a>c):
    if(b>c):
        print(b)
    else:
        print(c)
elif(b>c & b>a):
    if(c>a):
        print(c)
    else:
        print(a)
else:
    if(a>b):
        print(a)
    else:
        print(b)
"""

"""
#p3-second largest number
a,b,c= map(int,input().split())
if(a>b & a>c):
    a=0
    if(b>c):
        print(b)
    else:
        print(c)
elif(b>a & b>c):
    b=0
    if(a>c):
        print(a)
    else:
        print(c)
else:
    c=0
    if(a>b):
        print(a)
    else:
        print(b)
"""

"""
#p4-hello world
i=0
for i in range(1000):
    print("Hello World")
"""

"""
#p5-relation
a,b=map(int,input().split())
if(a>b):
    print("a > b")
elif(a<b):
    print("a < b")
else:
    print("a == b")
"""

"""
#p6-valid triangle
a,b,c= map(int, input().split())
if((a+b)>c or (b+c)>a or (a+c)>b):
    print("Yes")
else:
    print("No")
"""

"""
#how many left
a,b= map(int,input().split())
while(b>=a):
    b=b-a
print(b)
"""

"""
#number reverse
a=int(input())
s=0 
t=0
if(a>0):
    while(a!=0):
        t=a%10
        s=s*10+t
        a=a//10
    print(s)
elif(a==0):
    print(a)
else:
    a=a*-1
    while(a!=0):
        t=a%10
        s=s*10+t
        a=a//10
    print(s*-1)
"""

"""
#watermelon
w=int(input())
if(w%2==0 and w>2):
    print("Yes")
else:
    print("No")
"""

"""
#Fever-for loop
for i in range(int(input())):
    x=int(input())
    if(x>98):
        print("YES")
    else:
        print("NO")
"""

"""
#fever-while loop
t=int(input())
while(t!=0):
    x=int(input())
    if(x>98):
        print("YES")
    else:
        print("NO")
    t=t-1
"""

"""
#discount,sp=100 
for i in range(int(input())):
    x=int(input())
    print(100-x)
"""

"""
#chefzon discount
for i in range(int(input())):
    a,b,c,d= map(int,input().split())
    c=(c*a)//100
    d=(d*b)//100
    x=a-c
    y=b-d
    if(x>y):
        print("Second")
    elif(x<y):
        print("First")
    else:
        print("Any")
"""

"""
#chef and candies
for i in range(int(input())):            #t=int(input()) while(t!=0):
    n,x=map(int, input().split())
    if(n>x):
        a=n-x
        if(a%4==0):
            print(a//4)
        else:
            print((a//4)+1)
    else:
        print("0")
"""

#pizzas 
t=int(input())
while(t!=0):
    n,x=map(int,input().split())
    a=n*x
    if(a%4==0):
        print(a//4)
    else:
        print((a//4)+1)
















