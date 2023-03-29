import math


a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
x2 = (-b - math.sqrt(b**2-4*a*c))/2*a

print('First root:', x1)
print('Second root', x2)