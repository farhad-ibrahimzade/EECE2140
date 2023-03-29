import string

text = input("Enter the text: ") # String

list = [ch for ch in text if ch not in string.punctuation]

cleantext = ''.join(list)

words = cleantext.split()

dict = {} # key = word, value = how many times word appears

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word, amount in dict.items():
    print("Word:", word, "Amount:", amount)