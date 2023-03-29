'''The program checks whether the user-entered password is
6 to 16 characters long and contains upper case and lower case letters,
digits and special characters'''

pswd = input("Please enter a password: ")

print("--------------------------------------------------------------")

# These variables are flags for each criteria of password validity
length = True
digit = False
upper = False
lower = False
symbol = False
short = False
long = False

if len(pswd) < 6:
    length = False
    short = True
elif len(pswd) > 16:
    length = False
    long = True

for i in range(0, len(pswd)):
    letter = pswd[i]
    code = int(ord(letter))
    if (code == ord("!")) or (code == ord("@")) or (
      code >= ord("#") and code <= ord("%")):
        # The $ character's code point is between # and %
        symbol = True

    if code >= ord("0") and code <= ord("9"):
        # The code points of digits 1-8 are between 0 and 9
        digit = True

    if letter.isupper():
        upper = True

    if letter.islower():
        lower = True

# Validity is assessed based on all required conditions
valid = symbol and digit and upper and lower and length

if valid:
    print("Password is valid")

else:
    # Password is invalid, reasons for invalidity are listed
    print("Password is invalid: \n")
    if not symbol:
        print("- You are missing a special character (! $ # @ %)")

    if not digit:
        print("- You are missing a digit")

    if not upper:
        print("- You are missing an uppercase letter")

    if not lower:
        print("- You are missing a lowercase letter")

    if long:
        print("- The password is longer than 16 characters")

    if short:
        print("The password is shorter than 6 characters")
