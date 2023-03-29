class Fractions:

    def __init__(self, numerator, denominator) -> None:
        if denominator !=0:
            self.n = numerator
            self.q = denominator
        else:
            raise ValueError("Denominator cannot be 0")

    def getDecimal(self):
        return self.n/self.q

    def __add__(self, other):
        return Fractions(self.n*other.q + other.n*self.q, self.q * other.q)
    
    def __sub__(self, other):
        return Fractions(self.n*other.q - other.n*self.q, self.q * other.q)
    
    def __mul__(self, other):
        return Fractions(self.n*other.q, self.q * other.q)
    
    def __eq__(self, other) -> bool:
        return (self.n*other.q == other.n*self.q)
    
    def __str__(self) -> str:
        return f'({self.n}/{self.q})'
    
    
