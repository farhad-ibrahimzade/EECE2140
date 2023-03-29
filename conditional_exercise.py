year = int(input("Please enter the year: "))

answer = "leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "not a leap year"

print("This year is", answer)