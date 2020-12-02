def visitBinExpr(self,ctx,o):
    left, typeLeft = ctx.e1.accept(self, o)
    right, typeRight = ctx.e2.accept(self, o)

    if ctx.op in ['+', '-', '+.', '-.']:
        c = self.emit.emitADDOP(ctx.op[0], typeLeft, o.frame)
    else:
        c = self.emit.emitMULOP(ctx.op[0], typeLeft, o.frame)
    
    return left + right + c, typeLeft



        

