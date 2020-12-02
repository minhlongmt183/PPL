#Question 2
class Rational:
    def gcd(self, a, b):
        return a if b==0 else self.gcd(b, a%b)

    def __init__(self, n = 0, d = 1):
        assert(d != 0)
        g = self.gcd(abs(n), abs(d))
        self.numer = int(n / g)
        self.denom = int(d / g)

    #+
    def __add__(self, that):
        typeOfThat = type(that).__name__
        if typeOfThat == 'int':
            that = Rational(that)
            return Rational(self.numer * that.denom + self.denom * that.numer,
            self.denom * that.denom)
        elif typeOfThat == 'Rational':
            return Rational(self.numer * that.denom + self.denom * that.numer,
            self.denom * that.denom)
        else:
            assert((type(that).__name__ == 'Rational') or type(that).__name__ == 'int'),"The type of parameter must be int or Rational"
    
    #toString
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

#Question 3
class Expr:
    pass

class Var(Expr):
    def __init__(self, name):
        self.name = name
    def eval(self):
        return 1

class Number(Expr):
    def __init__(self, num):
        self.num = num
    def print(self):
        print(str(self.num))
    def eval(self):
        return self.num

class UpOn(Expr):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg

class BinOp(Expr):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right
    def eval(self):
        if self.operator == "+":
            return Number(self.left.eval() + self.right.eval())
        elif self.operator == "-":
            return Number(self.left.eval() - self.right.eval())
        elif self.operator == "*":
            return Number(self.left.eval() * self.right.eval())
        elif self.operator == "/":
            return Number(self.left.eval() / self.right.eval())


t = BinOp('*',BinOp('+',Var('x'),Number(0.2)),Number(3))
t.eval().print()