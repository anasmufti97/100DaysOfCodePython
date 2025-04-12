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








class Student:

    school_name = "Green School"
    def show(self):
        print(f"This is a method of the Student class {self.name}")  
        self.school_name = "Green School"  # Instance variable



s = Student()
s.name = "Ali"
s.show()


b= Student()
b.show()


