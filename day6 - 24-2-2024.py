"""
#prime or not using class and object
class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        p=0
        for i in range(2,self.n):
            if self.n%i==0:
                p+=1
        if p==0:
            return "True"
        else:
            return "False"
ob1=classn(20)
ob2=classn(10)
print(ob1.isprime())
print(ob2.isprime())
"""

"""
#palindrome using classes and objects
class check:
    def __init__(self,n):
        self.n=n
    def palindrome(self):
        if self.n==self.n[::-1]:
            print("Yes")
        else:
            print("No")
ob1=check("sos")
ob2=check("Hello Pragatians")
ob1.palindrome()
ob2.palindrome()
"""

"""
#wrong
class total:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        p=0
        for i in range(2,self.n):
            if self.n%i==0:
                p+=1
        if p==0:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        a=self.n
        t=0
        while a!=0:
            x=a%10
            t=(t*10)+x
            a=a//10
        if(self.n==t):
            print("Yes")
        else:
            print("No")
ob1=total(22)
#ob2=total(10)
ob1.isprime()
ob1.ispalindrome()
#ob2.isprime()
#ob2.palindrome()
"""

"""
#total to check both prime and palindrome at a time
class total:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        p=0
        for i in range(2,self.n):
            if self.n%i==0:
                p+=1
        if p==0:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        a=str(self.n)
        if a==a[::-1]:
            print("Yes")
        else:
            print("No")
ob1=total(22)
ob2=total(10)
ob1.isprime()
ob1.ispalindrome()
ob2.isprime()
ob2.ispalindrome()
"""


"""
#check prime and palindrome with 2 parameters
class total:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def isprime(self):
        p=0
        for i in range(2,self.n):
            if self.n%i==0:
                p+=1
        if p==0:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        a=str(self.s)
        if a==a[::-1]:
            print("Yes")
        else:
            print("No")
ob1=total(22,"sas")
ob2=total(13,"Hello")
ob1.isprime()
ob1.ispalindrome()
ob2.isprime()
ob2.ispalindrome()
"""

"""
#public access spsecifier
class car:
    speed=0
    name=""
    def __init__(self):
        self.speed=100
        self.name="BMW"
    def drive(self):
        print(self.speed)
c=car()
c.drive()
c.speed=200
c.drive()
"""

"""
#private access spsecifier
class car:
    __speed=0
    __name=""
    def __init__(self):
        self.__speed=100
        self.__name="BMW"
    def drive(self):
        #self.__speed=150
        print(self.__speed)
c=car()
c.drive()
c.__speed=200
c.drive()
"""

"""
#super() method example
class Parent:
    def __init__(self):
        print("Parent Class")
class child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class")
c=child()
"""

"""
#single inheritance
class Dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def display1(self):
        print(self.date)
        d={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        for i in d:                   #print(d[self.month])
            if i==self.month:
                print(d[i])
                break
        print(self.year)    
class details(Dob):
    def __init__(self,name,age,date,month,year):
        self.name=name
        self.age=age
        self.date=date
        self.month=month
        self.year=year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)

p=details("abc",27,24,8,2001)
p.display()
p.display1()
"""

"""
#multi-level inheritance simple example
class grandfather:
    def grandmother(self):
        print("This is grandfather")
class father(grandfather):
    def mother(self):
        print("This is father")
class son(father):
    def wife(self):
        print("This is son")
s=son()
s.grandmother()
s.mother()
s.wife()
"""

"""
#multi-level inheritance
class vehicle:
    def __init__(self,fuel):
        self.fuel=fuel
    def display3(self):
        print(self.fuel)
class motor(vehicle):
    def __init__(self,cc,fuel):
        self.cc=cc
        self.fuel=fuel
    def display2(self):
        print(self.cc)
        print(self.fuel)
class car(motor):
    def __init__(self,name,cc,fuel):
        self.name=name
        self.cc=cc
        self.fuel=fuel
    def display1(self):
        print(self.name)
        print(self.cc)
        print(self.fuel)
v1=car("BMW","300cc","Petrol")
v1.display1()
v1.display2()
v1.display3()
"""

#multiple inheritance


"""
#hierarchical inheritance without abstractmethod
class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=self.l*self.b
        print(a)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        x=self.s*self.s
        print(x)
c1=square(2)
c1.area()
c2=rectangle(2,5)
c2.area()
"""

"""
#hierarchical inheritance with abstractmethod
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=self.l*self.b
        print(a)
class square(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        x=self.s*self.s
        print(x)
c1=square(2)
c1.area()
c2=rectangle(2,5)
c2.area()
"""

#exception
try:
    a=int(input())
    b=int(input())
    c=a//b
except ZeroDivisionError:
    print("Division Error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")



