    def visitVarDecl(self,ctx,o):
        # Frame for a local/parameter declaration and None for a global declaration.
        # o: name in str type, mtype in Type type and val in Val type
        # Val type: Index, CName
        
        if o.frame == None:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False))
            return Symbol(ctx.name, ctx.typ, CName(self.className))
        else:
            idx =  o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx,ctx.name, ctx.typ,o.frame.getStartLabel(),o.frame.getEndLabel()))
    
        return Symbol(ctx.name, ctx.typ, Index(idx))