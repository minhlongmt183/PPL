
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
         #decl:List[VarDecl],stmts:List[Stmt]
        reduce(lambda env, elem: self.visit(elem, env), ctx.decl + ctx.stmts, ({},{}))

    def visitVarDecl(self,ctx:VarDecl,o):#name:str
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        
        o[0][ctx.name] = None
        return o
 
    def visitBlock(self,ctx:Block,o):
        #decl:List[VarDecl],stmts:List[Stmt]
        outer_env = o[1].copy()
        outer_env.update(o[0])


        new_env = ({},outer_env) 
        new_env = reduce(lambda env, elem: self.visit(elem, env), ctx.decl + ctx.stmts, new_env)
        
        for name in new_env[1]:
            if (not self.getType(name, o)) and (new_env[1][name]):
                self.updateType(name, new_env[1][name], o)

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


    def visitBinOp(self,ctx:BinOp,o):
        # op:str,e1:Exp,e2:Exp
        left_type   = self.visit(ctx.e1,o)
        right_type  = self.visit(ctx.e2,o)


        if ctx.op in ['+', '-', '*', '/']:
            if not left_type:
                self.updateType(ctx.e1.name, IntType(), o)
                left_type = IntType()
            
            if not right_type:
                self.updateType(ctx.e2.name, IntType(), o)
                right_type = IntType()

            if (type(left_type) == type(right_type)) and (type(left_type)== IntType):
                return IntType()

        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if not left_type:
                self.updateType(ctx.e1.name, FloatType(), o)
                left_type = FloatType()
            
            if not right_type:
                self.updateType(ctx.e2.name, FloatType(), o)
                right_type = FloatType()

            if (type(left_type) == type(right_type)) and (type(left_type)== FloatType):
                return FloatType()

        elif ctx.op in ['>', '=']:
            if not left_type:
                self.updateType(ctx.e1.name, IntType(), o)
                left_type = IntType()
            
            if not right_type:
                self.updateType(ctx.e2.name, IntType(), o)
                right_type = IntType()

            if (type(left_type) == type(right_type)) and (type(left_type)== IntType):
                return BoolType()

        elif ctx.op in ['>.', '=.']:
            if not left_type:
                self.updateType(ctx.e1.name, FloatType(), o)
                left_type = FloatType()
            
            if not right_type:
                self.updateType(ctx.e2.name, FloatType(), o)
                right_type = FloatType()

            if (type(left_type) == type(right_type)) and (type(left_type)== FloatType):
                return BoolType()

        elif ctx.op in ['&&', '||', '>b' , '=b' ]:
            if not left_type:
                self.updateType(ctx.e1.name, BoolType(), o)
                left_type = BoolType()
            
            if not right_type:
                self.updateType(ctx.e2.name, BoolType(), o)
                right_type = BoolType()

            if (type(left_type) == type(right_type)) and (type(left_type)== BoolType):
                return BoolType()

        raise TypeMismatchInExpression(ctx)



    def visitUnOp(self,ctx:UnOp,o):
        #op:str,e:Exp #op is -,-., !,i2f, floor

        param_type = self.visit(ctx.e, o)

        if ctx.op == '-':
            if not param_type:
                self.updateType(ctx.e.name, IntType(), o)
                return IntType()
            
            if type(param_type) is IntType:
                return IntType()

        elif ctx.op == '-.':
            if not param_type:
                self.updateType(ctx.e.name, FloatType(), o)
                return FloatType()
            
            if type(param_type) is FloatType:
                return FloatType()

        elif ctx.op == '!':
            if not param_type:
                self.updateType(ctx.e.name, BoolType(), o)
                return BoolType()

            if type(param_type) is BoolType:
                return BoolType()

        elif ctx.op == 'i2f':
            if not param_type:
                self.updateType(ctx.e.name, IntType(), o)
                return FloatType()
            
            if type(param_type) is IntType:
                return FloatType()


        elif ctx.op == 'floor':
            if not param_type:
                self.updateType(ctx.e.name, FloatType(), o)
                return IntType()

            if type(param_type) is FloatType:
                return IntType()

        raise TypeMismatchInExpression(ctx) 


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
