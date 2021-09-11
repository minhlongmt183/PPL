class pls_ignore_this_line:
    def visitIf(self, ctx, o):
        ExpCode, ExpType = self.visit(ctx.expr, Access(o.frame, o.sym, False))
        self.emit.printout(ExpCode)

        Middle = o.frame.getNewLabel()
        End = o.frame.getNewLabel()

        self.emit.printout(self.emit.emitIFFALSE(Middle, o.frame))
        self.visit(ctx.tstmt, Access(o.frame, o.sym, False))

        self.emit.printout(self.emit.emitGOTO(End, o.frame))
        self.emit.printout(self.emit.emitLABEL(Middle, o.frame))  # Middle

        if ctx.estmt:
            self.visit(ctx.estmt, Access(o.frame, o.sym, False))

        self.emit.printout(self.emit.emitLABEL(End, o.frame))  # End
