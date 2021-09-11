 def visitBinExpr(self, ctx, o):
        e1Code, e1Type = self.visit(ctx.e1, o)
        e2Code, e2Type = self.visit(ctx.e2, o)
        End = o.frame.getNewLabel()
        code = e1Code
        

        if ctx.op in ('||'):
            code += self.emit.emitIFTRUE(End, o.frame)
            code += self.emit.emitPOP(o.frame)
            code += e2Code
        elif ctx.op in ('&&'):
            code += self.emit.emitIFFALSE(End, o.frame)
            code += self.emit.emitPOP(o.frame)
            code += e2Code
            
        code += self.emit.emitLABEL(End, o.frame)
 
        return code, e1Type