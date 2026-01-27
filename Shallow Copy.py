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

