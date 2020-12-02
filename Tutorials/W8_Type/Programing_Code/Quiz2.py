from functools import reduce
from abc import ABCMeta

class Type(ABC): #abstract class
    pass
class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        #decl:List[VarDecl],exp:Exp
        tmp = reduce(lambda env, elem: self.visit(elem, env), ctx.decl, {})
        self.visit(ctx.exp, tmp)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = ctx.typ
        return o

    def visitIntType(self,ctx:IntType,o):pass


    def visitFloatType(self,ctx:FloatType,o):pass

    def visitBoolType(self,ctx:BoolType,o):pass

    def visitBinOp(self,ctx:BinOp,o):
        left_type = type(self.visit(ctx.e1,o))
        right_type = type(self.visit(ctx.e2,o))
        
        if ctx.op in ['+', '-', '*']:
            if BoolType in [left_type, right_type]:
                raise TypeMismatchInExpression(ctx)
            if FloatType in [left_type, right_type]:
                return FloatType()
            return IntType()
        elif ctx.op in ['/']:
            if BoolType in [left_type, right_type]:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif ctx.op in ['&&', '||']:
            if left_type == BoolType and right_type == BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>', '<', '==', '!=']:
            if left_type != right_type:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            

    def visitUnOp(self,ctx:UnOp,o):
        param_type = self.visit(ctx.e, o)
        if ctx.op == '-':
            if type(param_type) == BoolType:
                raise TypeMismatchInExpression(ctx)
            return param_type
        elif ctx.op == '!':
            if type(param_type) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return param_type
            

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()
            
    def visitId(self, ctx, o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name) 
