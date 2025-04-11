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
#     def __init__(self, name):
#         self._name = name  # _name is considered 'protected'

#     @property
#     def name(self):
#         print("Getting name...")
#         return self._name

#     @name.setter
#     def name(self, value):
#         print("Setting name...")
#         if not isinstance(value, str):
#             raise ValueError("Name must be a string")
#         self._name = value


# p = Person("Anas")
# print(p.name)      # Getter called
# p.name = "Ali"     # Setter called
# print(p.name)


# NO use of self in the function if it is static method
