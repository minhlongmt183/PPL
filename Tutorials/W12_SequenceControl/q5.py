class pls_ignore_this_line:
    def visitWhile(self, ctx, o):
        o.frame.enterLoop()  # Start loop
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))  # Continue

        start = o.frame.getNewLabel()
        end = o.frame.getNewLabel()

        self.emit.printout(self.emit.emitLABEL(start, o.frame))  # Start

        ExpCode, ExpType = self.visit(ctx.expr, Access(o.frame, o.sym, False))
        self.emit.printout(ExpCode)  # Condition

        self.emit.printout(self.emit.emitIFFALSE(end, o.frame))  # If condition dissatisfy

        self.visit(ctx.stmt, o)  # Code

        self.emit.printout(self.emit.emitGOTO(start, o.frame))  # Restart

        self.emit.printout(self.emit.emitLABEL(end, o.frame))  # End
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))  # Break
        o.frame.exitLoop()  # End loop
