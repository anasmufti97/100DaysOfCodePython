# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         print("this is constructor")

#     def greet(self):
#         print(f"Hello, {self.name}!")

# # Creating an instance of MyClass
# my_object = MyClass("Anas")
# my_object.greet()  # Output: Hello, Anas!     

# DECORATORS = Take function as an argument and modify it 


# def decorator_function(original_function):
#     def wrapper_function():
#         print("Wrapper executed before the original function")
#         original_function()
#         print("Wrapper executed after the original function")
#     return wrapper_function


# @decorator_function
# def display():
#     print("Display function executed")  

# decorator_function(display)()  # This will return the wrapper function/
# display()  # Output: Wrapper executed before the original function  



# class Person:


#     name = "name"
#     # def __init__(self):
#           # _name is considered 'protected'

#     # @property
#     def name2(self):
#         print("Getting name...")
#         return self.name

#     @name.setter
#     def name(self, value):
#         print("Setting name...")
#         if not isinstance(value, str):
#             raise ValueError("Name must be a string")
#         self._name = value


# p = Person()
# p.name = "Ali"     # Setter called
# print(p.name)


# obj = Person()
# obj.name = "Aliobj" 
# print(obj.name) # Output: Setting name...


# NO use of self in the function if it is static method


# class Student:
#     # Class variable
#     school_name = "Green School"
#     def __init__(self, name):
#         self.name = name  
#         # self.school_name = "Green School"  # Instance variable

# s1 = Student("Anas")
# s2 = Student("Ali")


# s1.school_name = "Green"  # Instance variable
# print(Student.school_name)  # Green School
# print(s2.school_name)  # Green School



# class Student:
#     school_name = "Green School"  # Class variable

#     def __init__(self, name):
#         self.name = name   # Instance variable

# s1 = Student("Anas")
# s2 = Student("Ali")

# print(s1.school_name)  # Green School
# print(s2.school_name)  # Green School

#changing file name in a folder

# import os 

# List all items and count only files
# file_count = os.listdir("changename")
# print("Files in folder:", len(file_count))
# print("Total files:", file_count)

# for file in file_count:
    # os.rename(os.path.join("changename", file), os.path.join("changename", "new_" + file))

# //////////////////////// class method ///////////////////////

# class Student:

#     school_name = "Green School"

#     def __init__(self, name):
#         self.name = name 
#         print("This is constructor") 

#     @classmethod
#     def get_school_name(cls):
#         return cls("anas")  # Access class variable using cls
    
#     def show(self ,name):
#         print(f"This is a method of the Student class {name}")  
#         self.school_name = "Green School"  # Instance variable

# s = Student.get_school_name()
# # s.name = "Ali"
# # s.show("anas")
# s.get_school_name()

# //////////////////////// class method ///////////////////////


# DIR, DICT, HELP FUNCTIONs

# class Parent:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("This is parent constructor")

# class Student(Parent):

#     def __init__(self, name, age,education):
#         self.education = education
#         super().__init__(name, age)
       
#         print("This is constructor")

# user = Student("Anas", 22, "BSCS")
# print(user.name)
# print(user.age)
# print(user.education)


# single inheritance

# mro docs pyton
# Walrus Operator in Python ///////////////////////////////




# food = "pizza"anas

# print(food :="pizza hut")  # assigning value to the food and then printing it
# print(food)  # Output: pizza hut



# foods = list()

# while (food := input("Enter food name: ")) != "exit":

#     foods.append(food)

# print(foods)  # Output: pizza hut
# ///////////////////////////////////////////////////////////////

# GENERATORS (yield)




# from functools import  lru_cache

# import time 

# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     time.sleep(3)  
#     if n <= 1:
#         return n
#     else:
#         return n

# print(fibonacci(5))
# print(fibonacci(3))
# print(fibonacci(2))
# print(fibonacci(7))
# print(fibonacci(5))
# print(fibonacci(5))
# print(fibonacci(5))
# print(fibonacci(22))
# print(fibonacci(7))
# print(fibonacci(5))



# AsyncIO in Python    (to run await function at a same time )


# import multiprocessing 
# import requests



# def download(url, name):
#     print("Downloaded start")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg",       
#     "wb").write(response.content)
#     print(f"Downloaded {name}")



# if __name__ == "__main__": #(Only run the following block of code if this script is being run directly (not imported by another script))
    
#  url = "https://picsum.photos/seed/picsum/200/300"

#  pros =[]

#  for i in range(5):
#     process = multiprocessing.Process(target=download, args=(url, i))
#     process.start()
#     pros.append(process)  # Append the process to the list


#  for pro in pros:
#     pro.join()  # Wait for the process to finish before starting the next one




# //////////////// to send the notification ////////////////////////

from plyer import notification

notification.notify(
    title='Reminder!',
    message='Take a break and stretch.',
    app_name='MyApp',
    timeout=5  # seconds
)

# //////////////// to send the notification ////////////////////////