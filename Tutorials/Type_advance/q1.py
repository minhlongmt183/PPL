from functools import reduce
from abc import ABCMeta

class Type(ABC): #abstract class
    pass
class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        #decl:List[VarDecl],stmts:List[Assign]
        check1 = reduce(lambda env, elem: self.visit(elem, env), ctx.decl + ctx.stmts, {})

    def visitVarDecl(self,ctx:VarDecl,o):#name:str
        o[ctx.name] = None
        return o

    def visitAssign(self,ctx:Assign,o):
        #lhs:Id,rhs:Exp
        id_type = self.visit(ctx.lhs, o)
        type_of_exp = self.visit(ctx.rhs,o)

        if id_type == None:
            id_type = self.visit(ctx.lhs, o)


        if id_type == None:
            if type_of_exp == None:
                raise TypeCannotBeInferred(ctx)
            else:
                o[ctx.lhs.name] = type_of_exp
        elif type_of_exp == None:
            o[ctx.rhs.name] = id_type
        else:
            if type(id_type) != type(type_of_exp):
                raise TypeMismatchInStatement(ctx)

        return o


    def visitBinOp(self,ctx:BinOp,o):
        # op:str,e1:Exp,e2:Exp
        left_type = self.visit(ctx.e1,o)
        right_type = self.visit(ctx.e2,o)


        if (type(left_type) == type(None)) and (type(right_type) != type(None)):
            o[ctx.e1.name] = right_type
            left_type = right_type
        elif (type(left_type) != type(None)) and (type(right_type) == type(None)):
            o[ctx.e2.name] = left_type
            right_type = left_type


        if ctx.op in ['+', '-', '*', '/']:

            if (type(left_type)== IntType) and (type(right_type) == IntType):
                return IntType()

            if type(left_type) == type(None):
                o[ctx.e1.name] = IntType()
                o[ctx.e2.name] = IntType()
                return IntType()

            raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if (type(left_type)== FloatType) and (type(right_type) == FloatType):
                return FloatType()

            if type(left_type) == type(None):
                o[ctx.e1.name] = FloatType()
                o[ctx.e2.name] = FloatType()
                return FloatType()

            raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['>', '=']:
            if (type(left_type)== IntType) and (type(right_type) == IntType):
                return BoolType()

            if type(left_type) == type(None):
                o[ctx.e1.name] = IntType()
                o[ctx.e2.name] = IntType()
                return BoolType()

            raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['>.', '=.']:
            if (type(left_type)== FloatType) and (type(right_type) == FloatType):
                return BoolType()

            if type(left_type) == type(None):
                o[ctx.e1.name] = FloatType()
                o[ctx.e2.name] = FloatType()
                return BoolType()

            raise TypeMismatchInExpression(ctx)

        elif ctx.op in ['&&', '||', '>b' , '=b' ]:
            if (type(left_type)== BoolType) and (type(right_type) == BoolType):
                return BoolType()

            if type(left_type) == type(None):
                o[ctx.e1.name] = BoolType()
                o[ctx.e2.name] = BoolType()
                return BoolType()

            raise TypeMismatchInExpression(ctx)



    def visitUnOp(self,ctx:UnOp,o):
        param_type = self.visit(ctx.e, o)
        if ctx.op == '-':
            if type(param_type) == type(None):
                o[ctx.e.name] = IntType()
                return IntType()
            elif type(param_type) != IntType:
                raise TypeMismatchInExpression(ctx)
            return param_type

        if ctx.op == '-.':
            if type(param_type) == type(None):
                o[ctx.e.name] = FloatType()
                return FloatType()
            elif type(param_type) != FloatType:
                raise TypeMismatchInExpression(ctx)
            return param_type

        if ctx.op == '!':
            if type(param_type) == type(None):
                o[ctx.e.name] = BoolType()
                return BoolType()
            elif type(param_type) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return param_type

        if ctx.op == 'i2f':
            if type(param_type) == type(None):
                o[ctx.e.name] = IntType()
            elif type(param_type) != IntType:
                raise TypeMismatchInExpression(ctx)

            return FloatType()


        if ctx.op == 'floor':
            if type(param_type) == type(None):
                o[ctx.e.name] = FloatType()
            elif type(param_type) != FloatType:
                raise TypeMismatchInExpression(ctx)

            return IntType()


    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]

