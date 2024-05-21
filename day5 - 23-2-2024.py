"""
#odd even index- Approach-1
s=input()
e=" "
o=" "
for i in range(len(s)):
    if i%2==0:
        e+=s[i]
    else:
        o+=s[i]
print("Even index:",e)
print("Odd Index:",o)
print(e+o)
"""

"""
#odd even index- Approach-2
s=input()
e=s[1::2]
o=s[::2]
print(e)
print(o)
print(e+o)
"""

"""
#count of a given character - Approach-1
s=input()
ch=input()
print(s.count(ch))
"""

"""
#count of a given character - Approach-2
s=input()
ch=input()
c=0
for i in range(len(s)):
    if ch == s[i]:
        c+=1
    
print(c)
"""

#even count of a given character


"""
#only vowels in a string-Approach -1
s=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
v=0
c=0
for i in range(len(s)):
    if s[i] in vowels:
        v+=1
    else:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")
"""

"""
#only vowels in a string-Approach -2
s=input()
vowels="aeiouAEIOU"
v=0
for i in s:
    if i in vowels:
        v+=1
if v==len(s):
    print("Yes")
else:
    print("No")
"""

"""
#only vowels in a string-Approach -3 (More efficient)
s=input()
vowels="aeiouAEIOU"
c=0
for i in s:
    if i not in vowels:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")
"""

"""
#only vowels in a string-Approach -4
s=input()
vowels="aeiouAEIOU"
c=0
for i in s:
    if i not in vowels:
        print("No")
else:
    print("Yes")
"""


"""
#only numbers in a string-Approach -1
s=input()
numbers=['0','1','2','3','4','5','6','7','8','9']
c=0
for i in range(len(s)):
    if s[i] in numbers:
        c+=1
if len(s)==c:
    print("Yes")
else:
    print("No")
"""

"""
#only numbers in a string-Approach -2
s=input()
numbers="0123456789"
c=0
for i in s:
    if i in numbers:
        c+=1
if c==len(s):
    print("Yes")
else:
    print("No")
"""

"""
#only numbers in a string-Approach -3 
s=input()
numbers="0123456789"
c=0
for i in s:
    if i not in numbers:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")
"""

"""
#only numbers in a string-Approach -4 (More efficient) [using built-in method
s=input()
if s.isdigit():
    print("Yes")
else:
    print("No")
"""

"""
#count vowels and consonants - Approach-1
s=input()
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  #we write consonants bcz it may consider numbers also as consonants
v=0
c=0
for i in s:
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1
print(v ,c)
"""

"""
#count vowels and consonants - Approach-2
import string
s=input()
vowels="aeiouAEIOU"
v=0
c=0
for i in s:
    if i in vowels:
        v+=1
    elif i in string.ascii_letters:
        c+=1
print(v ,c)
"""

"""
#count vowels and consonants - Approach-3
import string
s=input()
vowels="aeiouAEIOU"
v=0
c=0
for i in s:
    if i in vowels:
        v+=1
    elif i.isalpha:
        c+=1
print(v ,c)
"""

"""
s=input()
vowels="aeiouAEIOU"
v=0
c=0
for i in s:
    if i.isalpha():
        if i in vowels:
            v+=1
        else:
            c+=1
print(v ,c)
"""

"""
#compress a string(wrong)
s=input()
comp=" "
cs=" "
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        x=s[i]
        if s[i]==s[j]:
            c+=1
comp=str(x)+str(c)
cs+=comp
print(cs)



#bbbaaahh- b2a3h2
"""

"""
#number of words,vowels and consonants
for _ in range(int(input())):
    s=list(input().split())
    vowels="aeiouAEIOU"
    v=0
    c=0
    word=len(s)
    for i in s:
        for j in i:
            if i.isalpha():
                if j in vowels:
                    v+=1
                else:
                    c+=1
    print(word ,v ,c)
"""




""" (above problem ans.. wrong)
    space=0
    word=0
    for i in s:
        if i==" ":
            space+=1
        else:
            word.append(i) """


"""
#guess the number:   data structures-srucures
t=int(input())
res=""
for _ in range(t):
    a,b=list(input().split())
    for i in b:
        if i not in a:
            res+=i
print(res)   
"""

#print(ord('s'))

""""

#convert the given ascii value a after few numbers
t=int(input())
for i in range(t):
    a,b=input().split()
    b=int(b)
    r=""
    for i in a:
        k=ord(i)+b
        if k>122:
            k=96+(k-122)
            r=r+chr(k)
           else:
            r=r+chr(k)
    print(r)
"""

"""
#OOPS- factorial using method
class classa:
    def factorial(self,n):
        r=1
        for i in range(1,n+1):
            r=r*i
        print(r)
obj=classa()     #this is question
obj.factorial(5)
"""

"""
#factorial using constructor
class classa:
    def __init__(self,n):
        self.n=n
        print(n)
    def factorial(self):
        r=1
        for i in range(1,self.n+1):
            r=r*i
        print(r)
ob=classa(5)
ob.factorial()
"""



class classa:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)
        print(fact(self.n))
ob=classa(5)
ob.factorial()







































































































































































