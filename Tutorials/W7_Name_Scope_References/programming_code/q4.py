from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        #decl:List[Decl]
        env = reduce(lambda env, ele: self.visit(ele, env), ctx.decl, ({},{}))

    def visitVarDecl(self,ctx:VarDecl,o:object):
        #name:str,typ:Type
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)

        o[0][ctx.name] = ctx.typ

        return o
        

    def visitConstDecl(self,ctx:ConstDecl,o:object):
         #name:str,val:Lit
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)

        o[0][ctx.name] = ctx.val

        return o
        

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
        
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)

        o[0][ctx.name] = None

        outer_scope = o[0].copy()
        outer_scope.update(o[1])

        new_env = ({}, outer_scope)
        lst = ctx.param + ctx.body[0] + ctx.body[1]
        
   
        tmp = reduce(lambda env, ele: self.visit(ele, env), lst, new_env)

        return o
            

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):
        return o

    def visitId(self,ctx:Id,o:object):
        #name:str
        if ctx.name not in o[0] and ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        return o    