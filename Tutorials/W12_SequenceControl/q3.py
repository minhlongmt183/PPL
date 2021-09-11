    def visitAssign(self,ctx,o):
        right, typeRight = ctx.rhs.accept(self, Access(o.frame, o.sym, False))
        left, typeLeft = ctx.lhs.accept(self, Access(o.frame, o.sym, True))

        self.emit.printout(right + left)