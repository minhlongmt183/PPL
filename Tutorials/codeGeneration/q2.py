def visitFloatLiteral(self,ctx,o):
    c = self.emit.emitPUSHFCONST(ctx.value, o.frame)
    return c, FloatType()