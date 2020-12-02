from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visit(ctx.primtype() if ctx.primtype() else ctx.arraytype())

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimens()), self.visit(ctx.primtype()))

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitDimens(self,ctx:MPParser.DimensContext):
        return reduce(lambda x, y: UnionType(x, y), [self.visit(x) for x in ctx.dimen()])
  
    def visitDimen(self,ctx:MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx:MPParser.NumContext):
        return -int(ctx.INTLIT().getText()) if ctx.SIGN() else int(ctx.INTLIT().getText())

