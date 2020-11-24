from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from functools import reduce
from AST import *

class ASTGeneration(BKITVisitor):


    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return ctx.term(0).accept(self)

        right = ctx.term()[-1].accept(self)
        zipped = list(zip(ctx.term()[:-1], ctx.ASSIGN()))[::-1]
        return reduce(lambda a, b: Binary(b[1].getText(), b[0].accept(self), a), zipped, right)

    def visitTerm(self,ctx:BKITParser.TermContext):

        if ctx.getChildCount() == 1:
            return ctx.factor(0).accept(self)

        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))


    def visitFactor(self,ctx:BKITParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.operand(0).accept(self)

        left = ctx.getChild(0).accept(self)
        zipped = zip(ctx.operand()[1:], ctx.ANDOR())
        return reduce(lambda a, b: Binary(b[1].getText(), a, b[0].accept(self)), zipped, left)

    def visitOperand(self,ctx:BKITParser.OperandContext):

        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        
        return ctx.exp().accept(self)


