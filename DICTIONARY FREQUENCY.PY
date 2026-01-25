test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask user for the value
value = int(input("Enter the value to check its frequency: "))

# Count frequency of the value
frequency = list(test_dict.values()).count(value)

# Print the result
print("Frequency of", value, "is:", frequency)