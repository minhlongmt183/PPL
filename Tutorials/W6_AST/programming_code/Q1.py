class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        #program: vardecls EOF;
        return self.visitVardecls(ctx.vardecls()) + 1

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
       # vardecls: vardecl vardecltail;
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())


    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        # vardecltail: vardecl vardecltail |
        if ctx.getChildCount() > 0:
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())
        else:
            return 0

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        # vardecl: mptype ids ';' ;

        return 1 + self.visitMptype(ctx.mptype()) + self.visitIds(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1

    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() > 1:
            return 2 + self.visitIds(ctx.ids())
        else:
            return 1