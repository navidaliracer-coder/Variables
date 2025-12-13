#Take input from the user
rows = int(input("Please enter the total number of Rows  :  "))
number = 1 #Initialize by 1

print("Floyd's Triangle")
#Outer loop for number of rows
for i in range(1, rows + 1):
    #Inner loop for number of columns
    for j in range (1, i + 1):
        #Display result
        print(number, end = ' ')
        number = number + 1 
    print()