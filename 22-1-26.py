# a=20;
# b=input("Enter a num: ");
# print(id(a)); #id-> provides ypu unique num of object

# a=10;
# b=20;
# if(a>5 or b>20):
#     print("True");

# marks=int(input("Enter marks: "))
# if(marks>90 and marks<100):
#     print("A");
# elif(marks>80 and marks<90):
#     print("B");
# elif(marks>70 and marks<80):
#     print("C");
# else:
#     print("D");

# marks=int(input("Enter marks: "))
# if marks>=90:
#     print("A");
# elif 90> marks >=80:
#     print("B");
# elif 80>marks >=70:
#     print("C");
# else:
#     print("D");

# a=15;
# b=20;
# if(a>10):
#     print("a is greater than 10");
# elif(a>5):
#     print("A is greater than 5");


# print(2 & 3)   

# & --> bitwise and  
# | --> bitwise or
# ^ --> XOR
# left shift
# right shift
# a=6;
# b=8;
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(6 << 2)
# print(6 >> 1)
# print(5<<2)
# print(8>>2)

# a=10;
# b=15;
# print(a is b)

# print(a is not b)

# list=["btech","bca","mca"];
# if "btech6yh6  " in list:
#     print("True");

# if "mtech" not in list:
#     print("True");

# day=int(input("Enter the no."))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Looking forward for weekend")

# a=10;
# b=20;
# res= a if a>b else b;
# print(res)

# n=int(input("no. "))
# res= "even" if n%2==0 else "odd";
# print(res)


# user=1;     #integer
# user='qwerty';      #string
# print(user);\
# a=7985645;
# b=7985645;
# print(id(a))
# print(id(b))

# a='same';
# b='same';
# print(id(a))
# print(id(b))

# for i in range(1,51):
#     if(i%2==0):
#         print(i)

# i=0;
# while(i<10):
#     print(i,end=" ");
#     i=i+2


# for i in range(0,10,3):
#     print(i,end=" ")

# for i in range(10,0,-1):
#     print(i,end=" ")

# for i in range(0,11):
#         if(i==5):
#             break;
#         print(i,end=" ")

# for i in range(0,11):
#         if(i==5):
#             continue;
#         print(i,end=" ");

# for i in range(0,11):
#     if(i==5):
#         continue;
#     print(i,end=" ");
# else:
#     print("Iteration completed..");

# n=int(input("enter a number: "))
# for i in range(1,11):
#     print(n," X ", i," = ", n*i)

# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("") 



# n=int(input("Enter number: "))
# for i in range(1,n+1 ):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")   


#Pattern
# *****
# ****
# ***
# **
# *
# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print("*",end=" ")
#     print("")  

#function --> block of code used for reusability
# def sum(a,b):  # parameters not
#     return a+b ;   #return finsihes the function, stopd execution and return a value
# sum(10,20);         #arguments are real values
# #no output but still value is there
# #"****************************"


# def sum(a,b):  
#     return a+b ;   #return ->  pass the data from one function to another
# print(sum(10,20)); 

# def sum(a,b):
#     print(a+b);
# sum(30,67);

# sum(45,89)    #it is possoble in py that we can call the func before defining it
# def sum(a,b):
#     print(a+b)

# def fact(a):
#     if a<=1:
#         return 1
#     return a*fact(a-1)
# print(fact(5))


# def test(**kwargs):
#     print(kwargs);       #both give 
# test(name="xyz", age=30);     # outpout of kwargs in form of dictionary


# #args ->
# def test(**kw):
#     print(kw);       #both give 
# test(name="xyz", age=70); 


# def test(*args):
#     for i in args: 
#         print(i);       # output in form of list
# test(10,20,30); 


# def test(*args):
#     sum=0;
#     for i in args:     #sum using args and return
#         sum=sum+i;
#     return sum;
# a=test(10,20,30,40);
# print(a)


# def test(*args):
#     sum=0;
#     for i in args:                     #sum using args while writing print at first rather then return
#         sum=sum+i;
#     print(sum);
# test(10,20,30,40);


def test(a,b,*args, **kwargs):
   print("Parameter are: ",a,b);
   print("Arguments are: ",args);  #with args the data is stored in the tuple format
   print("Key arguments are: ", kwargs)  #with this data is stored in the  dictionary format
a=test(10,20,30,40,id=1, name="abir");

def test(*args,a,b, **kwargs):
   print("Parameter are: ",a,b);
   print("Arguments are: ",args);  #with args the data is stored in the tuple format
   print("Key arguments are: ", kwargs)  #with this data is stored in the  dictionary format
a=test(10,20,30,40,id=1, name="abir");