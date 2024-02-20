"""
#watching movie 
for i in range(int(input())):
    x,y=map(int,input().split())
    a=y//2
    print((x-y)+a)
"""

"""
#movie 
def movie(x,y):
    print((x-y)+(y//2))
def testcases():
    t=int(input())
    while(t!=0):
        t=t-1
        x,y=map(int,input().split())
        movie(x,y)
testcases()
"""

"""
#number of occurences of 4
for i in range(int(input())):
    x=int(input())
    count=0
    while(x!=0):
        t=x%10
        if t==4:
            count=count+1
        x=x//10
        
    print(count)
"""

"""
#number of occurences of '4'
def count(x,c):
    while(x!=0):
        t=x%10
        if t==4:
            c=c+1
        x=x//10
    return c
def testcases():
    t=int(input())
    while(t!=0):
        t=t-1
        x=int(input())
        print(count(x,0))
testcases()    
"""

#append three
for i in range(int(input())):
    n=int(input())
    a=n
    c=0
    while n!=0:
        n=n//10
        c=c+1
    x=3*(10**c)+a
    x=(x*10)+3
    print(x)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



