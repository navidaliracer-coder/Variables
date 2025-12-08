#Take two nput form the user
lower = int(input("enter an lower range:  "))
upper = int(input("enter an upper range:  "))
print("Prime number in between", lower, "and", upper, "are:")

#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
    #all prime numbers are greater then one
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
             break
        else:
            print(num)
            