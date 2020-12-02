    def visitBinExpr(self,ctx,o):
        left, typeLeft      = ctx.e1.accept(self, o)
        right, typeRight    = ctx.e2.accept(self, o)
        inType              = typeLeft
    
        if (type(typeLeft) is IntType) and (type(typeRight) is FloatType):
            left += self.emit.emitI2F(o.frame)
            inType = typeRight
        elif  (type(typeLeft) is FloatType) and (type(typeRight) is IntType):
            right += self.emit.emitI2F(o.frame)
        
    
        if ctx.op in ['+', '-']:
            c = self.emit.emitADDOP(ctx.op, inType, o.frame)
        elif ctx.op in ['*', '/']:
            if (ctx.op is '/' and type(inType) is IntType):
                left    += self.emit.emitI2F(o.frame)
                right   += self.emit.emitI2F(o.frame)
                inType   = FloatType()

            c = self.emit.emitMULOP(ctx.op, inType, o.frame)
            
        else:
            c = self.emit.emitREOP(ctx.op, inType, o.frame)
        
        if ctx.op in ['+', '-' ,'*']:
            if FloatType in [type(typeLeft), type(typeRight)]:
                typeResult = FloatType()
            else:
                typeResult = IntType()
            
        elif ctx.op is '/':
            typeResult = FloatType()
        else:
            typeResult = BoolType()
        
        return left + right + c, typeResult