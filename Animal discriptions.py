#Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.

from abc import ABC, abstractmethod

class Batman(ABC):

    def move (self):
        pass

class Comics(Batman):

    def move(self):
        print("I am the orignal one, the canon one")

class Arkham(Batman):
    def move(self):
        print(" I am the one from the games, the most mad and fierce")

class lego(Batman):
    def move(self):
        print("I am the one that is funniest and the one that kids enjoy")
    
class movie(Batman):
    def move(self):
        print("I am the most popular and the one viewed by most")

R = Comics()
R.move
    
G = Arkham()
G.move

T = lego()
T.move

H = movie()
H.move
