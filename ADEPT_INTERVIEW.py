#split a string
#reverse it
#put it back together
#use split(), reversed(), join()

# test_string = input("Enter a string: ")
# print("The original string is:\n", str(test_string))

# new = " ".join(reversed(test_string.split(" ")))
# print("The new string is:\n", str(new))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def new_string():
#     old_string = input("Enter a string: ")
#     print("The original string is:", str(old_string))
    
#     new = " ".join(reversed(old_string.split(" ")))
    
#     print("The new string is:", str(new))
    
# new_string()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def girlfriend():
#     old_girlfriend = input("Enter your string here: ")
#     print("The original string is: ", str(old_girlfriend))
    
#     new_girlfriend = " ".join(reversed(old_girlfriend.split(" ")))
    
#     print("The new string is: ", str(new_girlfriend))
    
# girlfriend()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Creating a class and object with class and instance attributes

# class Dog:
    
#     # class attribute
#     attr1 = "asshole"
    
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
        
# # driver code
# # object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# # accessing class attributes
# print("Rodger is an {}".format(Rodger.__class__.attr1))
# print("Tommy is an {}".format(Tommy.__class__.attr1))

# # accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Creating Class and objects with methods

# class Dog:
    
#     # class attribute
#     arrt1 = "mammal"
    
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print("My name is {}".format(self.name))

# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# # Accessing class methods
# Rodger.speak()
# Tommy.speak()

# class Car:
    
#     def __init__(self,name):
#         self.name = name
        
#     def talk(self):
#         print("My name is {}".format(self.name))
        
# Rodger = Car("Rodger")
# Tommy = Car("Tommy")

# Rodger.talk()
# Tommy.talk()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Inheritence in Python

# parent class
# class Person(object):
    
# 	# __init__ is known as the constructor
# 	def __init__(self, name, idnumber):
# 		self.name = name
# 		self.idnumber = idnumber

# 	def display(self):
# 		print(self.name)
# 		print(self.idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("ID Number: {}".format(self.idnumber))
	
# # child class
# class Employee(Person):
# 	def __init__(self, name, idnumber, salary, post):
# 		self.salary = salary
# 		self.post = post

# 		# invoking the __init__ of the parent class
# 		Person.__init__(self, name, idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("ID Number: {}".format(self.idnumber))
# 		print("Post: {}".format(self.post))


# # creation of an object variable or an instance
# a = Employee('Christopher', 11592657, 200000, "Intern")

# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Polymorphism in Python

# class Bird():
    
#     def intro(self):
#         print("There are many types of birds\n")
        
#     def flight(self):
#         print("Most birds can fly but some cannot\n")
        
# class sparrow(Bird):
    
#     def flight(self):
#         print("Sparrows can fly\n")
        
# class ostrich(Bird):
    
#     def fligt(self):
#         print("Ostriches cannot fly\n")
        
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Polymorphism in Python

# create a base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeekforGeeks"
        
# #create a derived class
# class Derived(Base):
#     def __init__(self):
        
#         #call constructor of
#         # base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
        
# # Driver code
# obj1 = Base()
# print(obj1.a)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Reverse a string

def main():
    a = input("Enter a string: ")
    print("The original string is: ", str(a))
    
    b = " ".join(reversed(a.split(" ")))
    
    print("The new string is: ", str(b))
    
main()