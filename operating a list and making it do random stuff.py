#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

#Zip elements of 2 lists 
#Print elements one by one, but the second one be backwords
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


#Zip that dictionary
stocks = ['Microsoft', 'WayneTech', 'Stark industries']
