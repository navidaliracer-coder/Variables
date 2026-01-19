#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, "Coding" : 1}

#printing original dictionary 
print("The original dictionary :" + str(test_dict))

#initialize value
K = 2

#using loop 
#Selective key values in dictionary
res = 0
for key in test_dict:
     if test_dict[key] == K:
          res = res + 1


#Printing result 
print("The frequency of K is : " + str(res))