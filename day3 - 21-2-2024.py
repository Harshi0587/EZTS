"""
#finding duplicate element in an array
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]==l[j]) :
            x=l[i]
            break
print(x)
"""

"""
#duplicate using slicing technique
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if(l[i] in l[i+1:]):
        print(l[i])
        break
"""

"""
#duplicate using sort method
n=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(n):
    if(l[i]==l[i+1]):
        a=l[i]
        break
print(a)
"""

"""
#duplicate using count
n=int(input())
l=list(map(int,input().split()))
for i in l:
    x=l.count(i)
    if(x>1):
        print(i)
        break
"""

"""
#unique using count
n=int(input())
l=list(map(int,input().split()))
for i in l:
    x=l.count(i)
    if(x==1):
        print(i)
"""

"""
#unique using for loop
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]!=l[j]) :
            print(l[i])
            break
"""

"""
#unique using slicing technique
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if(l[i] not in l[i+1:]):
        print(l[i])
"""

"""
#unique using membership
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if(l[i] not in l[i+1:] and l[i] not in l[:i]):
        print(l[i])
"""    

"""
#gravity switch
n=int(input())
l=list(map(int,input().split()))
print(l.sort())
"""

"""
#chef cooking team
n=int(input())
t=[]
for i in range(1,n+1):
    if(n%i==0):
        t.append(i)
a=0
b=0
print(t)
for i in t:
    if(i%2==0):
        a=a+1
    else:
        b=b+1
if(a==b):
    print("Yes")
else:
    print("No")
"""

"""
#chef cooking team using recursive function
def factors(n,t):
    for i in range(1,n+1):
        if(n%i==0):
            t.append(i)
    a=0
    b=0
    print(t)
    for i in t:
        if(i%2==0):
            a=a+1
        else:
            b=b+1
    if(a==b):    #can also take len(a), len(b)
        print("Yes")
    else:
        print("No")
def testcases():
    t1=int(input())
    while(t1!=0):
        n=int(input())
        t=[]
        factors(n,t)
        t1=t1-1
testcases()
"""

"""
#cost of groceries
for i in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=0
    for j in range(len(a)):
        if a[j]>=x:
            cost=cost+b[j]
    print(cost)
"""    

"""
#prime or not
n=int(input())
for i in range(2,n+1):
    if(n%i==0):
        print("Not Prime")
        break
    else:
        print("Prime")
        break  
"""

"""
#prime using count
n=int(input())
for i in range(2,n):
    c=0
    if(n%i==0):
        c=c+1
    if(c>=1):
        print("Not Prime")
        break
    else:
        print("Prime")
        break     
"""

"""
#prime using list
n=int(input())
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l)
if(len(l)==2):
    print("Prime")
else:    
    print("Not Prime")
"""

"""
#alice and bob running
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=0
b1=0
for i in range(n):
    if(a[i]<=2*b[i]):
        a1=a1+1
    if(b[i]<=2*a[i]):
        b1=b1+1
if(a1==b1):
    print(a1)
else:
    print(0)
"""

"""
#alice and bob using zip function
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i,j in zip(a,b):
    if i<=2*j and j<=2*i:
        c=c+1
print(c)
"""

"""
#square
n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i**2)
print(l)
"""

"""
#even square
n=int(input())
l=[]
for i in range(1,n+1):
    if(i%2==0):
        l.append(i**2)
print(l)
"""

"""
#even square using for loop
n=int(input())
for i in range(2,n+1,2):
    print(i*i,end=" ")       #here end tells us to print in the same line
"""

"""
#perfect numbers(wrong program)
n=int(input())
l=[]
for i in range(1,n):
    c=0
    if(n%i==0):
        c=c+1
        l.append(i)
    if(c==n):
        print(n)
print(l)
"""

"""
#correct program for perfect numbers 
n=int(input())
for i in range(2,n+1,2):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
"""


























