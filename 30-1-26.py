#instance variable--> depends on the object , different for every object, we use self
# but class variable remain same, in every object
# #Class method and Static method
#class method--> it works with class variable
#here we use cls 
# @classmethod--> this dont work for  object
# class Student:
#     school="ABC"; #class variable

#     @classmethod
#     def change(cls,newName):
#         cls.school=newName;
# Student.change("XYZ");
# print(Student.school)


# class Car:
#     model="BMW";
#     @classmethod
#     def change(cls,newName):
#         cls.model=newName;
# Car.change("Creta");
# print(Car.model)


#Static method--> a normal function  that is inside the class, use static method to wrap up the function
#no self, no cls
#@staticmethod
#USE--> 
# class A:
#     @staticmethod
#     def add(a,b):
#         return a+b;
# print(A.add(10,20))


#File Handling--> store data permanently
#Open, read, write, append, delete

#Types of files-->text files, binary files

#Text file Modes--> r,w, r+(read& write), w+(write &read),a\
#binary Files--> rb, wb --> we store 0 & 1 example--> audio & video files, photos 

# f=open("newTextFile.txt","w");
# f.write("This is a text file")
# f.write("\n File handling")
# f.close()

# f=open("newTextFile.txt","r");
# data = f.read()
# print(data)

# f=open("newTextFile.txt","r");
# data = f.readline() #read linen by line
# print(data)


# f=open("newTextFile.txt","r");
# data = f.readlines() #give result in list
# print(data)

# # update the file 
# f=open("newTextFile.txt","a");
# f= f.write(" File handling Appending something")

 #! Delete
import os
# os.remove("newTextFile.txt");

#! tell() and seek()
#!tell()--> to check the cursor position
# f=open("newTextFile.txt","w");
# f.write("This is a text file")

# f=open("newTextFile.txt","r+")
# print(f.tell());

#! seek()--> changing the cursor position

# f.seek(8);
# print(f.tell());
# f.write("File Handling......");
# f.close();

#read and write
# f=open("newTextFile.txt","r+");
# f.seek(8); #specific position
# f.write("Hii,There") 
# f.close()

#Append: at the last
# f=open("newTextFile.txt","a");
# f.seek(8);
# f.write("Hii,There") 
# f.close()
#give result in list

#!With-->
# with open("newnew.txt", "w") as f:
#     f.write("This is new file......")
# os.remove("newnew.txt");

#binary files
# f=open("image.jpg","rb");
# data=f.read();
# print(data);  #we cant see this this will show in the format f  0 ,1

#CSV--> comma separated values
import csv
with open("menu.csv","w") as f:
    # pass;  #
    writer=csv.writer(f);
    writer.writerow(["Pizza","Pasta","Pav Bhaji"]) 
    #we can create one row here, we cant use nested level data 
    writer.writerow(["Hotchocolate","Vada Pav","Kadhi Chawal"])
    # writer.writerows(["Brownie Icecream","Adrak chai","Aloo parantha"])

with open("menu.csv","r") as f:
    reader=csv.reader(f);
    for i in reader:
        print(i)