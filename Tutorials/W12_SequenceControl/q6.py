class pls_ignore_this_line:
    def visitFuncDecl(self, ctx, o):
        # Create new frame
        o.frame = Frame(ctx.name, ctx.returnType)
        o.frame.enterScope(True)

        # Function declaration
        InType = [x.typ for x in ctx.param]
        self.emit.printout(self.emit.emitMETHOD(ctx.name, MType(InType, ctx.returnType), True))

        # Function parameter
        LocalScope = []
        for pr in ctx.param:
            prSym = self.visit(pr, SubBody(o.frame, LocalScope))
            LocalScope += [prSym]

        # Function declaration part
        for decl in ctx.body[0]:
            declSym = self.visit(decl, SubBody(o.frame, LocalScope))
            LocalScope += [declSym]

        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))  # Function body begin here

        for stm in ctx.body[1]:
            self.visit(stm, o)

        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))  # Function body end here

        self.emit.printout(self.emit.emitENDMETHOD(o.frame))
        o.frame.exitScope()

        return Symbol(ctx.name, MType([], ctx.returnType), CName(self.className))
