#Input a word or a string
Name = input("Please enter your name: ")

NameBackwords = ('')
#loop for reversing the string
for i in Name:
    NameBackwords = i + NameBackwords

print("\nYour Name:", Name)
print("Your name BACKWORDS! :", NameBackwords)

