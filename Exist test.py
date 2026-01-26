#Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program.

for i in range (10):

    #I will now become 5 telling python to kill the program
    if i == 5:

        #Print the kill command
        print(exit)
        exit()
    print(i)