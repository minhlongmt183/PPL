from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        env = reduce(lambda acc, ele: self.visit(ele, acc), ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        check = list(filter(lambda x: ctx.name == x.name, o))
        if len(check) > 0:
            raise RedeclaredVariable(ctx.name)
        return o + [ctx]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        check = list(filter(lambda x: ctx.name == x.name,o))
        if len(check) > 0:
            raise RedeclaredConstant(ctx.name)
        return o + [ctx]
        

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        check = list(filter(lambda x: ctx.name == x.name, o))
        if len(check) > 0:
            raise RedeclaredFunction(ctx.name)
        reduce(lambda acc, ele: self.visit(ele, acc), ctx.param + ctx.body, [])
        return o + [ctx]
            

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass