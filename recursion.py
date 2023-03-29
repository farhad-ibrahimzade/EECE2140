
def nums(n):
    if n == 1:
        return 1
    
    return str(nums(n-1)) + ", " +  str(n)
    
print(nums(5))

def reverse(string):
    if string == "":
        return ""
    
    return string[-1] + reverse(string[:-1])
    
print(reverse("hello"))

def gcd(m, n):
    if n == 0:
        return m
    
    return gcd(n, m%n)

print(gcd(24,18))