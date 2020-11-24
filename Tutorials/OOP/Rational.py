
class Rational():

    def __init__(self, n = 0, d = 1):
        assert d!= 0 , "d is nonzero"
        
        self.g = self.__gcd(n, d)

        self.numer = n // self.g
        self.denom = d // self.g

    def __gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.__gcd(b, a % b)

    def __add__(self, other):
        number = self.numer * other.denom + other.number * self.denom
        demon = self.denom * other.denom

        return(Rational(number, denom))

    def __str__(self):
        return (str(self.numer) + ' / ' + str(self.denom))

x = Rational(3, 1)
print(str(x))
        
    