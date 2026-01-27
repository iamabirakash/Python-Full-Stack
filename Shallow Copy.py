# #dict--> where we have key & value pair
# #nested dictionary--> dictinary inside a dictionary
# dict={ 'a': {'b':676},'c':{'d':43}}
# print(dict)
# print(dict['a']['b']) #we can print the value of dictionary using keys
# dict1={
#     "name":"ABC",
#     "ID":1,
#     "address":{
#         "Home":"Chandigarh",
#         "Work":["Delhi","Noida"],
#     },
# }
# dict1["age"]=20;  #this will add this key value pair in the existing dictionary
# print(dict1['ID'])
# print(dict1["name"][1])
# print(dict1["address"]["Home"])
# print(dict1["address"]["Work"][1])

# #keys(),values(), items()
# for i in dict1:
#     print(i) #this will only print the keys
# for i in dict1.values():   #this will print value pair
#     print(i)
# for i,j in dict1.items():  #this will print all the key and value pair
#     print(i," ",j)

# dict={
#     "name":"amisha",
#     "ID":123,
#     "city":"Jalandhar"
# }
# dict1={
#     "state":"Punjab",
#     "Mobile No":123456
# }
# dict1.update(dict)
# print(dict1)

# a=[10,20,30];
# b=a  #reference --> refer b is taking the reference of a
# b[0]=100;
# print(a)  #here the data is changing in a also bcz b is referencing to a
# print(b)
# print(id(a))
# print(id(b))


#Shallow copy
#different objects till one level(not for nested lists)
#import copy(importing module)
# a=[10,30,40];
# b=a[:]  
# b[0]=100;
# print(a)
# print(b)
# print(id(a)) 
# print(id(b))
# # 
# a=[[10,20],[30,40]];
# b=a[:]   #--> shallow copy   --> whenever we add this su=ymbol in a list then the changes are made  only in b and chnages are not visible in a
# b[0]=100;
# print(a)
# print(b)
# print(id(a)) #ids are diffferent means they are pointing to diff diff address
# print(id(b))

#DEep Copy--> create diff objects for multiple levels
# import copy
# a=[[10,20],[30,40]];
# b=copy.deepcopy(a);
# b[0][0]=100;
# print(a)
# print(b)
# print(id(a)) #ids are diffferent means they are pointing to diff diff address
# print(id(b))

# Difference between shallow copy and deep copy

#Strings--> sequence of characters
#nature --> just like lists, but strings are immutable
# str="Python" 
# str1=''
# str2='''
# This is 
#         multiline string
# '''
#dic

# string
#as similar to list we can use indexing also here
#but we cant change/update that particular string

# str="Python"
# print(str)
# print(id(str))
# str=str+" Programming"   #whenever we are changing the str new object is made 
# print(str)
# print(id(str))

#functions and methods difference
# a function that belongs to particular class--> methods
# a function that doesn't belong to a particular class--> functions

#functions
#len, lower, upper, capitialize(convert first letter of a word to capital), title(change the first letter of each word to capital),
# concat, strip, lstrip, rstrip, count, split(split the word into alist), join

str='Amisha mehta'
print(len(str))
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.count('a'));  #str--> occurence of which letter
print(str.title())



#Decorators--> it will add behaviour to function --> ehat decorator do is decorate the code basically add
# whenever we decorate the function need to wrap uo the logic 
# def greet(fx):  #this is our decorator , we can pass the data from one function to another function
#     def mfx():
#         print("Hi, class ");
#         fx()        #the function we are decorating this time and here we are decorating show function
#         print("Function is executed"); #this logic is wrap up inside another function that is mfx
#     return mfx;

# @greet  #we are using @--> annotation to tell the interpreter that we are decorating this function
# def show():
#     print("This is a function")
#show(); to print show function
# @greet
# def test():
#     print("This is test function")

# test();
# @greet
# def bday():
#     print("HAPPY BIRTHDAY")
# bday();

# @greet
# def test():
#     print("This is test function")

# greet(test)(); #pass function as arguments  no need to put brackets we are passing the show function as an argument to the greet function

# def bday(fx):
#     def happy():
#         print("HAPPY BIRTHDAY")
#         fx()
#         print("BIRTHDAY KHTM");
#     return happy;

# @bday
# def amisha():
#     print("HELLO")
# amisha();

#this is a type of encapsulation --> find, wrap the data
# We can pass the value/statement with the help of return keyword

# def greet(fx):
#     def mfx():
#         print("Hi, class");
#         fx();
#         print("Function executed");
#     return mfx;

# def add(a,b):
#     print(a+b);                                                                                                            
# greet(add(10,20))();


# def greet(fx):                                                                                                                                                     
#     def mfx(a,b):
#         print("Hi, class");
#         fx(a,b);
#         print("Function executed");
#     return mfx;

# def add(a,b):
#     print(a+b);
# greet(add)(10,20);

# def greet(fx):
#     def mfx(*args):
#         print("Hi, class");
#         fx(*args);
#         print("Function executed");
#     return mfx;

# def add(a,b):
#     print(a+b);
# greet(add)(10,20);

#regex: regular expresion--> to get some insigts from the pattern, pattern matching in strings
# import re   #importing re module

#basic functions
# # search()- find the first occurence of the word, to search the particular word at the starting of the list
# text="Hello World"
# result=re.search("World",text)    #2. parameters 1. what to search, where to search
# if result:
#     print("Found...")

# #re.finadall() --> return all matches as a list
# s='cat bat rat mat'
# print(re.findall("at",s))

# # re.match--> 
# print(re.match("bat",s)) #if the word is in the starting then only we can find the word otherwise we cant
# print(re.match("cat",s))

#split
# str="python is a high level language";
# result=str.split()
# print(result)

# import math
# from math import sqrt, factorial
#from math import * (to import everthing from math module)
# print(sqrt(16));
# print(math.sqrt(9));

# print(factorial(5));


# can we accrees the method inside the file  --> yes
# import calc 
# print(calc.add(10,20))

from datetime import datetime
# print(datetime.date(3-2-2026))
print(datetime.now())
print(datetime.today()) 
#datetime is a module and function name also

#print specific time and date with the help of time and date module


#random module
import random
# print(random.random())     #provides random values bw 0 to 1
# print(random.randint(1,10));
# print(random.seed(3));  #this is used to fix the value of randint 
# print(random.randint(1,10));

colors=['red','blue','black'];
random.shuffle(colors);
print(colors);

#guess the number game
print("*****************************Guess the Number game*********************************")
n=random.randint(1,50)
print();
count=0;
count1 =10
while(True):
    if(count1>0):
        num=int(input("Guess a Number (1-50): "))
        if(num>50):
            print("Choose number betwwen the given range.")
        
        else:
            if(num==n):
                print("YOU WON!!")
                print("Chances left: ", count1)
                print("In how much counts u did it: ",count)
                print("Acurracy",100-((count/10)*100))
                break;
            if(num>n):
                print("Guess the smaller number")
                print("Chances left: ", count1)
                count+=1;
                count1-=1
                continue;
            else:
                print("Guess the larger number")
                print("Chances left: ", count1)
                count+=1;
                count1-=1
                continue;
    else:
        print("YOU LOOSE, PLAY AGAIN!!")
        break;

