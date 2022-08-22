# newlist=[1,2,3,4,5]
#
# mylist=list(filter(lambda x:(x>1),newlist))
# print


# newlist=[2,3,4,5,6]
# mylist=list(map(lambda x: (x*2),newlist))
#
# print(mylist)


# x= "global"
#
#
# def fun():
#     global x
#     x=x * 2
#     print(x)
#
# fun()


# nonlocal variable
# def outer():
#     nonlocal x
#     x="local"
#     def local():
#
#         x= "nonlocal"
#         print(x)
#
#     local()
#     print(x)
#
# outer()


#
# def add():
#     global c
#     c=2
#
# add()
# print(c)


# def foo():
#     x=20
#
#     def loo():
#         global x
#         x=30
#
#     print("before calling nested function",x)
#     print("calling now")
#     loo()
#     print("after calling x",x)
#
# foo()
# print("in main",x)


# def fun():
#     global x
#     x=20
#
#     def sun():
#         global x
#         x=30
#     sun()
#     print(x)
#
# fun()
# print(x)


# def outer_function():
#     global a
#     a = 20
#
#     def inner_function():
#         global a
#         a = 30
#         print('a =', a)
#
#     inner_function()
#     print('i =', a)
#
#
# a = 10
# outer_function()
# print('a =', a)


# from math import e
#
# print("print math",e)

#
# import sys
# print(sys.path)

# import config
# print(dir(config))
#
# print(config.__doc__)


#
# print(0b1010111)
# print(0xFB + 0b10)
#
# print(0o15)

#
# print(int(2.5))
# print(float(5))
# print(complex('3+5j'))
#
# print(1.1+2.2)

# import decimal
# print(0.1)
#
# print(decimal.Decimal(0.1))

#
# from decimal import Decimal as d
#
# print(d('1.1')+d('2.2'))
# print(d('1.2')*d('2.50'))
#
# import fractions
#
# print(fractions.Fraction(1.5))
# print(fractions.Fraction(5))
# print(fractions.Fraction(1,3))


# from fractions import Fraction as f
#
# print(f(1.5))
# print(f(5))
#
#


#
# import fractions
#
# print(fractions.Fraction(1.1))
# print(fractions.Fraction('1.1'))


#
# from fractions import Fraction as F
#
# print(F(1.1)+F(1,2))
# print(1/F(5,6))
# print(F(-3,10)>0)
# print(F(-3,10)<0)


# import math
# print(math.pi)
# print(math.cos(45))
# print(math.exp(10))
# print(math.sinh(1))
# print(math.log10(1000))
# print(math.factorial(6))


# Python Mathematics


# import random

# print(random.randrange(10,20))

# x=[1,2,3,4,5,6]

# random.shuffle(x)
# print(x)
# print(random.random())
# print(random.choice(x))

#
# list=[1,2,3,4,5,6,7]
#
# print(list[1])
# print(list[2])
# print(list[0])


# nested list

#
# mylist=['hello',[1,2,3,4],[56,781,82]]
#
# print(mylist[0][4])
# print(mylist[1][3])
# print(mylist[2][1])


# negative indexing
#
#
# list=[1,2,3,4,5,6]
#
#
# print(list[-1])
# print(list[-4])


# #list slicing python
#
#
# x=['a','b','c','d','e']
#
# print(x[1:4])
# print(x[2:])
# print(x[:])


# Add/Change List Elements


# x=[1,2,3,4,5,6,7]
# x[0]=99
# print(x)
# x[2:5]=[8,9,10]
# print(x)


# Appending and Extending lists in Python
#
# x=[1,2,3,4]
# x.append(6)
# print(x)
# x.extend([99,66,88,55])
# print(x)


# Concatenating and repeating lists
# x=[1,2,4]
# print(x+[5,3,7])
# print(['re']*3)

# Demonstration of list insert() method
# x=[1,2,3]
# x.insert(2,5)
# x[2:2]=[44,55]
# print(x)

# Delete List Elements

# myList=['a','c','d','w','e','g']
# del myList[2]
# print(myList)
# del myList[2:4]
# print(myList)
# del myList
# print(myList)


#
# list=['a','b','c','d','e']
# list.remove('a')
# print(list)
#
# print(list.pop(1))
# print(list.pop())


#
# my_list = [3, 8, 1, 6, 8, 8, 4]
# my_list.append('a')
# print(my_list)
# print(my_list.count(3))
# print(my_list.index(1))


# pow=[2**x for x in range(10)]
# print(pow)


# List Membership Test

# list=['p','e','f','g','d']
#
# print('p' in list)
# print('s' in list)
# print('g' in list)


# Iterating Through a List
#
# for n in ['apple','banana','grapes']:
#     print("i like",n)


#
# tuple=()
# print(tuple)
#
# tuple=(1,2,3,4)
# print(tuple)
#
#
# tuple=(1,"suman",3+2j)
# print(tuple)


# tuple packing

#
# myTuple=1,2,"dog"
# print(myTuple)
#
# # tuple unpacking is also possible
#
# a,b,c=myTuple
# print(a)
# print(b)
# print(c)


# tuple = ("hello")
# print(type(tuple))
#
# tuple="hello",
# print(type(tuple))
#
# tuple =("hello",)
# print(type(tuple))
#
#


# nested tuple


#
# x=((1,2,3,4),[99,33,66],"suman",)
#
# print(x[0])
# print(x[2][1])


# slicing
# list ma negative indexing -1 tuple ma negative indexing 0
#
# array=['a','b','c','d','e']
#
#
# print(array[2:3])
# print(array[0:1])
# print(array[-3:-1])

# tuple=((1,2,3,4),[6,5])
#
# tuple[1][1]=99
# print(tuple)


# tuple=("a","b","c","D","e")
#
# print('a' in tuple)
# print('b' in tuple)
#
#
# print('g' in tuple)

# Using a for loop to iterate through a tuple

#
# for n in ('john','hp'):
#     print("hello",n)


# list='string!'
#
# print(list[1:-5])

#
# list=('programiz')
# list[0]='a'
#
#
# # list='python'
# print(list)


# Iterating through a string
#
# count = 0
# str='hello world'
# for n in str:
#     if n == 'l':
#         count+=1
# print("{} lettes found".format(count))
# print("%s's letter found "%(count))

#
# str="suman"
# list=list(enumerate(str))
# print(list)
# print(len(str))


#
# print('a' in 'battle')
# print('at' not in 'battle')
# print("'s'")


# #Python String Formatting
# print('''she said,"what's up?"''')
# print('she said,"what\'s up?"')
# print("she said,\"what's up?\"")

# str = "SUMAN KHATRI"
# print(str.lower())
# print(str.upper())
# print('HELLO'.join(str))
# print('suman khatri'.replace('suman', 'sk'))
# print('suman khatri'.find('i'))


# Creating Python Sets

# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

#
# my_set={1,2,3,4,5,3,4,2}
# print(my_set)
#
# my_set=set([1,2,3,4,5])
# print(my_set)
#
# my_set={1,2,3,[4,5]}
# print(my_set)


# creating empty set


# a={}
# print(type(a))
#
#
# a=set()
# print(type(a))


# Modifying a set in Python

# a={1,2,3}
# a.add(33)
# print(a)
#
# a.update([22,33,44])
# print(a)
#
# a.update([99,88,77],{11,44,55})
# print(a)


# Removing elements from a set
# a={1,2,3,4}

# a.pop()
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)


# Python Set Operations
# Set Union

# a={1,2,3,4,5}
# b={7,8,9,0}
# print(a|b)
# print(a.union(b))
# print(b.union(a))

# Set Intersection

# a={1,2,3,4}
# b={2,4,6,7}
# print(a&b)
# print(a.intersection(b))
# print(b.intersection(a))


# Set Difference

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a-b)
# print(a.difference(b))
# print(b.difference(a))


# Set Symmetric Difference

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a^b)
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))


# Set Membership Test
# a=set("suman")
# print('s' in a)


# Iterating Through a Set
#
# for n in set("apple"):
#     print(n)


# some of the built-in  function used commonly in set

# all() function returns:
#
# True - If all elements in an iterable are true
# False - If any element in an iterable is false

# a=[False]
# print(all(a))


# any() Return Value
# The any() function returns a boolean value:
#
# True if at least one element of an iterable is true
# False if all elements are false or if an iterable is empty

# a=[0,1,False]
# a=[0,False]
# print(any(a))


# Python enumerate()

# languages = ['Python', 'Java', 'JavaScript']
# enumerate_prime = enumerate(languages)
# convert enumerate object to list
# print(list(enumerate_prime))


# len(),max(),min(),sorted(),sum()
# a=[1,9,3,4]
# print(len(a))
# print(max(a))
# print(min(a))
# print(sorted(a))
# print(sum(a))


#
# a={1,2,3}
# a.add(5)
# print(a)
# a.update([1,2,3,45])
# print(a)


# forzenset


# a=frozenset([1,2,3,4])
# b=frozenset([3,4,5,6])
# print(a.isdisjoint(b))
# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# print(a^b)


# Creating Python Dictionary
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# print(my_dict)


# Accessing Elements from Dictionary


# my_dict={'name':'suman','age':"unknown"}
# print(my_dict)
# print(my_dict['name'])
# print(my_dict.get('age'))

# Changing and Adding Dictionary elements
# my_dict={'name':'suman','age':"unknown"}
# my_dict['address']="nepal"
# print(my_dict)


# Removing elements from Dictionary

# pop()
# a={1:2,3:4,5:6}
# print(a.pop(5))

# popitem()
# a={1:2,3:4,5:6}
# print(a.popitem())

# clear()

# a={1:2,3:4,5:6}
# print(a.clear())


# fromkeys()
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = 'vowel'
# creates a dictionary with keys and values
# vowels = dict.fromkeys(keys, value)
# print(vowels)

# items()

# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# print(sales.items())


# Python Dictionary update()
# marks = {'Physics':67, 'Maths':87}
# marks.update({'practical':48})
# print(marks)


# my_list = {}.fromkeys(['Math', 'Science', 'English'],0)
# print(my_list)
# for n in my_list.items():
#      print(n)
#
# print(list(sorted(my_list.keys())))



#Python Dictionary Comprehension
#
# square={x:x*x for x in range(6)}
# print(square)



# squares={x:x*x for x in range(10) if(x%2==1)}
# print(squares)
from pprint import pprint

squares={1:2,3:4,9:6,7:8}

# print('1' in squares)
# print('2' not in squares)

# Iterating through a Dictionary
# for n in squares:
#     print(squares[n])
#
# print(all(squares))
# print(any(squares))
# print(len(squares))
# print(list(sorted(squares)))2


#Opening Files in Python
#
# with open("text.txt",mode='a+') as f:
#
#     f.write("new record inserted today\n")
#     print(f.read())
#     f.seek(0)
#     print(f.read())
#
#     f.seek(0)
#     print(f.tell())


#read a file line-by-line using a for loop.

#
# with open("text.txt",'r') as f:
#     for line in f:
#         print(line,end='')


#readline()
# with open("text.txt",'r') as f:
#     print(f.readline())
#     print(f.fileno())
#     print(f.readable())
#     print(f.read(5))
#     print(f.writelines(["hello  i am using python"]))


#docstring
#
# def func():
#     '''hello man'''
#
# print(func.__doc__)



#directory

# import os
# print(os.getcwd())
# print(os.getcwdb())



#changing directory
# import  os
# print(os.getcwd())
# os.chdir('C:\\Users\sumit\OneDrive\Desktop')
# print(os.getcwd())


#list directory
# import os
# print(os.listdir('C:\\'))
# print(os.listdir())



#Making a New Directory

# import os
# print(os.mkdir('suman'))
# print(os.listdir())
#
# #Renaming a directory
#
# import os
# print(os.rename('suman','hp'))
# print(os.listdir())


#Removing Directory or File

#import os
#print(os.listdir())
#print(os.rmdir('hp'))
#print(os.remove('text.txt'))
#print(os.listdir())


#In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module.
# import os
# import shutil
# os.mkdir('suman')
# print(os.listdir())
# shutil.rmtree('suman')
# print(os.listdir())


# import os
# print(os.listdir())
# os.chdir('C:\Users\sumit\OneDrive\Desktop\python-intern\suman')
# print(os.listdir())
# with open('test.txt','w') as f:
#     f.write("hello")
# print(os.getcwd())

# print(dir(locals()['__builtins__']))


#Catching Exceptions in Python

# import sys
# randsys=['a',0,2]
#
# for n in randsys:
#     try:
#         print("the entry is {}".format(n))
#         r=1/int(n)
#         break
#     except:
#         print(sys.exc_info()[0],"occured")
#         print("next entry")
# print("the entry ",n,"is",r)



#print the name of the exception using the exc_info()

# import sys
# randomsys=['a',1,2]
# for n in randomsys:
#     try:
#         r=1/int(n)
#         print(r)
#         break
#     except Exception as e:
#         print(e.__class__)
# print("the reciprocal of ",n, "is",r)


#Raising Exceptions in Python

# try:
#     a=int(input("enter a number "))
#     if a<=0:
#         raise ValueError("this is not a positive number")
# except ValueError as ve:
#     print(ve)


#Python try with else clause
#
# try:
#     num = int(input("enter a number"))
#     assert num%2==0
# except Exception as e:
#     print("the number is not even number")
#
# else:
#     rec=1/num
#     print(rec)


#Python try...finally
#
# try:
#     f=open("text.txt","r")
#     # f.write("helo world")
#     print(f.read())
#
#
# finally:
#     f.close()


#User-Defined Exception in Python

# class Error(Exception):
#     pass
#
#
# class valueTooSmall(Error):
#     pass
#
# class valueTooBig(Error):
#     pass
#
#
#
# number=10
# while True:
#     try:
#         usrInput=int(input("enter a number"))
#         if usrInput<number:
#             raise valueTooSmall
#         elif usrInput>number:
#             raise valueTooBig
#         break
#     except valueTooSmall:
#         print("the given value is too big")
#     except valueTooBig:
#         print("the value it too big")
#
#
# print("congratulation the guess is true")








#Customizing Exception Classes
#
# class SalaryNotInRange(Exception):
#
#
#     def __init__(self,salary,message="the given salary is not in range form 5000 to 15000"):
#         self.salary=salary
#         self.message=message
#         super().__init__(self.message)
#
# salary = int(input("enter a salary"))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRange(salary)





#class

# class parrot:
#     species="bird"
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj1=parrot("Sandy",999)
# print(obj1.name)
# print(obj1.age)
# print(obj1.__class__.species)



#Creating Methods in Python



class parrot:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return "{} sings a {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)


obj1= parrot("sandy",1)
print(obj1.name)
print(obj1.age)
print(obj1.sing("happy"))