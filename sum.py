#Input an integer value
n = int(input("Enter the sum you want to calculate:  "))
sum = 0

#Iterates for n=1 times: i = 1, n = 1,
for i in range(1, 1+n):
    sum = sum + i
    print("\nSum =", sum)
