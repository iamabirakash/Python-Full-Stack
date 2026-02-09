# def gen():
#     yield 1
#     yield 2
# res=gen()
# print(next(res))
# res.close()
# print(next(res))
# def gen2():
#     yield from gen()
#     yield 3
# res2=gen2()
# print(next(res2))
# print(next(res2))
# print(next(res2))



# def gen():
#     x = yield "hello"
#     yield x;
# res = gen();
# print(next(res))

# print(res.send(10));

class Parent(): 
	
	def __init__(self): 
		self.value = "Parent"
		
	def show(self): 
		print(self.value) 
		
class Child(Parent): 
	
	def __init__(self): 
		super().__init__()  
		self.value = "Child"
		
	def show(self): 
		print(self.value) 
		
obj1 = Parent() 
obj2 = Child() 

obj1.show()  
obj2.show() 