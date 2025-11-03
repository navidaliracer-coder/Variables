#input a word
text =str(input("enter a string: "))

# Reverse string
# Using step value as -1 to inerate in reverse
revText = text[::-1]
text = revText

print("Reverse of given string is:")
print (text)