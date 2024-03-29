

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return ctx.term().accept(self)
        return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self))

    def visitTerm(self,ctx:MPParser.TermContext):
        if ctx.getChildCount() == 1:
            return ctx.factor(0).accept(self)
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))


    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.operand().accept(self)
        return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), ctx.operand().accept(self))


    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        return ctx.exp().accept(self)

