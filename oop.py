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


def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the original function")
        original_function()
        print("Wrapper executed after the original function")
    return wrapper_function



@decorator_function
def display():
    print("Display function executed")  





# decorator_function(display)()  # This will return the wrapper function/
display()  # Output: Wrapper executed before the original function    



