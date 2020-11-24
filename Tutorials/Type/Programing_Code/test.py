from functools import reduce
from abc import ABC
from dataclasses import dataclass


class Visitor(ABC):
    def visit(self,ctx,o):
        return ctx.accept(self, o)

class Program: #decl:List[VarDecl],stmts:List[Assign]
    def __init__(self,decl,stmts):
        self.decl,self.stmts = decl,stmts
    def accept(self,visitor,param):
        return visitor.visitProgram(self,param)
    def __str__(self):
        return "{}([{}],[{}])".format("Program",",".join([str(i) for i in self.decl],",".join([str(i) for i in self.stmts])))


class VarDecl: #name:str
    def __init__(self,name):
        self.name = name
    def accept(self,visitor,param):
        return visitor.visitVarDecl(self,param)
    def __str__(self):
        return """{}("{}")""".format("VarDecl",self.name)

class Assign: #lhs:Id,rhs:Exp
    def __init__(self,lhs,rhs):
        self.lhs,self.rhs = lhs,rhs
    def accept(self,visitor,param):
        return visitor.visitAssign(self,param)
    def __str__(self):
        return """{}({},{})""".format("Assign",str(self.lhs),str(self.rhs))

class Exp(ABC): #abstract class
    pass

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def __init__(self,op,e1,e2):
        self.op,self.e1,self.e2 = op,e1,e2
    def accept(self,visitor,param):
        return visitor.visitBinOp(self,param)
    def __str__(self):
        return """{}("{}",{},{})""".format("BinOp",self.op,str(self.e1),str(self.e2))


class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    def __init__(self,op,e):
        self.op,self.e =op,e
    def accept(self,visitor,param):
        return visitor.visitUnOp(self,param)
    def __str__(self):
        return """{}("{}",{})""".format("UnOp",self.op,str(self.e))

class IntLit(Exp): #val:int
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitIntLit(self,param)
    def __str__(self):
        return "{}({})".format("IntLit",str(self.val))

class FloatLit(Exp): #val:float
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitFloatLit(self,param)
    def __str__(self):
        return "{}({})".format("FloatLit",str(self.val))

class BoolLit(Exp): #val:bool
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitBoolLit(self,param)

    def __str__(self):
        return "{}({})".format("BoolLit",str(self.val))

class Id(Exp): #name:str
    def __init__(self,name):
        self.name = name
    def accept(self,visitor,param):
        return visitor.visitId(self,param)
    def __str__(self):
        return "{}({})".format("Id",str(self.name))

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
            left_type = right_type


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



class StaticError(Exception):
    pass

@dataclass
class UndeclaredIdentifier(StaticError):
    target: object
    def __str__(self):
        return  "Undeclared variable "+ str(self.target)

@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Exp

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Assign

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Assign

    def __str__(self):
        return "Type Cannot Be Inferred: "+ str(self.stmt)

StaticCheck().visitProgram(Program([VarDecl("x")],[Assign(Id("x"),BinOp("/",BinOp("+",Id("x"),IntLit(3.4)),BinOp("-",Id("x"),IntLit(2))))])
,
    None
)
