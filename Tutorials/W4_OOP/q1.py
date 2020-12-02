from abc import ABC, abstractmethod
class Type:
    def __init__(self, type):
        self.type = type

class Type:
    def __init__(self, type):
        self.type = type
class Eval(Type):
    def __init__(self):
        super().__init__("eval")
class PrintPrefix(Type):
    def __init__(self):
        super().__init__("prefix")
class PrintPostfix(Type):
    def __init__(self):
        super().__init__("postfix")



class Exp(ABC):
    @abstractmethod
    def eval(self): 
        pass

    @abstractmethod
    def printPrefix():
        pass

    @abstractmethod
    def printPostfix():
        pass

    def accept(self, type):
        if type.type == "eval":
            return self.eval()
        elif type.type == "prefix":
            return self.printPrefix()
        elif type.type == "postfix":
            return self.printPostfix()

class IntLit(Exp):
    def __init__(self, num):
        self.num = num
    
    def eval(self):
        return self.num
    
    def printPrefix(self):
        return str(self.num)

    def printPostfix(self):
        return str(self.num)

class FloatLit(Exp):
    def __init__(self, num):
        self.num = num
    
    def eval(self):
        return self.num

    def printPrefix(self):
        return str(self.num)

    def printPostfix(self):
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
    
    def printPostfix(self):
        return self.operand.printPostfix() + ' ' + self.operator  + '.'
    

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
    

    def printPostfix(self):
        return self.left.printPostfix()+ ' ' + self.right.printPostfix() + ' ' + self.operator 

x = IntLit(1)
y = IntLit(2)

exp = BinExp(x, '+', y)
exp.eval()
print(exp.printPostfix())