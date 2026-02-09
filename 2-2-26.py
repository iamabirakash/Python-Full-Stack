# # exception handeling 
# #  try - except - finally - else
# try:
#     num = int(input("ener the no.: "));
#     num2= input("enter the no.: ");
#     var = 10/num;
#     var2 = num2+num
# except TypeError:
#     print("enter the correct data type ")
# except ValueError:
#     print("enter the interger number ");
# except ZeroDivisionError as e:
#     print("cannot divide by zero", e);
# finally: # when we want to show the masg. to user always if the code have eny error or not 
#     print("hiii")

# class Student(Exception):
#     def show(self):
#         try:
#             num = int(input("ener the no.: "));
#             num2= input("enter the no.: ");
#             var = 10/num;
#             var2 = num2+num
#         except TypeError:
#             print("enter the correct data type ")
#         except ValueError:
#             print("enter the interger number ");
#         except ZeroDivisionError as e:
#             print("cannot divide by zero", e);
#         finally: # when we want to show the masg. to user always if the code have eny error or not 
#             print("hiii")
#         try:
#             name  = input("enter the name: ")
#             age = int(input("enter the age: "))
#             print("name: ",name)
#             print('age: ',age)
#         except ValueError:
#             print("enter the correct")

# s1 = Student()
# s1.show()

# custom base exception
# class Student(Exception):
#     def __init__(self, age):
#         if age <18:
#             raise Exception("age must be at least 18");
#         self.age = age;

# try:
#     S1= Student(13)
#     print(S1.age)
# except Exception as e:
#     print(e)


# base exception it's mean all type of errror

# class Student(Exception):
#     def show(self):
#         try:
#             num = int(input("ener the no.: "));
#             num2= input("enter the no.: ");
#             var = 10/num;
#             var2 = num2+num
#         except BaseException:
#             print("enter the correct data type ")
#         except ValueError:
#             print("enter the interger number ");
#         except ZeroDivisionError as e:
#             print("cannot divide by zero", e);
#         finally: # when we want to show the masg. to user always if the code have eny error or not 
#             print("hiii")
#         try:
#             name  = input("enter the name: ")
#             age = int(input("enter the age: "))
#             print("name: ",name)
#             print('age: ',age)
#         except ValueError:
#             print("enter the correct")

# s1 = Student()
# s1.show()


# Iterable --is a object in which you can lopp over with for 
# it is a object has iter() method 
# list1 = [10,2,3,34]
# for i in list1:
#     print(i)

# # iterator --> object having iter() and next() methods 
# # iter() --> provide one value at a time and remember the state 
# list1 = [10,2,3,34]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it)) --> it's give the error 


# cycle iterator --> it's use for cont. printing 
# from itertools import cycle
# colors = cycle(["read","green","blue"])

# it= colors
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# def test():
#     # return [10,20,30]
#     yield 10
#     yield 20
#     yield 30
# it=test()
# print(next(it)) #will print the output one by one, stope execution and remembers current state
#create a func which will return the even no from 1-10 using yield keyword
# def t():
#     for i in range(1,11):
#         if(i%2==0):
#             yield i
# it=t()
# print(next(it))
# print(next(it)) 

#generator expression

# gen=(x*x for x in range(6))
# it=gen
# print(next(it))
# print(next(it))
# print(next(it))

#memory efficiency
# def read():
#     with open("file.txt") as f:
#         for line in f:
#             yield line
# r=read()
# print(next(r))
#create 3 gen, one for even no 1-10, one for odd 1-10 third for sum of even and odd no


# gen1=(x for x in range(1,11) if x%2==0)
# it=gen1
# print(next(it))
# print(next(it))
# print(next(it))

# gen2=(x for x in range(1,11) if x%2!=0)
# it1=gen2
# print(next(it1))
# print(next(it1))
# print(next(it1))

# gen3=(x+i for x in gen1 for i in gen2)
# it2=gen3
# print(next(it2))
# print(next(it2))



