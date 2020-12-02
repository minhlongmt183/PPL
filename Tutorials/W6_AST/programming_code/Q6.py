
from functools import reduce
class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Expr(ABC):
    __metalclass__ = ABCMeta
    pass

class Binary(Expr):  #op:string;left:Expr;right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "Binary(" + self.op + ","+ str(self.left) +"," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinary(self, param)

class Id(Expr): #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Id(" + self.value + ")"

    def accept(self, v , param):
        return v.visitId(self, param)

class IntLiteral(Expr): #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class BooleanLiteral(Expr): #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)


class ASTGeneration(MPVisitor):


    def visitProgram(self,ctx:MPParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return ctx.term(0).accept(self)

        right = ctx.term()[-1].accept(self)
        zipped = list(zip(ctx.term()[:-1], ctx.ASSIGN()))[::-1]
        return reduce(lambda a, b: Binary(b[1].getText(), b[0].accept(self), a), zipped, right)

    def visitTerm(self,ctx:MPParser.TermContext):

        if ctx.getChildCount() == 1:
            return ctx.factor(0).accept(self)

        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))


    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.operand(0).accept(self)

        left = ctx.getChild(0).accept(self)
        zipped = zip(ctx.operand()[1:], ctx.ANDOR())
        return reduce(lambda a, b: Binary(b[1].getText(), a, b[0].accept(self)), zipped, left)

    def visitOperand(self,ctx:MPParser.OperandContext):

        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        
        return ctx.exp().accept(self)
