from abc import ABC, abstractmethod



class Exp(ABC):
    @abstractmethod
    def eval(self): 
        pass

    @abstractmethod
    def printPrefix():
        pass


class IntLit(Exp):
    def __init__(self, num):
        self.num = num
    
    def eval(self):
        return self.num
    
    def printPrefix(self):
        return str(self.num)


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num
    
    def eval(self):
        return self.num

    def printPrefix(self):
        return str(self.num)
   

class UnExp(Exp):
    def __init__(self, operator, operand):
        assert operator in "+-", "not support"
        self.operator = operator
        self.operand = operand

    def eval(self):
        v = self.operand.eval()
        v = v if self.operator == '+' else -v
        return v
    
    def printPrefix(self):
        return self.operator + '. ' + self.operand.printPrefix()
    
    

class BinExp(Exp):
    def __init__(self, left, operator, right):
        assert operator in "+-*/", "operand is not support"
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        a = self.left.eval()
        b = self.right.eval()

        if self.operator == "+":
            v = a + b
        elif self.operator == "-":
            v = a - b
        elif self.operator == "*":
            v = a * b
        elif self.operator == "/":
            v = a / b

        return v

    def printPrefix(self):
        return self.operator + ' ' + self.left.printPrefix() + ' ' + self.right.printPrefix()
    

x = IntLit(1)
y = IntLit(2)

exp = BinExp(x, '+', y)
exp.eval()
print(exp.printPrefix())