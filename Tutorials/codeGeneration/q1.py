def visitIntLiteral(self, ctx, o):
    a = self.emit.emitPUSHICONST(ctx.value, o.frame)
    return a, IntType()