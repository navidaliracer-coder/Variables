("Hello Dark Knight lets play Rock, Paper, Scissors:")
import random

options = ["Rock", "Paper", "Scissors"]


user_choice = input("Choose Rock, Paper, or Scissors")

computer_choice = random.choice(options)

print("You, Dark Knight have chose:", user_choice)
print("I, Riddler have chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie Dark Knight.")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Scissors cuts Rock, You have won Dark Knight!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock, You have won Dark Knight!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts paper, You have won Dark Knight!")
else:
    print("You have failed Dark Knight")






