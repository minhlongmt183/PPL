from abc import ABC, abstractmethod

class Exp:
    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def printPrefix(self):
        pass

class IntLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number
    def printPrefix(self):
        return str(self.number)

class FloatLit(Exp):
    def __init__(self, number):
        self.number = number

    def eval(self):
        return self.number

    def printPrefix(self):
        return str(self.number)

class BinExp(Exp):
    def __init__(self, left, operator, right):
        assert operator in "+-*/", "operator is not supported"
        self.left = left
        self.right = right
        self.operator = operator

    def eval(self):
        a = self.left.eval()
        b = self.right.eval()
        
        if self.operator == '+':
            v = a + b
        elif self.operator == '-':
            v = a - b
        elif self.operator == '*':
            v = a * b
        elif self.operator == '/':
            v = a / b

        return v

class UnExp(Exp):
    def __init__(self, operator, operand):
        assert operator in "+-*/", "operator is not supported"
        self.operand = operand
        self.operator = operator

    def eval(self):
        v = self.operand.eval()

        return v if self.operator == '+' else -v

a = IntLit(1)
b = IntLit(2)

exp = BinExp(a, '+', b)
print(exp.eval())
