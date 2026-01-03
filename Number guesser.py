import random
playing = True
number = str(random.randint(10,20))

print("Hello Dark Knight, lets see if your imbecilec mind can play a guessing game. ")
print("I will generate a number from 10 to 20, and you have to guess it, simple.")
print("The game ends when you get the number right")
print("Best of luck Dark Knight")

while playing:
    guess = input("Give me your best guess Dark Knight! \n")
    if number == guess:
        print("You have somehow got it correct with a brain the size of a Bat, Dark Knight")
        print("The number you entered Dark Knight was.....")
        print(number,"!")
        break

else:
    print("You have failed Dark Knight, I am nothing if not genourous!")
    print("So fail again, Dark Knight")
