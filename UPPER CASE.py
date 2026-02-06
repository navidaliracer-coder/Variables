#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString():
     #User writes what he wants to get uppercased
    def __init__(self):
        self.str1 = ""

     #Makes the string uppercase
    def get_String(self):
        self.str1 = input("Enter String :")

    def print_String(self):
        print("Result :", self.str1.upper())

str1 = IOString

str1.get_String()
str1.print_String()
