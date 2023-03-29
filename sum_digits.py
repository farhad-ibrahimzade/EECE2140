num = int(input('Input the number: '))

firstDigit = num%10
secondDigit = num%100 // 10
thirdDigit = num%1000 // 100

print('First digit:', firstDigit)
print('Second digit:', secondDigit)
print('Third digit:', thirdDigit)