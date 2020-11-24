class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))
        # return Program([VarDecl(Id(ctx.ID().getText()),[],None)])


    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return [VarDecl(x, ctx.mptype().accept(self)) for x in ctx.ids().accept(self)]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + ctx.ids().accept(self)

