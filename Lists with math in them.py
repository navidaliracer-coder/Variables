L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list :", L)

count = 0

for i in L:
    count += i


avg = count/len(L)

print("The sum is ", count)
print("The average is", avg)

L.sort()

print("Smallest number is:", L[0])

print("The largest elemement is:", L[-1])