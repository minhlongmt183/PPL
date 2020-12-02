
from functools import reduce
from abc import ABCMeta

class Type(ABC): #abstract class
    pass
class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass


class StaticCheck(Visitor):

    def updateType(self, name, new_type, o):
        if name in o[0]:
            o[0][name] = new_type
        else:
            o[1][name] = new_type
        
        return o
    
    def getType(self, name, o):
        return o[0][name] if name in o[0] else o[1][name]

    def visitProgram(self,ctx:Program,o):
        #decl:List[Decl],stmts:List[Stmt]
        reduce(lambda env, elem: self.visit(elem, env), ctx.decl + ctx.stmts, ({},{}))

    def visitVarDecl(self,ctx:VarDecl,o): 
        #name:str
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        
        o[0][ctx.name] = None
        return o


    def visitFuncDecl(self,ctx:FuncDecl,o):
        #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        
        outer_env = o[1].copy()
        outer_env.update(o[0])
        
        new_env = ({},outer_env)
        reduce(lambda env, elem: self.visit(elem, env), ctx.param + ctx.local + ctx.stmts, new_env)

        param_type = [self.getType(var.name, new_env) for var in ctx.param]
        o[0][ctx.name] = param_type

        for name in outer_env:
            if name in new_env[0]:
                continue

            if (not self.getType(name, o)) and (outer_env[name]):
                self.updateType(name, outer_env[name], o)

        return o



    def visitCallStmt(self,ctx:CallStmt,o):
        # name:str,args:List[Exp]
        if (ctx.name not in o[0]):
            raise UndeclaredIdentifier(ctx.name)
        
        param_type  = self.getType(ctx.name, o)
        arg_type    = [self.visit(arg, o) for arg in ctx.args]
        

        if (type(param_type) is not list) or (len(arg_type) != len(param_type)):
            raise TypeMismatchInStatement(ctx)
        
        for i in range(len(arg_type)):
            if (not param_type[i]) and (not arg_type[i]):
                raise TypeCannotBeInferred(ctx)
            elif not param_type[i]:
                param_type[i] = arg_type[i]
            elif (not arg_type[i]):
                self.updateType(ctx.args[i].name, param_type[i], o)
            elif type(arg_type[i]) != type(param_type[i]):
                raise TypeMismatchInStatement(ctx)
        
        self.updateType(ctx.name,param_type, o)
        
        return o



    def visitAssign(self,ctx:Assign,o):
        #lhs:Id,rhs:Exp
        exp_type    = self.visit(ctx.rhs, o)
        id_type     = self.visit(ctx.lhs, o)

        if (not id_type) and (not exp_type):
            raise TypeCannotBeInferred(ctx)

        elif not id_type:
            self.updateType(ctx.lhs.name, exp_type, o)
            
        elif not exp_type:
            self.updateType(ctx.rhs.name, id_type, o)
                
        elif type(id_type) != type(exp_type):
            raise TypeMismatchInStatement(ctx)

        return o

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self, ctx, o):
        if ctx.name not in o[0] and ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
            
        return self.getType(ctx.name, o)


