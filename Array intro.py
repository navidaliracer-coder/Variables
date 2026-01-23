#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

import array as arr

#Rise my array, RISE
array_num = arr.array('i', [1, 2, 5, 3, 7, 9, 3])
print("Original array:  "+str(array_num))

#Count dem occurences
print("Number of occurences of number 3 in this array is:",str(array_num.count(3)))

#Array does goes BACKWORDS
array_num.reverse()
print("REVERSE")
print(str(array_num))


