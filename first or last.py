#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)


    print("List of words with first and last characters same\n", lst)
    return ctr 


count = match_words(['abc', 'cfc', 'xyz', 'aba', '1121'])
print("Number of words having first and last characters same:", count)