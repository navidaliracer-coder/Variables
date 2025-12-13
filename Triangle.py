#Take input
print("Half Pyramid pattern of the stars (*):")
n = int(input("Enter the number of rows: "))
#Outer loop to handle number of rows
for i in range(n):
    #inner loop to handle number of collums
    for j in range(i + 1):
        #display result
        print("*", end=" ")
    print()


