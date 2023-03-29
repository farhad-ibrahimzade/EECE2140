
# First thought - use lists
firstWord = input("Enter the first word: ")

secondWord = input("Enter the first word: ")

firstLst = sorted(char for char in firstWord)
secondLst = sorted(char for char in secondWord)

if firstLst == secondLst:
    print("The words are Anagrams")

else:
    print("The words are not Anagrams")

# More efficient - use dictionaries to get the total count of all letters in the words and then compare the dictionaries

dict1 = {}

dict2 = {}

for char in firstWord:
    if char in dict1:
        dict1[char] +=1
    else:
        dict1[char] = 1

for char in secondWord:
    if char in dict2:
        dict2[char] +=1
    else:
        dict2[char] = 1

if dict1 == dict2:
    print("The words are Anagrams")

else:
    print("The words are not Anagrams")