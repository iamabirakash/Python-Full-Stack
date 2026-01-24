# 1. Create a program that reverses each word but keeps the sentence order unchanged. 
# Example: 
# Input: 
# Python is powerful 
# Output: 
# nohtyP si lufrewop 
# a= "Python is powerful"
# b=list(a.split())
# print(a)
# l2=[]
# for i in b:
#     l2.append(i[::-1])
# # print(l2)
# print(" ".join(l2))



# 2. Create a program using *args to multiply all numeric values. Ignore non-numeric values. 
# Example: 
# Input: 
# multiply(2, 3, 'a', 4) 
# Output: 
# 24 
# def test(*args):
#     mul=1
#     for i in args:
#         a=type(i)
#         if (a==int):
#                mul=mul*i;
#     print (mul); 
# a= test(2,3,'a',4)



# 3. Create a program using lambda, filter, and map 
# Create a program to filter even numbers from a list and square them. 
# Example: 
# Input: 
# [1, 2, 3, 4, 5, 6] 
# Output: 
# [4, 16, 36] 
# lst=[1,2,3,4,5,6]
# new_lst=list(filter(lambda x: x%2==0,lst))
# print(new_lst)
# res=list(map(lambda x: x*x,new_lst))
# print(res)



# 4. Create a program to find the longest word in a string 
# Create a program to find the longest word without using max(). 
# Example: 
# Input: 
# Python makes programming interesting 
# Output: 
# Programming 
# a="Python makes programming interesting"
# b=list(a.split())
# max=0;
# max_str=" "
# for i in b:
#     n=len(i);
#     if(n>max):
#         max=n
#         max_str=i;
# print(max_str," : ", max)



# 5. Create a program to remove duplicate elements from a list 
# Create a program to remove duplicates while preserving order. 
# Example: 
# Input: 
# [1, 2, 3, 2, 1, 4] 
# Output: 
# [1, 2, 3, 4] 
# a = [1, 2, 3, 2, 1, 4]
# n = len(a)
# i = 0
# while i < n:
#     j = i + 1
#     while j < n:
#         if a[i] == a[j]:
#             a.pop(j)   
#             n -= 1    
#         else:
#             j += 1
#     i += 1

# print(a)



# 6. Create a program to find common elements in two lists 
# Create a program to find common elements between two lists without using set. 
# Example: 
# Input: 
# [1, 2, 3, 4] 
# [3, 4, 5, 6] 
# Output: 
# [3, 4] 
# def comm(list1, list2):
#     result = []
#     for i in list1:
#         if i in list2 and i not in result:
#             result.append(i)
#     return result
# list1=[1,2,3,4]
# list2=[3,4,5,6]
# print(com(list1, list2))



# 7. Create a program to rotate a list by k positions 
# Create a program to rotate elements of a list to the right by k positions. 
# Example: 
# Input: 
# List: [1, 2, 3, 4, 5] 
# k = 2 
# Output: 
# [4, 5, 1, 2, 3] 
# def rot(lst, k):
#     n = len(lst)
#     k = k % n  
#     return lst[-k:] + lst[:-k]
# a = [1, 2, 3, 4, 5]
# k = 2
# rotated = rot(a, k)
# print(rotated)



# 8.  Create a program to find missing number in a list 
# Create a program to find the missing number from a list containing numbers from 1 to n. 
# Example: 
# Input: 
# [1, 2, 3, 5] 
# Output: 
# 4 

# def find(lst):
#     n = len(lst) + 1  
#     exp= n * (n + 1) // 2
#     act= sum(lst)
#     return exp - act
# num = [1, 2, 3, 5]

# print(find(num))



# 9. Create a program to simulate a login system 
# Create a program that: 
# • Accepts username & password 
# • Allows only 3 attempts 
# Example Output: 
# Login Successful 
# or 
# Account Locked 

# USER= "amisha"
# PASS = "12345"
# attempts = 0

# while attempts < 3:
#     user = input("Enter username: ")
#     pwd = input("Enter password: ")
#     if user == USER and pwd == PASS:
#         print("Login Successful")
#         break
#     else:
#         attempts += 1

# if attempts == 3:
#     print("Account Locked")



# 10. Create a program to find the first non-repeating character 
# Create a program to find the first non-repeating character in a string. 
# Example: 
# Input: 
# swiss 
# Output: 
# W
def find(s):
    count={}
    for char in s:
        count[char]=count.get(char,0)+1;
    for char in s:
        if count[char]==1:
            return char
    return None
input='swiss';
result=find(input);
print(result)
