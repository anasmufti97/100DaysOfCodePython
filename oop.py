class MyClass:
    def __init__(self, name):
        self.name = name
        print("this is constructor")

    def greet(self):
        print(f"Hello, {self.name}!")

# Creating an instance of MyClass
my_object = MyClass("Anas")
my_object.greet()  # Output: Hello, Anas!     




# DECORATORS = Take function as an argument and modify it 