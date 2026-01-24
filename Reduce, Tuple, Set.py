#Reduce --> if u want to combine the elements of a list then u can use reduce 
# from functools import reduce
# lst=[10,20,30]
# res=reduce(lambda a,b: a+b, lst)
# print(res)
# map, filter, reduce
#these three  used for running a loop internally 

## Tuple --> immutable(can't change the data inside it -> the data is for read purpose only), ordered, fast
# In ordered we can use slicing and indexing
# tpl=10,20,30;  # not having round brackets still giving us tuple
#storing multiple values in a single variable is known as packing(basically gathering the elements)
# print(tpl);
# print(type(tpl));

# values inside tuple providing variables for it is  known as unpacking( basically scattering the elements)
# tpl=(10,20,30);
# a,b,c=tpl; #unpacking
# print(a)
# print(c)

#to use multiple values ad multiple variables in so that it will not throw error( as we have more no. of elemnts as compare to the variables)
# tpl=(10,20,30);
# a, *b= tpl;
# print(b)

#to update the tuple we need to convert it into list -> then after updating again u can change it to list

#Set=collection of unique elements, mutable, unordered(cant use index or slicing)
# st={1,2,2,3,8,5}
# print(st)
# print(st.add(6))
# print(st.update(3,10))#which no we want to update, with which no u want to update 
#remove, discard, pop

# st1={10,20,30}
# st2={30,40,50}
# # # union
# print(st1 | st2)   #union- combo of all sets
# print(st1 & st2)    #intersection -common between all sets
# print( st1 - st2)   #  difference - elemts of set 1 that does nt belong to b
# # s1-s2 = result which elemnets only belong yo s1
# print(st1^ st2)     #symmetric difference -- uncommon elemnts from both elemets
Youtube={'a','b','c','d'}
Insta={'a','c','e','f'}
LinkedIn={'c','f','g','h'}

# print( Youtube & Insta & LinkedIn )    # user using three platforms
# s1= Youtube &  Insta
# s2= Insta & LinkedIn
# s3= Youtube & LinkedIn
# print(s1 | s2 | s3)    #user using two platforms
# s11= Youtube ^  Insta
# print(s11 ^ LinkedIn)
s12 = Insta ^ Youtube
s13 = Youtube ^ LinkedIn
s23 = Insta ^ LinkedIn
print(s12)
print(s13)
print(s23)

print(s12 ^( s13 ^ s23))
