#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class Employee:

    def __init__(self):
        print("Employee class has been summoned")

        def __del__(self):
            print("Destructor has been summoned")

def Create_obj():
    print("Creating object...")
    obj = Employee()
    print("Function has been terminated")
    return obj

print('The create object function has been summoned')
obj = Create_obj
print("Program is over...")

