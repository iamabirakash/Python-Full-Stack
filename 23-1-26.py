# n=int(input("Enter number: "))
# def fibo(n):
#     if(n==0 & n==1):
#         return 1
#     if(n>=10):
#         return 1
#     return n+fibo(n+1)
# print([fibo(i) for i in range(10)])
  
# print(fibo(n))

# n=int(input("Enter number: "))
# def fibo(n):
#     a,b=0,1;
#     print(a)
#     print(b)
#     for i in range(2,n+1):
#         c=a+b
#         print(c)
#         a,b=b,c
# fibo(n)

# def add(a,b):
#     return a+b;        #y we use use return 
# def show(res):
#     print(res);
# show(add(10,20))


# def sum(a,b):
#     return a+b
# def show(a,b):
#     print(sum(a,b))
# show(10,20)

# def sum(a,b):
#     return a+b;
# print(sum(10,20))


# x=50;   #global variable-> we can access it from anywhere like from inside or outside of that function
# def test():
#     x=20;    #only def function can access this variable that is called local variable
#     #place where we are declaring variable is callled scope, function will search for local scope first then global scope
#     print("Inside fn ",x)
# test()
# print("outside fn ",x)

# x=50;
# def test():
#     x=100; #now update the global variablevalue inside the function
# test()
# print("Outside fn: ",x)


# x=50;
# def test():
#     global x #inside a function to change the local variable ito global use global word then we can update the valuee of global variable
#     x=100;
# test()
# print("outsoide function:" ,x)

#action you can choose 1. withdraw 2. enter the amount, deposit 3. bank balance check, exit

#ask user what she wants to do, use matchcase, exit code


# balance = 10000;
# def deposit(amount):
#     global balance;
#     balance = balance + amount;

# def withdraw(amount):
#     global balance;
#     if(balance >= amount):
#         balance = balance - amount;

# def show():
#     print("Balance is: ",balance);

# show();
# withdraw(5000);
# show();
# deposit(15000);
# show();



# balance=0;
# while True:
#     print("ATM MENU");
#     print("1. Witdraw")
#     print("2. Deposit")
#     print("3. Check balance")
#     print("4. Exit")
#     a=int(input("Enter number: "))
#     match a:
#         case 1:
#             w=int(input("Enter amount to withdrw: "))
#             if(balance >= w):
#                 balance = balance - w;
#                 print("Succesfull")
#             else:
#                 print("No Balance")
#         case 2:
#             d= int(input("Enter amonut to deposit"))
#             balance = balance + d;
#             print("Done")
#         case 3:
#             print("Show balnce: ",balance)
#         case 4:
#             print("Thankyou for visiting")
#             break;
#         case _:
#             print("Choose correct no.")


#recursion- function calling itself
# def fact(num):
#     if (num == 0):
#         return 1;
#     return num * fact(num-1);
# res=fact(5);
# print(res);


# def fibo(num):
#     if(num<=1):
#         return 1;
#     return fibo(num-1) + fibo(num-2);

# print([fibo(i) for i in range(10)])

#lambda function -> anonymous function --> function without name
#  we can do function calling, function definition  and etc using lambda function in one line only
# add= lambda a,b: a+b;
# print(add(10,20));

# mul= lambda x: x*x;
# print(mul(5));

# divide = lambda x,y: x/y;
# print(divide(10,2))

#Starting with anew topic i.e. list
#list are mutable(we can change /add/ remove the elements)
#list --> mutable and oderted(u can access the elemnt on the basis of index) collection of element
#[] --> we use qaure brackets to make a list
# indexing and slicing - yes
# lst=[10,20,30,40];
# print(lst[0]);
# print(lst[-1]); #lst[start, stop, step]
# print(lst[0:3]);
# print(lst[:3])
# print(lst[0:7])
# print(lst[-1:-4:-2])  #while going backward we must add  step negative
# print(lst[-4:-1])
# print(lst[5:0:-1])
# lst1=[10,20,30,40,50,60];
# print(lst1[-6:-1:2])

# lst2=[12,24,65,78];
# lst2[0]=20;
# for i in lst2:
#     print(i,end=" ")

#largest number 
# lst3=[23,45,12,35,79,9,98]
# max=lst3[0]
# for i in lst3:
#     if(max<i):
#         max=i;
# print("Largest: ", max)

#One Code for both Largest and Second Largest Number
# largest=lst3[0];
# second=lst3[1];
# for i in lst3:
#     if i> largest:
#         largest=i;
# print(largest);
# for i in lst3:
#    if i>second and i!=largest:
#         second=i;
# print(second)  

# lst=["BCA","BTech", "MCA","MTech"];
# #built in functions
# #adding the elements
# #append -- last position,
# #insert-- insert value in a specificposition with two parameters
# #extend-- multiple values 

# # lst.append("BSC")
# lst.extend(['BSC','MSC']);
# # lst.insert(1,"BSC"); # 2 parameters 1. position, 2. elements
# # print(lst)
# new_lst=[];
# new_lst.append(lst)
# print(new_lst)


#Usage of List Comprehension
# lst=[10,20,30];
# new_lst=[i for i in lst];      # list comrehension, one i for appending, second i for  iteration
# new_lst=[i+10 for i in lst];
# #for i in lst:
#     # new_lst.append(i+10);
# print(new_lst);


# lst=[100,200,300]
# new_lst=[num+4 for num in lst];
# print(new_lst)

# lst= [2,3,4,5,6,7,8]
# new_lst=[i for i in lst if i%2==0];
# print(new_lst)
#remove elements
#remove, pop, clear
# lst.pop(2);
# lst.clear();
# print(lst.count(3))    #count will tell us the occurence of the elements
# lst.sort(reverse="True")
# lst.reverse();
#with map u can update each and every element of the list
# print(lst)


#map --> performs operations on each element of a list
# lst=[2,3,3,3,4,5,6,7,8];
# res=list(map(lambda x: x+5,lst) )#1. logic purpose   uses lambda so that we can make logic in only one line 2. parameter is iterator
# print(res)
#map and filter always return filter object and object


#filter --> select the elements based on few conditions than, filter out the elements based on same conditions
lst=[2,3,3,3,4,5,6,7,8];
res=list(filter(lambda x: x>5,lst))
print(res)