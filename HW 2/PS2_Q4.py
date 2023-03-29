'''The program returns the first non repeated character
 from user-entered text'''

print("--------------------------------------------------------------")

text = input("Please enter the string: ")

nonRepeated = None

for char in text:
    if text.count(char) == 1:
        nonRepeated = char
        break

# Check if characters were repeated
if nonRepeated:
    print("The first non repeated character is", nonRepeated)

else:
    print("All characters are repeated")
