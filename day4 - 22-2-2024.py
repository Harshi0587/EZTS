"""
#pangrams using sets
s=set(input()) 
print(len(s))
print(s)
print(type(s))
abc={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
print(abc)
c=0
for i in abc:
    for j in s:
        if i==j:
            c=c+1
if(c>=26):
    print("Pangram")
else:
    print("Not Pangram")
"""

"""
#pangrams using sets - using length
s=input()
s1=set(s)
if(len(s1)>=26):
    print("Pangram")
else:
    print("Not Pangram")


"""

"""(wrong)  #dict cannot be compared with dict.
abc={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
d1=dict.fromkeys(abc,0)
d2=sorted(d1)
s=set(input())
s1=dict.fromkeys(s,0)
s2=sorted(s1)
if d2 in s2:
    print("Pangram")
else:
    print("Not Pangram")

"""

"""
#using dictionaries
abc={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
d={}
for i in s:
    if i in abc:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
x=d.keys()
print(d)
if(len(x)==26):
    print("Pangram")
else:
    print("Not Pangram")
"""

"""
#1st repeating character
s=input()
x=s.count('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
if(x>=2):
    print(x)
else:
    print(".")
"""

"""
#name and phn number(sir)
n=int(input())
d={}
for i in range(n):
    name, num= input().split()
    d[name]=num
while True:
    if s in d:
        print(s,"=",d[s])
    else:
        print("Not found")
"""



"""(wrong)-me
n=int(input())
d={}
for i in range(n):
    s=input()
    x=s.dict()
        
print(x)
"""

"""
#lexicological order for the given words
n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
print(d)
x=max(d.values())
l=[]
for i in d:
    if d[i]==x:
        l.append(i)
print(max(l) ,x)
"""

"""
#database (SPOJ-RPLD Platform)- corrupted or not 
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for j in range(r):
        k,l=map(int,input().split())
        if l in d:
            d[l].append(k)
        else:
            d[l]=[k]
for k in d:
    if len(d[k])!=len(set(d[k])):     #if(len(d[k])>n and len(set(d[k])==len(d[k]):            ( == or !=) donno
        print(f"Scenario #{i+1} : Impossible")
        break
else:
    print(f"Scenario #{i+1} : Possible")
"""

"""
#graphs(directed unwieghted) uding dictionary [R]
d={}
for i in range(int(input())):
    a,b=input().split()
    if a not in d:
        d[a]=[b]
    else:
        d[a].append(b)
x=input("Enter resquired:")
print(d.get(x,None))
"""

"""
#sir- directed unweighted graph
n=int(input())
route={}
for i in range(n):
    c1,c2=input().split()
    if c1 not in route:
        route[c1]=[c2]
    else:
        route[c1].append(c2)
print(route)
city=input()
if city in route:
    print(*route[city],sep=" ")
else:
    print("None")
"""

#directed weighted graphs
d={}
for i in range(int(input())):
    a,b,c=input().split()
    if a not in d:
        d[a]={b:c}
    else:
        d[a][b]=c
x=input("Enter required: ")
if x in d:
    m=min(d[x].values())
    for i in d[x]:
        if d[x][i]==m:
            print(i)
else:
    print(None)







































