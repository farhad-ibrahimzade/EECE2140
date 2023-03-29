'''The program checks how many spaces there are in the user-entered text'''

print("--------------------------------------------------------------")

text = input("Enter the text: ")

lst = [i for i in text if i == " "]

spaces = len(lst)

# Use proper grammar for user message
if spaces != 1:
    print("There are", spaces, "spaces in your text")

else:
    print("There is 1 space in your text")
