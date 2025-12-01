#input number greater then 1
n = int(input("Enter your value of n:  "))

#print the numbers 1 to 10
print("numbers from {0} to {1} are: ".format(n,1))

#loop to print numbers  
for i in range(n,0, -1):
    print(i)
